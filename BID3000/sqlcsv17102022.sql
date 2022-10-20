USE coffeemerchant_dw;

SELECT 
dim_time.year,dim_time.quarter,dim_time.monthno, dim_time.monthname, dim_time.dato,
dim_inventory.itemType,dim_inventory.Name,
dim_customer.state,dim_customer.city,
fact_stage_order.quantity, fact_stage_order.actual_price,fact_stage_order.actual_sold
FROM fact_stage_order,dim_inventory,dim_customer,dim_time
WHERE fact_stage_order.time_sk = dim_time.time_sk 
AND fact_stage_order.inventory_sk = dim_inventory.inventory_sk
AND fact_stage_order.consumer_sk = dim_customer.customer_sk
INTO OUTFILE ' C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\sales_output.csv '
FIELDS ENCLOSED BY '"' TERMINATED BY ',' ESCAPED BY '"'
LINES TERMINATED BY '\r\n';
