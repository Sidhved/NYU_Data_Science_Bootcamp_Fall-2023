SELECT COUNT(DISTINCT customer_id) AS total_customers,
       AVG(amount) AS average_amount_per_customer
FROM orders
WHERE order_date BETWEEN '2023-01-01' AND '2023-01-31';
