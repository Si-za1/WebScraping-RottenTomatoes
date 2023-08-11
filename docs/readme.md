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
            git clone https://github.com/Si-za1/WebScraping-RottenTomatoes.git

##### Navigate to the project directory:

- bash
    
        Copy code
            cd rotten-tomatoes-scraper

##### Install the required dependencies:

- bash
        
        Copy code
            python -m env [your folder path for virtual env\venv]
            pip install beautifulsoup4
            pip install requests
            pip install lxml
            pip install dotenv 
            pip install pyscopg2



#### Usage
   
     Run the scraper.py script to start the entire pipeline for the scraping of movie information from Rotten tomatoes, then load into the Raw Table and also to the Std table
     

##### Rotten Tomatoes  
    The things scraped here are

        - Movie name 
        - Cast 
        - Release Year
        - Rating


### Project Structure
- bash
        
        Copy code

        rotten-tomatoes-scraper/
        │
        ├── docs
            Readme.md               # document related to the project
        ├── schema
            -- raw                  #  DDL for raw
                -- 001_create.sql
            --std                   # DDL for std
                -- 001_create.sql
        ├── src                   #all the folders related to the project
            --database
                -- __init__.py
                -- connection.py      #connection with the database
                -- query.py           #for running the queries
            -- scraping
                --__init__.py
                -- scraping.py        #code for scraping the site
            -- sql 
                -- raw              #dml for the raw tables
                    -- 001_insert.sql
                -- std              #dml for the std tables
                    -- 001_insert.sql
                --constants.py   #path for all the files
                -- utilis.py     #for reading the file paths
        └── .gitignore           # Git ignore file
        -- scraper.py           #for running the ETL

### Project completion schedule 

    Day 01
     Research on the beautifulSoup, requests, and web scraping
    
    Day 02
        Worked on scraping the page, scraping all the details that I need, as well as worked on how to work with the Html tags and inspection tools
    
    Day 03 
        Worked on database connection with PgAdmin4 using postgres, and worked on loading all the raw data into the raw schema
    
    Day 04
        Worked on cleaning of the raw data, and sending it to the standard table

    Day 05
        Final touchup and wrapping up 

Links to the documentation I followed:
[official documentation](https://pypi.org/project/beautifulsoup4/), 
[Geeks for Geeks](https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/), [Real Python](https://realpython.com/beautiful-soup-web-scraper-python/#:~:text=Beautiful%20Soup%20is%20a%20Python,web%20page%20using%20developer%20tools.)

Site used for scraping: [Rotten Tomatoes](https://www.rottentomatoes.com/search?search=anime)

**Note: This project is done for learning purpose!**







