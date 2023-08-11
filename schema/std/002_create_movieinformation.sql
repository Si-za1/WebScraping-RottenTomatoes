-- now making a table without the cast information 

CREATE TABLE IF NOT EXISTS std.movie_information(
	movie_id SERIAL PRIMARY KEY,
	title VARCHAR,
	rating INT,
	release_year INT
);