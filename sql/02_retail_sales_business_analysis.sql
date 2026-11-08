/*
PROJECT: Retail Sales Business Analysis
PURPOSE: Analyze delivered retail sales, profitability,
         product performance, regional performance,
         sales channels, employees and customers.

DATABASE: RetailSalesAnalysis
SOURCE VIEW: public.vw_retail_sales_delivered

BUSINESS RULE:
Only records classified as VALID and with order_status
equal to ENTREGADO are included.
*/


-- =====================================================
-- 01. GENERAL SALES KPIs
-- =====================================================

SELECT
    COUNT(*) AS delivered_orders,
    SUM(quantity) AS units_delivered,
    ROUND(SUM(gross_sales_mxn), 2) AS gross_sales,
    ROUND(SUM(discount_amount_mxn), 2) AS total_discounts,
    ROUND(SUM(net_sales_mxn), 2) AS net_sales,
    ROUND(SUM(total_cost_mxn), 2) AS total_cost,
    ROUND(SUM(gross_profit_mxn), 2) AS gross_profit,
    ROUND(
        SUM(gross_profit_mxn) * 100.0 /
        NULLIF(SUM(net_sales_mxn), 0),
        2
    ) AS gross_margin_pct
FROM public.vw_retail_sales_delivered;


-- =====================================================
-- 02. SALES BY CATEGORY
-- =====================================================

SELECT
    category,
    COUNT(*) AS delivered_orders,
    SUM(quantity) AS units_delivered,
    ROUND(SUM(net_sales_mxn), 2) AS net_sales,
    ROUND(SUM(gross_profit_mxn), 2) AS gross_profit,
    ROUND(
        SUM(gross_profit_mxn) * 100.0 /
        NULLIF(SUM(net_sales_mxn), 0),
        2
    ) AS gross_margin_pct
FROM public.vw_retail_sales_delivered
GROUP BY category
ORDER BY net_sales DESC;


-- =====================================================
-- 03. SALES BY REGION
-- =====================================================

SELECT
    region,
    COUNT(*) AS delivered_orders,
    SUM(quantity) AS units_delivered,
    ROUND(SUM(net_sales_mxn), 2) AS net_sales,
    ROUND(SUM(gross_profit_mxn), 2) AS gross_profit,
    ROUND(
        SUM(gross_profit_mxn) * 100.0 /
        NULLIF(SUM(net_sales_mxn), 0),
        2
    ) AS gross_margin_pct
FROM public.vw_retail_sales_delivered
GROUP BY region
ORDER BY net_sales DESC;


-- =====================================================
-- 04. MONTHLY SALES TREND
-- =====================================================

SELECT
    DATE_TRUNC('month', order_date)::DATE AS sales_month,
    COUNT(*) AS delivered_orders,
    SUM(quantity) AS units_delivered,
    ROUND(SUM(net_sales_mxn), 2) AS net_sales,
    ROUND(SUM(gross_profit_mxn), 2) AS gross_profit,
    ROUND(
        SUM(gross_profit_mxn) * 100.0 /
        NULLIF(SUM(net_sales_mxn), 0),
        2
    ) AS gross_margin_pct
FROM public.vw_retail_sales_delivered
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY sales_month;


-- =====================================================
-- 05. SALES BY CHANNEL
-- =====================================================

SELECT
    sales_channel,
    COUNT(*) AS delivered_orders,
    SUM(quantity) AS units_delivered,
    ROUND(SUM(net_sales_mxn), 2) AS net_sales,
    ROUND(SUM(gross_profit_mxn), 2) AS gross_profit,
    ROUND(
        SUM(gross_profit_mxn) * 100.0 /
        NULLIF(SUM(net_sales_mxn), 0),
        2
    ) AS gross_margin_pct
FROM public.vw_retail_sales_delivered
GROUP BY sales_channel
ORDER BY net_sales DESC;


-- =====================================================
-- 06. SALES PERFORMANCE BY SALESPERSON
-- =====================================================

SELECT
    salesperson,
    COUNT(*) AS delivered_orders,
    SUM(quantity) AS units_delivered,
    ROUND(SUM(net_sales_mxn), 2) AS net_sales,
    ROUND(SUM(gross_profit_mxn), 2) AS gross_profit,
    ROUND(
        SUM(gross_profit_mxn) * 100.0 /
        NULLIF(SUM(net_sales_mxn), 0),
        2
    ) AS gross_margin_pct,
    ROUND(
        SUM(net_sales_mxn) / NULLIF(COUNT(*), 0),
        2
    ) AS average_order_value
FROM public.vw_retail_sales_delivered
GROUP BY salesperson
ORDER BY net_sales DESC;


-- =====================================================
-- 07. PRODUCT PERFORMANCE
-- =====================================================

SELECT
    product_id,
    product_name,
    category,
    COUNT(*) AS delivered_orders,
    SUM(quantity) AS units_delivered,
    ROUND(SUM(net_sales_mxn), 2) AS net_sales,
    ROUND(SUM(gross_profit_mxn), 2) AS gross_profit,
    ROUND(
        SUM(gross_profit_mxn) * 100.0 /
        NULLIF(SUM(net_sales_mxn), 0),
        2
    ) AS gross_margin_pct
FROM public.vw_retail_sales_delivered
GROUP BY product_id, product_name, category
ORDER BY net_sales DESC;


-- =====================================================
-- 08. TOP 10 CUSTOMERS
-- =====================================================

SELECT
    customer_id,
    customer_name,
    city,
    region,
    COUNT(*) AS delivered_orders,
    SUM(quantity) AS units_delivered,
    ROUND(SUM(net_sales_mxn), 2) AS net_sales,
    ROUND(SUM(gross_profit_mxn), 2) AS gross_profit,
    ROUND(
        SUM(gross_profit_mxn) * 100.0 /
        NULLIF(SUM(net_sales_mxn), 0),
        2
    ) AS gross_margin_pct
FROM public.vw_retail_sales_delivered
GROUP BY customer_id, customer_name, city, region
ORDER BY net_sales DESC
LIMIT 10;


-- =====================================================
-- 09. CUSTOMER REPEAT RATE
-- =====================================================

WITH customer_orders AS (
    SELECT
        customer_id,
        COUNT(*) AS delivered_orders
    FROM public.vw_retail_sales_delivered
    GROUP BY customer_id
)
SELECT
    COUNT(*) AS total_customers,
    COUNT(*) FILTER (
        WHERE delivered_orders = 1
    ) AS one_time_customers,
    COUNT(*) FILTER (
        WHERE delivered_orders > 1
    ) AS repeat_customers,
    ROUND(
        COUNT(*) FILTER (
            WHERE delivered_orders > 1
        ) * 100.0 / NULLIF(COUNT(*), 0),
        2
    ) AS repeat_customer_rate,
    MAX(delivered_orders) AS max_orders_by_customer
FROM customer_orders;