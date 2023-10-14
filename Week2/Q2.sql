SELECT COUNT(*) AS total_completed_orders
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
WHERE orders.order_date = '2023-03-18'
  AND customers.first_name = 'John'
  AND customers.last_name = 'Doe';