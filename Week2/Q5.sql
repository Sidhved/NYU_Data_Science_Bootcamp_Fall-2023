-- Most revenue
SELECT *
FROM orders
ORDER BY revenue DESC
LIMIT 1;

-- Least revenue
SELECT *
FROM orders
ORDER BY revenue ASC
LIMIT 1;