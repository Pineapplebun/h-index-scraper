import multiprocessing as mp
from tkinter import filedialog as fd
import id_scraper2
import excel_parser

def run_id_scraper(param):
    """ (str) -> None 
    
    Precondition: param must be the folder directory of an excel file called authorId
    whose first column is blank, second column is their last name, third column is
    their first name, and fourth column is their university.
    
    Runs the scraping method from id_scraper2.py
    
    >>> run_id_scraper("C:\")
    
    """
    
    id_scraper2.scrape_id(param)

def scrape_folder(folders):
    """ (List) -> None
    
    Runs the multiprocessing methods using elements from folders as parameters.

    >>> scrape_folder["C:\"])
    
    """
    parameters = folders
    
    pool = mp.Pool(len(parameters))
    pool.map(run_id_scraper, parameters)
    print("Scraping complete")

if __name__ == "__main__":
    #scrape_id takes a folder name

    file_dir = []
    n = int(input("How many universities to scrape from? (Enter an integer)"))
    for i in range(1, n + 1):
        file_dir.append(fd.askdirectory())    
    
    parameters = file_dir
    
    scrape_folder(parameters)





    

