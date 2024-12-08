-- import database table dump
SELECT city, avg(value) as avg_temp FROM temperatures GROUP BY state ORDER BY city;