INSERT INTO std.cast_information(
	cast_name
)		

SELECT 
	REPLACE(UNNEST(STRING_TO_ARRAY(the_cast, ',')), '"', '') AS cast_name
     
FROM std.movies;
	
