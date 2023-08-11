INSERT INTO std.movie_information(
	title,
	rating,
	release_year
)

SELECT
	title,
	rating,
	release_year
	
FROM std.movies;

