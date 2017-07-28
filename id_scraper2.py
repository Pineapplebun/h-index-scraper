from selenium import webdriver #browser
from selenium.webdriver.support.ui import Select #select elements only
from selenium.webdriver.support import expected_conditions as EC #waits
from selenium import webdriver #browser
from selenium.webdriver.support.ui import Select #select elements only
from selenium.webdriver.support import expected_conditions as EC #waits
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys #key support
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import excel_parser
import hindexscraper2 as hs2
import os
import time
import re

def scrape_id(authorIdPath):
    """ (str) -> None
    
    Precondition: id_folder must  must be the folder directory of an excel file 
    called authorId whose first column is blank, second column is their last name, 
    third column is their first name, and fourth column is their university.
    
    Searches the authorId on Scopus from an authorId excel file specified in id_folder
    and adds it into the corresponding column.
    """
    
    excel_file_path = authorIdPath + "//authorId.xlsx"
    search_author = "https://www-scopus-com.myaccess.library.utoronto.ca/search/form.uri?display=authorLookup&clear=t&origin=searchbasic&txGid=0"
    download_dir = authorIdPath
    
    #initialize the web browser, set download directory and chromeDriver path
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : download_dir}
    chromeOptions.add_experimental_option("prefs", prefs)
    chromePath = "C:\\Python34\\selenium\\chromedriver.exe"    
    driver = webdriver.Chrome(executable_path = chromePath, chrome_options=chromeOptions)
    driver.implicitly_wait(2)
    
    names = excel_parser.authors(excel_file_path)
    print(names)
    
    for author in names:
        driver.get(search_author)
        driver.find_element_by_id("lastname").send_keys(names[author][0])
        driver.find_element_by_id("firstname").send_keys(names[author][1])
        driver.find_element_by_id("institute").send_keys(names[author][2])
        driver.find_element_by_id("authorSubmitBtn").click()
        
        try:
            author_id = driver.find_element_by_id("hiddenRow1").get_attribute('innerHTML')
            print(author_id)
            regex = r"[0-9]+"
            matches = re.findall(regex, author_id)
            print(matches)
            names[author].append(int(matches[0]))
            
            try:
                another = driver.find_element_by_id("hiddenRow2").get_attribute('innerHTML')
                print("found more than one result, need to re-examine")
                names[author].append("found more than one result, need to re-examine")
            except:
                continue
            
        except NoSuchElementException:
            print("Could not find any authors")
            names[author].append("NOT FOUND!")
            continue
            
    
    excel_parser.add_id(names, excel_file_path)
    print("PARSING COMPLETE")
    driver.close()
    
    hs2.scrape_hindex(excel_file_path, authorIdPath)