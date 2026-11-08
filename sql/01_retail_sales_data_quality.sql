/*
PROJECT: Retail Sales Business Analysis
PURPOSE: Data quality validation and anomaly detection.
DATABASE: RetailSalesAnalysis

SOURCE TABLE: public.stg_retail_sales
QUALITY VIEW: public.vw_retail_sales_quality
SUMMARY VIEW: public.vw_retail_sales_quality_summary
*/


-- =====================================================
-- 01. DATASET OVERVIEW
-- =====================================================

SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT order_id) AS distinct_orders,
    MIN(order_date) AS first_order_date,
    MAX(order_date) AS last_order_date,
    COUNT(*) FILTER (
        WHERE order_id IS NULL
    ) AS null_order_ids
FROM public.stg_retail_sales;


-- =====================================================
-- 02. BASIC DATA QUALITY CHECKS
-- =====================================================

SELECT
    COUNT(*) FILTER (
        WHERE customer_id IS NULL
    ) AS null_customer_ids,

    COUNT(*) FILTER (
        WHERE product_id IS NULL
    ) AS null_product_ids,

    COUNT(*) FILTER (
        WHERE quantity IS NULL OR quantity <= 0
    ) AS invalid_quantities,

    COUNT(*) FILTER (
        WHERE unit_price_mxn IS NULL OR unit_price_mxn < 0
    ) AS invalid_prices,

    COUNT(*) FILTER (
        WHERE unit_cost_mxn IS NULL OR unit_cost_mxn < 0
    ) AS invalid_costs,

    COUNT(*) FILTER (
        WHERE discount_rate IS NULL
           OR discount_rate < 0
           OR discount_rate > 1
    ) AS invalid_discounts,

    COUNT(*) FILTER (
        WHERE net_sales_mxn IS NULL
    ) AS null_net_sales,

    COUNT(*) FILTER (
        WHERE gross_profit_mxn IS NULL
    ) AS null_gross_profit

FROM public.stg_retail_sales;


-- =====================================================
-- 03. IDENTIFY ANOMALOUS RECORDS
-- =====================================================

SELECT
    order_id,
    order_date,
    product_name,
    quantity,
    discount_rate,
    net_sales_mxn,
    gross_profit_mxn
FROM public.stg_retail_sales
WHERE quantity IS NULL
   OR quantity <= 0
   OR discount_rate IS NULL
   OR discount_rate < 0
   OR discount_rate > 1
   OR net_sales_mxn IS NULL
   OR net_sales_mxn < 0;


-- =====================================================
-- 04. DATA QUALITY SUMMARY
-- =====================================================

SELECT
    COUNT(*) AS total_records,

    COUNT(*) FILTER (
        WHERE data_quality_status = 'VALID'
    ) AS valid_records,

    COUNT(*) FILTER (
        WHERE data_quality_status = 'ANOMALY'
    ) AS anomaly_records,

    ROUND(
        COUNT(*) FILTER (
            WHERE data_quality_status = 'VALID'
        ) * 100.0 / NULLIF(COUNT(*), 0),
        2
    ) AS data_quality_pct

FROM public.vw_retail_sales_quality;


-- =====================================================
-- 05. ANOMALY DETAILS
-- =====================================================

SELECT
    order_id,
    quantity,
    discount_rate,
    net_sales_mxn,
    data_quality_status,
    data_quality_issues
FROM public.vw_retail_sales_quality
WHERE data_quality_status = 'ANOMALY';


-- =====================================================
-- 06. DATA QUALITY SUMMARY VIEW
-- =====================================================

SELECT *
FROM public.vw_retail_sales_quality_summary;


-- =====================================================
-- 07. ORDER STATUS DISTRIBUTION
-- =====================================================

SELECT
    order_status,
    COUNT(*) AS total_orders,
    ROUND(SUM(net_sales_mxn), 2) AS net_sales,
    ROUND(SUM(gross_profit_mxn), 2) AS gross_profit
FROM public.vw_retail_sales_quality
GROUP BY order_status
ORDER BY total_orders DESC;