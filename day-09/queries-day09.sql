
-- join query-1

SELECT
    e.ID,
    e.NAME,
    d.department_name
FROM employees e
JOIN departments d
ON e.department_id = d.department_id;

-- join query-2

SELECT
    p.project_name,
    e.NAME
FROM projects p
JOIN employees e
ON p.employee_id = e.ID;

-- join query-3

SELECT
    e.NAME,
    d.department_name,
    p.project_name
FROM employees e
JOIN departments d
ON e.department_id = d.department_id
JOIN projects p
ON e.ID = p.employee_id;

--update query 
--Give every employee a ₹5,000 raise.

UPDATE employees
SET SALARY = SALARY + 5000;

-- delete query

DELETE FROM employees
WHERE NAME = 'Test User';

-- total employees in each dept

SELECT
    d.department_name,
    COUNT(e.ID) AS Total_Employees
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id
GROUP BY d.department_name;