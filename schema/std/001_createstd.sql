-- CREATE SCHEMA IF NOT EXISTS std;

-- DROP TABLE IF EXISTS std.movies CASCADE;

CREATE TABLE IF NOT EXISTS std.movies(
	movie_id SERIAL PRIMARY KEY,
	title VARCHAR(255),
    rating INT,
    release_year INT,
    the_cast VARCHAR(255)
    
);

-- now making a table without the cast information 

CREATE TABLE IF NOT EXISTS std.movie_information(
	movie_id SERIAL PRIMARY KEY,
	title VARCHAR,
	rating INT,
	release_year INT
	
);

-- -- now making a table which has unnested cast names 


CREATE TABLE IF NOT EXISTS std.cast_information(
	cast_id SERIAL PRIMARY KEY,
	cast_name VARCHAR
);

-- Drop and recreate the lookup table

CREATE TABLE IF NOT EXISTS std.lookup_table (
    movie_id INTEGER REFERENCES std.movies(movie_id),
    cast_id INTEGER REFERENCES std.cast_information(cast_id),
    PRIMARY KEY (movie_id, cast_id)
);

