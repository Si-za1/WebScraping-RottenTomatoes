from bs4 import BeautifulSoup
import requests


genre_name = ["anime", "action", "comedy"]

genre_urls = {
        genre: f"https://www.rottentomatoes.com/search?search={genre}"
        for genre in genre_name            
    }

def scrape_rotten_tomatoes(genre):
   
    if genre not in genre_urls:
        print("Genre not found!")
        return []

    url = genre_urls[genre]
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    doc = BeautifulSoup(response.text, "html.parser")
    all_movies = []

    movies = doc.find(id='search-results').\
        find('search-page-result', {'type': 'movie'}).\
        find('ul', {'slot': 'list'}).\
        find_all('search-page-media-row')
    

    for movie in movies:
        title_elem = movie.find("a", class_="unset", slot="title").text.strip()
        rating_elem = movie["tomatometerscore"]
        year_elem = movie["releaseyear"]
        cast_elem = movie["cast"].split(",")
        all_movies.append(( title_elem, rating_elem, year_elem, cast_elem))

        # # Print movie details for each movie
        # print("Scraped movie:", "title:", title_elem, "rating:", rating_elem, "year:", year_elem, "cast:", cast_elem)

    return all_movies

# if __name__ == '__main__':
   
#    for genre in genre_name:
#         movies = scrape_rotten_tomatoes(genre)
#         print(f"Movies in {genre} genre:")
#         for movie in movies:
#             print("title:", movie[0], "rating:", movie[1], "year:", movie[2]) #movie[0]== title, movie[1] == rating
#             print("cast:", movie[3])

#         print("\n")

