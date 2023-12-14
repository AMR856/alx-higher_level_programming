-- This stuff is weird but let's hang on
CREATE TABLE IF NOT EXISTS unique_id(
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);