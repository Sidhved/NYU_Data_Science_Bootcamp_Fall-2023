SELECT d.department_id, d.department_name
FROM departments d
JOIN sales s ON d.department_id = s.department_id
WHERE s.year = 2022
GROUP BY d.department_id, d.department_name
HAVING SUM(s.revenue) < 600;
