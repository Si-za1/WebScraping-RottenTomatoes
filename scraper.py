import os
from src.utils import ls, read_file
from src.database.query import execute_query_from_file
from src.database.connection import get_connection
from src.constants import RAW_SCHEMA_PATH, STD_SCHEMA_PATH, INSERT_DATA_PATH, INSERT_STD_DATA_PATH
from src.scraping.scraping import scrape_rotten_tomatoes

if __name__ == '__main__':
    # # CONNECTION ESTABLISH
    conn, cur = get_connection()
    

    # # WORKING WITH RAW SCHEMA
    files = ls(RAW_SCHEMA_PATH)
    for file in files:
        file_path = os.path.join(RAW_SCHEMA_PATH, file)
        query = read_file(file_path)
        execute_query_from_file(conn, cur, query)
    breakpoint()

    # # WORKING WITH INSERT DATA
    files = ls(INSERT_DATA_PATH)
    for file in files:
        file_path = os.path.join(INSERT_DATA_PATH, file)
        query = read_file(file_path)
    breakpoint()
    
    # Execute scraping for each genre
    genre_name = ["anime", "action", "comedy" ]
    for genre in genre_name:
        movies = scrape_rotten_tomatoes(genre)
        print(f"Movies in {genre} genre:")
        for movie in movies:
            print("title:", movie[0], "rating:", movie[1], "year:", movie[2])
            print("cast:", movie[3])
            title, rating, year, cast = movie 
            data = (title, rating, year, cast)
            
            # Use parameterized query
            cur.execute(query, data)
            conn.commit()

    # WORKING WITH STD SCHEMA
    files = ls(STD_SCHEMA_PATH)
    for file in files:
        file_path = os.path.join(STD_SCHEMA_PATH, file)
        query = read_file(file_path)
        execute_query_from_file(conn, cur, query)
    breakpoint()
        
   
    # WORKING WITH INSERT DATA FOR STD
    files = ls(INSERT_STD_DATA_PATH)
    for file in files:
            file_path = os.path.join(INSERT_STD_DATA_PATH, file)
            query = read_file(file_path)
            execute_query_from_file(conn, cur, query)
            conn.commit()

    conn.close()


    