CREATE SCHEMA IF NOT EXISTS raw;


CREATE TABLE IF NOT EXISTS raw.movies (
    title VARCHAR(255),
    rating VARCHAR(255),
    release_year VARCHAR(255),
    the_cast VARCHAR(255)
);
