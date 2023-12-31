-- Insert data into the lookup table
INSERT INTO std.lookup_table (movie_id, cast_id)
SELECT 
    m.movie_id,
    ci.cast_id
FROM std.movies m
CROSS JOIN LATERAL UNNEST(STRING_TO_ARRAY(m.the_cast, ',')) AS cast_name_array(cast_name)
JOIN std.cast_information ci 
	ON ci.cast_name = cast_name_array.cast_name;