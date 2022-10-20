USE COFFEEMERCHANT_DW;

# Rank the items by ascending item price
SELECT NAME,PRICE,itemType,
DENSE_RANK() OVER(ORDER BY price) as 'RankItem'
FROM dim_inventory;

# Rank the customers by sales
SELECT FirstName, SUM(actual_sold) as sum_sold,
DENSE_RANK() OVER (ORDER BY SUM(actual_sold) DESC)
AS 'RankItem'
FROM dim_customer s, fact_stage_order f
WHERE s.customer_sk = f.consumer_sk
GROUP BY FirstName;


SELECT name, AVG(actual_sold) AS AvgSales,COUNT(*) AS RowCount,
RANK() OVER (ORDER BY(actual_sold) DESC) AS 'AvgSalesRank'
FROM dim_inventory i, fact_stage_order f, dim_time t
WHERE i.inventory_sk = f.inventory_sk AND f.time_sk = t.time_sk
AND t.monthno >= 01 AND t.monthno <= 03
GROUP BY name
HAVING COUNT(*) >= 5;


SELECT state, firstname, SUM(actual_sold) AS SumSales,
DENSE_RANK() OVER (PARTITION BY state 
	ORDER BY SUM(actual_sold) DESC) AS 'SalesRank'
FROM dim_customer c, fact_stage_order s
WHERE c.customer_sk = s.consumer_sk
GROUP BY state,firstname
ORDER BY state;


SELECT zipcode, SUM(quantity) AS SumSalesUnit,
RANK() OVER(ORDER BY SUM(quantity) DESC) AS SURank,
DENSE_RANK() OVER(ORDER BY SUM(quantity) DESC) AS SUDenseRankUnit,
NTILE(4) OVER (ORDER BY SUM(quantity) DESC) AS SUNTILERank,
ROW_NUMBER() OVER (ORDER BY SUM(quantity) DESC) AS SURowNumRank
FROM dim_customers c, fact_stage_order f
WHERE c.customer_sk = f.consumer_sk
GROUP BY zipcode;


SELECT name,year,COUNT(*) AS rowcount,
RANK() OVER (PARTITION BY year
	ORDER BY COUNT(*) DESC) AS RankRowCount,
DENSE_RANK() OVER (PARTITION BY year,
	ORDER BY COUNT(*) DESC) AS DRankRowCount
FROM dim_inventory i, fact_stage_order f, dim_time t
WHERE f.inventory_sk = i.inventory_sk
AND f.time_sk = t.time_sk
GROUP BY name,year
HAVING COUNT(*) > 5;