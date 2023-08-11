-- -- now making a table which has unnested cast names 

CREATE TABLE IF NOT EXISTS std.cast_information(
	cast_id SERIAL PRIMARY KEY,
	cast_name VARCHAR
);
