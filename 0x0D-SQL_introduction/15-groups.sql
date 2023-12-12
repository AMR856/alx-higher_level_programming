-- We're stornger when we work in groups
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;