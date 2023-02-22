-- a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)
-- a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city,AVG(value) as avg_temp FROM tempratures
WHERE month = 7 OR month = 8
GROUP BY city 
ORDER BY avg_temp DESC LIMIT 3;
