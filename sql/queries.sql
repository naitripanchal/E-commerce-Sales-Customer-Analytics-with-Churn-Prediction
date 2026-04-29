 SELECT 
   ...>     order_status, 
   ...>     COUNT(*) as count
   ...> FROM orders
   ...> WHERE order_approved_at IS NULL 
   ...>    OR order_delivered_customer_date IS NULL
   ...> GROUP BY order_status;
sqlite> 
sqlite> 
sqlite> SELECT 
   ...>     customer_unique_id,
   ...>     MAX(order_purchase_timestamp) as last_purchase,
   ...>     julianday('2018-09-03') - julianday(MAX(order_purchase_timestamp)) as days_since_last_order
   ...> FROM orders o
   ...> JOIN customers c ON o.customer_id = c.customer_id
   ...> GROUP BY customer_unique_id
   ...> ORDER BY days_since_last_order ASC
   ...> LIMIT 10; 


#QUERY2
Query: Total Revenue by Customer (Monetary Value)
sqlite> 
sqlite> SELECT 
   ...>     c.customer_unique_id,
   ...>     ROUND(SUM(p.payment_value), 2) as total_spent
   ...> FROM customers c
   ...> JOIN orders o ON c.customer_id = o.customer_id
   ...> JOIN payments p ON o.order_id = p.order_id
   ...> WHERE o.order_status = 'delivered'
   ...> GROUP BY c.customer_unique_id
   ...> ORDER BY total_spent DESC
   ...> LIMIT 10;


