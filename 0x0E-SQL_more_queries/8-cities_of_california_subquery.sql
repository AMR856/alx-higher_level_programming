-- All I am is a man I want the world in my hands
-- I hate the beach but I stand in CALIFORNIA with my toes in the sand
SELECT id, name FROM cities
WHERE state_id = (
    SELECT id FROM states
    WHERE name = 'California'
);
