""" STEP 1: Download files
PLEASE VERIFY/CHANGE BEFORE RUNNING: 
1. download directory 
2. chromeDriver path (read 3.)
3. requires selenium library and chromeDriver: http://chromedriver.storage.googleapis.com/index.html?path=2.22/
4. excel read file path
5. set number of arrow down button for each year
"""
from selenium import webdriver #browser
from selenium.webdriver.support.ui import Select #select elements only
from selenium.webdriver.support import expected_conditions as EC #waits
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys #key support
from selenium.webdriver.common.by import By
import excel_parser
import os
import time

def scrape_hindex(excel_file_path, authorIdPath):
    """ (str, str) -> None
    
    Finds the author on Scopus from an authorId file specified in the id_folder
    and downloads it in the folder_name within the h-index-scraper files folder.
    
    >>> scrape_hindex("C:\", "C:\")
    
    """
    download_dir = authorIdPath
    rename_dir = authorIdPath
    authorIdList = excel_parser.createAuthorList(excel_file_path)
    print(authorIdList)
    num_authors = len(authorIdList)
    scopusAuthor = 'https://www-scopus-com.myaccess.library.utoronto.ca/authid/detail.uri?authorId='
    start_date = 11
    end_date = 1
    
    #initialize the web browser, set download directory and chromeDriver path
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : download_dir}
    chromeOptions.add_experimental_option("prefs", prefs)
    chromePath = "C:\\Python34\\selenium\\chromedriver.exe"
    
    driver = webdriver.Chrome(executable_path = chromePath, chrome_options=chromeOptions)
    driver.implicitly_wait(20)
    
    #iterate through list of authors
    
    for i in range(0, num_authors):
        try:
            if authorIdList[i] != "NOT FOUND!":
                authorURL = scopusAuthor + authorIdList[i]
                driver.get(authorURL)
                
                #click citation view element and wait
                wait = WebDriverWait(driver, 20)
                viewCitation = wait.until(EC.element_to_be_clickable((By.ID, 'authViewCitOver')))
                viewCitation.click()
                #driver.find_element_by_id('authViewCitOver').click()
                
                #set the first date range box to be 2001
                startYearButton = driver.find_element_by_id('startYear-button')
                startYearButton.send_keys("2")
                endYearButton = driver.find_element_by_id('endYear-button')
                
                years = start_date
                while (years != 0):
                    startYearButton.send_keys(Keys.ARROW_DOWN)
                    years = years - 1
                
                years = end_date
                while (years != 0):
                    endYearButton.send_keys(Keys.ARROW_DOWN)
                    years = years - 1
                
                #clicks update
                wait = WebDriverWait(driver, 20)
                update = wait.until(EC.element_to_be_clickable((By.ID, 'updateOverviewButtonOn')))
                update.click()
                
                #goes to export url
                time.sleep(10)
                driver.refresh()
                time.sleep(10)
                dlLink = driver.find_element_by_id('CTOExport')
                print(dlLink)
                newLink = dlLink.get_attribute("href")
                print(newLink)
                driver.get(newLink)
                print(newLink)
            else:
                print("NOT FOUND! Next in line!")
                continue
        except:
            continue
    
    print("H-INDEX SCRAPING COMPLETE")
    time.sleep(30)
    driver.close()
    excel_parser.rename(rename_dir)

