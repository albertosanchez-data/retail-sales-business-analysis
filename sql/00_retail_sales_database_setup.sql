/*
PROJECT: Retail Sales Business Analysis
DATABASE: RetailSalesAnalysis
PURPOSE: Recreate the database staging table and analytical views.

EXECUTION ORDER:
1. Create staging table.
2. Import source CSV data.
3. Create data quality views.
4. Create delivered sales view.
*/


-- =====================================================
-- 01. CREATE STAGING TABLE
-- =====================================================

CREATE TABLE public.stg_retail_sales (
    order_id VARCHAR(30),
    order_date DATE,
    customer_id VARCHAR(30),
    customer_name VARCHAR(150),
    city VARCHAR(100),
    region VARCHAR(100),
    salesperson VARCHAR(100),
    product_id VARCHAR(30),
    product_name VARCHAR(150),
    category VARCHAR(100),
    quantity INTEGER,
    unit_price_mxn NUMERIC(14,2),
    unit_cost_mxn NUMERIC(14,2),
    discount_rate NUMERIC(8,4),
    payment_method VARCHAR(50),
    sales_channel VARCHAR(50),
    order_status VARCHAR(50),
    net_sales_mxn NUMERIC(14,2),
    total_cost_mxn NUMERIC(14,2),
    gross_profit_mxn NUMERIC(14,2),
    gross_margin_pct NUMERIC(10,4),
    discount_amount_mxn NUMERIC(14,2),
    gross_sales_mxn NUMERIC(14,2),
    sales_reconciliation_check VARCHAR(50),
    profitability_status VARCHAR(50)
);