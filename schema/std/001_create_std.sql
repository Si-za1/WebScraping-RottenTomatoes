CREATE SCHEMA IF NOT EXISTS std;

DROP TABLE IF EXISTS std.movies CASCADE;

CREATE TABLE IF NOT EXISTS std.movies(
	movie_id SERIAL PRIMARY KEY,
	title VARCHAR(255),
    rating INT,
    release_year INT,
    the_cast VARCHAR(255)   
);



