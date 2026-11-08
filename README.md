# Retail Sales Business Analysis

**End-to-end retail business analysis using PostgreSQL, SQL, Python, and Power BI.**

An end-to-end data analytics project focused on evaluating retail sales performance, profitability, data quality, product performance, regional results, sales channels, and customer behavior.

The project transforms transactional data into business insights through SQL analysis, Python processing, and an executive Power BI dashboard.

---

## 1. Project Overview

This project analyzes a retail sales dataset containing **1,000 transactions from 2025**.

The analytical workflow includes:

- Database preparation and data staging.
- Data quality assessment and anomaly detection.
- SQL-based business performance analysis.
- Python data processing and analytical output generation.
- Power BI dashboard development.
- Business insights and data-driven recommendations.

The commercial performance analysis focuses on valid delivered orders to ensure that the reported sales and profitability metrics represent completed transactions.

## 2. Business KPIs

The following indicators summarize the performance of valid delivered orders.

| KPI | Result |
|---|---:|
| Delivered Orders | 577 |
| Units Sold | 1,551 |
| Gross Sales | MXN $4,546,860.00 |
| Discounts | MXN $225,180.00 |
| Net Sales | MXN $4,321,680.00 |
| Total Cost | MXN $3,141,480.00 |
| Gross Profit | MXN $1,180,200.00 |
| Gross Margin | 27.31% |

## 3. Data Quality Assessment

The original dataset was evaluated before performing the commercial analysis.

| Data Quality Metric | Result |
|---|---:|
| Total Records | 1,000 |
| Valid Records | 998 |
| Records with Anomalies | 2 |
| Data Quality Rate | 99.80% |

Two records were identified with data quality issues:

- Invalid discount rate and negative net sales.
- Invalid quantity (zero units).

The original records were preserved in the staging table. Analytical views were created to classify anomalies and exclude invalid records from commercial performance analysis.

This approach maintains data traceability while protecting the reliability of business metrics.

## 4. Power BI Executive Dashboard

The interactive dashboard provides an overview of retail performance through five KPI cards and four analytical visualizations.

### Complete Dashboard

![Retail Sales Dashboard](documentation/retail_sales_dashboard.png)

### Sales Performance Analysis

![Retail Sales Charts](documentation/retail_sales_charts.png)

### Key Performance Indicators

![Retail Sales KPIs](documentation/retail_sales_kpis.png)

### Dashboard Components

**KPI Cards**
- Net Sales
- Gross Profit
- Gross Margin
- Delivered Orders
- Units Sold

**Analytical Visualizations**
- Net Sales by Product Category
- Monthly Net Sales Trend
- Net Sales by Region
- Net Sales by Sales Channel

## 5. Key Business Insights

### 5.1 Product Category Performance

- Technology generated the highest net sales, reaching **MXN $2,791,202.50**.
- Technology also generated the highest absolute gross profit.
- Accessories achieved the highest gross margin at **48.14%**.
- Components recorded a gross margin of **34.73%**.

**Business insight:** Technology is the main sales contributor, while accessories offer an attractive profitability opportunity.

**Recommendation:** Evaluate accessory cross-selling opportunities alongside high-value technology products. Validate the opportunity through order-level product analysis.

### 5.2 Regional Performance

- Northeast led net sales with **MXN $1,485,405.00**.
- Central achieved the highest gross margin at **28.55%**.
- West recorded the lowest gross margin at **26.64%**.

**Business insight:** The region generating the highest sales is not necessarily the region achieving the highest profitability.

**Recommendation:** Investigate the product mix, pricing, and discount strategies behind the stronger gross margin in Central and the lower margin in West.

### 5.3 Monthly Sales Trends

- March recorded the highest net sales: **MXN $614,745.00**.
- September ranked second: **MXN $529,742.00**.
- January achieved the highest gross margin: **31.87%**.
- November recorded the lowest gross margin: **25.29%**.

**Business insight:** Higher sales volume does not necessarily translate into higher profitability.

**Recommendation:** Investigate November's lower margin and evaluate monthly changes in product mix, costs, and discounts.

### 5.4 Sales Channel Performance

- Physical stores generated the highest net sales: **MXN $1,607,414.50**.
- Telephone sales recorded the highest number of orders: **203**.
- Telephone sales achieved the highest gross margin: **27.54%**.
- Gross margins were relatively consistent across all three sales channels.

**Business insight:** Physical stores are the largest contributor to net sales, while telephone sales demonstrate strong order activity and profitability.

**Recommendation:** Evaluate opportunities to improve conversion and average transaction value across all channels.

### 5.5 Product Performance

