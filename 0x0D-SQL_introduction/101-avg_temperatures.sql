-- I'm using some more things now
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;