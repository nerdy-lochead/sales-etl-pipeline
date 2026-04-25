-- Total revenue
SELECT SUM(total_price) AS total_revenue FROM sales;

-- Revenue by product
SELECT product, SUM(total_price) AS revenue
FROM sales
GROUP BY product;

-- Top customers
SELECT customer_name, SUM(total_price) AS total_spent
FROM sales
GROUP BY customer_name
ORDER BY total_spent DESC;