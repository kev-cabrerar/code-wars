SELECT d.id, d.name
FROM departments d
WHERE id IN (SELECT s1.department_id FROM sales s1 WHERE (s1.price) > 98.00);