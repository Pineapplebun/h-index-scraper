Note: some experimentation is required in order to find the correct number of clicks...
If the structure of the Scopus has changed, this web scraper may not work.

Instructions:

1. Before you run the process_all.py, make sure you have an authorId.xlsx file whose first column is blank 
(which will be filled in by the script), second column is the last name, third column is the first name, 
fourth column is the university affiliation. Each university should have their own folder and authorId.xlsx file. 
You will select these folders in the dialog box that opens when you run the script. 

2. To determine the range of years (e.g. 2010 - 2016) that you want to download files from, there is currently no other way but to experiment with the "Citation Overview" page where you export the author's contributions. Go to any citation overview page and check
how many "up" arrow clicks is needed to select the upper bound of your citation year range and "down" clicks for the lower bound. 

    a. Enter the number of clicks to get to the starting date in the variable <start_date>
    b. Enter the number of clicks to get to the end date in the variable <end date>

3. Finding scopus author id is NOT 100% GUARANTEED. The algorithm only takes THE FIRST RESULT of any search. Therefore, if there are
multiple results, you should check to make sure that you have the right person. To help with this, the script also marks in the fifth
column whether or not there were multiple results in the search for scopus author ids. ALWAYS CHECK TO MAKE SURE.

Running the script:

1. Go to hindexscraper2.py in the scrape_index function local variables and input 
the number of clicks in the start_date and end_date variables.
2. Run process_all.py
3. Enter the number of universities you want to scrape
4. In the dialog box, select the folder(s) where authorId.xlsx is located
5. Wait.
6. When "Scraping Complete" is printed, you should find your files in their corresponding folders.