- Laptop 15 pulgadas was the top product by net sales, generating **MXN $1,716,075.00**.
- It also generated the highest absolute gross profit: **MXN $387,675.00**.
- Mouse óptico achieved the highest gross margin at **58.73%**.
- Audífonos combined a **49.94% gross margin** with 165 units delivered.

**Business insight:** The product generating the highest revenue is not necessarily the product generating the highest gross margin.

**Recommendation:** Review product-level pricing, costs, and discount strategies. Evaluate opportunities to promote products with stronger margins.

### 5.6 Salesperson Performance

- Mario Castillo led net sales with **MXN $841,688.50**.
- Mario Castillo also generated the highest gross profit: **MXN $232,158.50**.
- Andrea Ruiz achieved the highest gross margin: **27.87%**.
- Andrea Ruiz handled the highest number of delivered orders: **110**.

**Business insight:** Sales volume, order activity, and profitability can identify different dimensions of individual performance.

**Recommendation:** Compare sales performance using revenue, gross profit, gross margin, and delivered orders rather than relying on revenue alone.

### 5.7 Customer Analysis

- 233 customers generated delivered sales.
- 169 customers made more than one delivered purchase.
- The customer repeat rate was **72.53%**.
- The highest number of delivered orders by one customer was 9.
- Miguel Hernández was the highest-ranked customer by delivered sales, with **MXN $116,000.00**.

**Business insight:** Repeat purchasing represents an important opportunity for customer retention and long-term value.

**Recommendation:** Analyze repeat customer behavior and identify opportunities for retention, loyalty initiatives, and customer lifetime value analysis.

## 6. Key Business Recommendations

Based on the analytical findings, the following actions are recommended:

1. **Increase accessory cross-selling:** Evaluate complementary product opportunities with high-value technology purchases.
2. **Improve margin monitoring:** Investigate the factors behind November's lower gross margin.
3. **Review pricing and discounts:** Assess their impact on laptop and technology category profitability.
4. **Benchmark regional performance:** Study the product mix and commercial practices contributing to Central's higher gross margin.
5. **Strengthen customer retention:** Analyze repeat customers and develop strategies to increase customer lifetime value.
6. **Evaluate sales channels:** Compare order volume, revenue, and profitability to identify channel-specific improvement opportunities.
7. **Monitor salesperson performance:** Use multiple profitability and productivity indicators for a balanced evaluation.

## 7. Tools and Technologies

| Technology | Application |
|---|---|
| PostgreSQL | Database management, staging, and analytical views |
| SQL | Data quality validation and business analysis |
| Python | Data import, processing, automation, and analytical outputs |
| Power BI | Executive dashboard and business intelligence |
| Excel | Supporting data review |
| GitHub | Project documentation and version control |

## 8. Project Structure

```text
retail-sales-business-analysis/
│
├── documentation/
│   ├── business_findings.md
│   ├── retail_sales_dashboard.png
│   ├── retail_sales_charts.png
│   └── retail_sales_kpis.png
│
├── outputs/
│   └── Analytical CSV outputs
│
├── python/
│   └── Python scripts
│
├── sql/
│   └── SQL scripts
│
└── Retail_Sales_Business_Analysis.pbix
```

## 9. Analytical Workflow

1. **Database preparation:** Set up the PostgreSQL database and staging structure.
2. **Data quality assessment:** Validate transactions and identify anomalies.
3. **Data preparation:** Create analytical views for valid commercial records.
4. **SQL business analysis:** Calculate KPIs and analyze products, regions, months, channels, salespeople, and customers.
5. **Python processing:** Execute data processing and generate analytical CSV outputs.
6. **Power BI visualization:** Build an executive dashboard to communicate business performance.
7. **Business recommendations:** Translate analytical findings into practical improvement opportunities.

## 10. Project Objectives and Skills Demonstrated

This project demonstrates practical capabilities in:

- SQL querying and PostgreSQL database analysis.
- Data quality assessment and anomaly detection.
- Data preparation and analytical data validation.
- Python-based data processing and automation.
- KPI development and profitability analysis.
- Exploratory and diagnostic business analysis.
- Power BI dashboard development.
- Business insight generation and data-driven recommendations.

## 11. Conclusion

The analysis identified key drivers of retail sales performance and profitability across products, categories, regions, months, sales channels, salespeople, and customers.

It also demonstrated the importance of data quality and the distinction between revenue growth and profitability.

By combining PostgreSQL, SQL, Python, and Power BI, this project illustrates an end-to-end analytical workflow that transforms transactional data into structured business intelligence and actionable recommendations.

---

**Author:** Alberto Sanchez

**GitHub:** [albertosanchez-data](https://github.com/albertosanchez-data)

**LinkedIn:** [Alberto Sanchez](https://www.linkedin.com/in/alberto-sanchez-data/)
