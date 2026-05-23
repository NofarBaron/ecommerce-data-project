--create dim_users 
CREATE OR REPLACE TABLE `my-project-284-493514.ecommerce_data.dim_users` AS
SELECT
  customer_id,
  MIN(event_time) AS first_seen,
  COUNT(*) AS total_events
FROM `my-project-284-493514.ecommerce_data.fact_events`
GROUP BY customer_id;

CREATE OR REPLACE TABLE `my-project-284-493514.ecommerce_data.dim_users` AS
SELECT
  u.* except(is_payer), 
  IF(o.customer_id IS NOT NULL, true, false) AS is_payer,
  o.* except(customer_id),
FROM `my-project-284-493514.ecommerce_data.dim_users` u 
left join(
    SELECT
    customer_id,
    SUM(order_amount) AS total_spent,
    COUNT(*) AS total_orders,
    sum(case when lower(status)='success' then 1 else 0 end) as success_orders,
    sum(case when lower(status)='failed' then 1 else 0 end) as failed_orders,
    sum(case when lower(status)='refunded' then 1 else 0 end) as refunded_orders,
  FROM `my-project-284-493514.ecommerce_data.orders` 
  GROUP BY customer_id) o
using(customer_id)
;


