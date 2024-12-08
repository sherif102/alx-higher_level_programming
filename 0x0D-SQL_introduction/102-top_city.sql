-- retrieve the top 3 cities with hot temperature from temperatures
SELECT city, avg(value) as avg_temp
FROM temperatures 
WHERE month = 'July' OR month = 'August'
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;