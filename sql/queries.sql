 SELECT 
   ...>     order_status, 
   ...>     COUNT(*) as count
   ...> FROM orders
   ...> WHERE order_approved_at IS NULL 
   ...>    OR order_delivered_customer_date IS NULL
   ...> GROUP BY order_status;
sqlite> -- Query: Calculating Days Since Last Purchase (Recency)
sqlite> -- Why: This is the #1 predictor for Churn.
sqlite> SELECT 
   ...>     customer_unique_id,
   ...>     MAX(order_purchase_timestamp) as last_purchase,
   ...>     julianday('2018-09-03') - julianday(MAX(order_purchase_timestamp)) as days_since_last_order
   ...> FROM orders o
   ...> JOIN customers c ON o.customer_id = c.customer_id
   ...> GROUP BY customer_unique_id
   ...> ORDER BY days_since_last_order ASC
   ...> LIMIT 10; 
87ab9fec999db8bd5774917de3cdf01c|2018-10-17 17:30:18|-44.7293750001118
262e1f1e26e92e86375f86840b4ffd63|2018-10-16 20:16:02|-43.8444675924256
af5454198a97379394cacf676e1e96cb|2018-10-03 18:55:29|-30.7885300926864
634420a0ea42302205032ed44ac7fccc|2018-10-01 15:30:09|-28.6459375000559
9bb92bebd4cb7511e1a02d5e50bc4655|2018-09-29 09:13:03|-26.3840625002049
ba84da8c159659f116329563a0a981dd|2018-09-26 08:40:15|-23.3612847221084
9c3af16efacb7aa06aa3bc674556c5d6|2018-09-25 11:59:18|-22.4995138887316
08642cd329066fe11ec63293f714f2f8|2018-09-20 13:54:16|-17.5793518517166
ef0103e9602d12594d19c2b666219bc1|2018-09-17 17:21:16|-14.723101851996
c1ee153508c6b785b491443a95ff364e|2018-09-13 09:56:12|-10.4140277779661
sqlite> 

#QUERY2
Query: Total Revenue by Customer (Monetary Value)
sqlite> -- Why: Identifies our highest-value users.
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
0a0a92112bd4c708ca5fde585afaa872|13664.08
da122df9eeddfedc1dc1f5349a1a690c|7571.63
763c8b1c9c68a0229c42c9fc6f662b93|7274.88
dc4802a71eae9be1dd28f5d788ceb526|6929.31
459bef486812aa25204be022145caa62|6922.21
ff4159b92c40ebe40454e3e6a7c35ed6|6726.66
4007669dec559734d6f53e029e360987|6081.54


