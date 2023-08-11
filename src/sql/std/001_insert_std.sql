INSERT INTO std.movies(
	title,
	rating,
	release_year,
	the_cast
)

SELECT 
    title::VARCHAR AS movie_name,
    CASE WHEN rating = '' THEN 0 ELSE rating::INT END AS movie_rating,
    release_year::INT  AS release_year,
    replace(unnest(string_to_array(replace(replace(the_cast, '{', ''), '}', ''), ',')), '"', '')::VARCHAR AS cast_name

FROM raw.movies;
