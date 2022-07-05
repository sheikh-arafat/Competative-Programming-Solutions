/*
--1st Solve
SELECT DISTINCT CITY
FROM STATION
WHERE (SUBSTRING(CITY, 1, 1) IN ('a','e','i','o','u')) 
AND (SUBSTRING(CITY, -1, 1) IN ('a','e','i','o','u'));
--2nd Solve(Alternative)
*/
SELECT DISTINCT CITY
FROM STATION
WHERE LEFT(CITY, 1) IN ('a','e','i','o','u')
AND RIGHT(CITY, 1) IN ('a','e','i','o','u');
