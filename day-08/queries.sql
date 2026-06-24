--query-1 

SELECT * 
FROM employees;

--query-2

SELECT *
FROM employees
WHERE department = 'IT';

-- query-3

SELECT *
FROM employees
ORDER BY salary DESC;

-- query-4

SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department;

-- query-5

SELECT *
FROM employees
WHERE salary > 100000;