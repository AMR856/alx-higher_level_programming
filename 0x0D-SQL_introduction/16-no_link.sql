-- Now I'm just repeating myself but with ground values
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;