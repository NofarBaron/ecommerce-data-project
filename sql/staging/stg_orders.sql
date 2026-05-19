
CREATE OR REPLACE TABLE `my-project-284-493514.ecommerce_data.orders_new` AS
SELECT
  order_id,customer_id,product_id,order_amount,
  coalesce(SAFE_CAST(order_date AS TIMESTAMP),SAFE.PARSE_TIMESTAMP('%Y-%m-%d %H:%M:%S', order_date)) AS order_time,
  payment_method,lower(status) as status,quantity 
FROM `my-project-284-493514.ecommerce_data.orders`
WHERE order_id IS NOT NULL
and order_date is not null 
and not is_nan(order_amount) 
;