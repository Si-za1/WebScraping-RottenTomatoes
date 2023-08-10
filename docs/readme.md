# Web Scraping Project: Rotten Tomatoes Scraper
### This project is a web scraping application written in Python using the BeautifulSoup library to extract movie information from Rotten Tomatoes, and the ETL pipeline is made to load the data to the pgAdmin4 via postgres. 

## Table of Contents
- Overview
- Installation
- Usage
- Project Structure
- Project completion schedule

#### Overview
    This project is focused on scraping movie information from Rotten Tomatoes using Python and BeautifulSoup. It extracts details like movie titles, ratings, reviews, and other relevant data for further analysis.

#### Installation
    Clone this repository to your local machine using:

- bash
        
            Copy code
            git clone https://github.com/your-username/rotten-tomatoes-scraper.git

##### Navigate to the project directory:

- bash
    
        Copy code
            cd rotten-tomatoes-scraper

##### Install the required dependencies:

- bash
        
        Copy code
            pip install beautifulsoup4
            pip install requests
            pip install lxml


#### Usage
   
     Run the scraper.py script to start scraping movie information from 
     

##### Rotten Tomatoes  
    The things scraped here are

        - Movie name 
        - Cast 
        - Genre 
        - Rating

- bash
    
    Copy code
            
            python scraper.py: The scraped data will be saved to a CSV file named movies.csv in the project directory.

### Project Structure
- bash
        
        Copy code

        rotten-tomatoes-scraper/
        │
        ├── scraper.py           # Main Python script for web scraping
        ├── requirements.txt     # List of project dependencies
        ├── README.md            # Project documentation (you are here)
        └── .gitignore           # Git ignore file

### Project completion schedule 

    Day 01
     Research on the beautifulSoup, requests, and web scraping
    
    Day 02
        Worked on scraping the page, scraping all the details that I need, as well as worked on how to work with the Html tags and inspection tools
    
    Day 03 
        Worked on databse connection with PgAdmin4 using postgres, and worked on loading all the raw data into the raw schema
    
    Day 04
        Worked on cleaning of the raw data, and sending it to the standard table

    Day 05
        Final touchup and wrapping up 

Links to the documentation I followed:
[official documentation](https://pypi.org/project/beautifulsoup4/), 
[Geeks for Geeks](https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/), [Real Python](https://realpython.com/beautiful-soup-web-scraper-python/#:~:text=Beautiful%20Soup%20is%20a%20Python,web%20page%20using%20developer%20tools.)

Site used for scraping: [Rotten Tomatoes](https://www.rottentomatoes.com/search?search=anime)

**Note: This project is done for learning purpose!**







