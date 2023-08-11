-- Drop and recreate the lookup table

CREATE TABLE IF NOT EXISTS std.lookup_table (
    movie_id INTEGER REFERENCES std.movies(movie_id),
    cast_id INTEGER REFERENCES std.cast_information(cast_id),
    PRIMARY KEY (movie_id, cast_id)
);

