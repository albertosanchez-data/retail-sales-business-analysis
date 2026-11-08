# Retail Sales Business Analysis

## Business Findings and Insights

### 1. Project Overview

This project analyzes a retail sales dataset containing 1,000 transactions from 2025.

The analysis uses PostgreSQL to perform data quality validation, identify anomalies, evaluate sales performance, and generate business insights.

**Technology stack:**

- Microsoft Excel
- PostgreSQL
- SQL
- Python (data import and automation)
- Power BI (business intelligence)

### 2. Data Quality Assessment

| Metric                 | Result |
| ---------------------- | -----: |
| Total records          |  1,000 |
| Valid records          |    998 |
| Records with anomalies |      2 |
| Data quality rate      | 99.80% |

Two records were identified with data quality issues:

- Invalid discount rate and negative net sales.
- Invalid quantity (zero units).

The original records were preserved in the staging table. Analytical views were created to classify anomalies and exclude invalid records from commercial performance analysis.

### 3. Delivered Sales Performance

The commercial analysis includes only valid records with delivered order status.

| KPI              |           Result |
| ---------------- | ---------------: |
| Delivered orders |              577 |
| Units delivered  |            1,551 |
| Gross sales      | MXN 4,546,860.00 |
| Discounts        |   MXN 225,180.00 |
| Net sales        | MXN 4,321,680.00 |
| Total cost       | MXN 3,141,480.00 |
| Gross profit     | MXN 1,180,200.00 |
| Gross margin     |           27.31% |

### 4. Category Performance

- Technology generated the highest net sales: MXN 2,791,202.50.
- Accessories achieved the highest gross margin: 48.14%.
- Components delivered a gross margin of 34.73%.
- Technology generated the highest absolute gross profit.

**Business opportunity:** Increase accessory cross-selling alongside technology products to improve transaction profitability. This opportunity requires further validation through order-level product analysis.

### 5. Regional Performance

- Northeast led net sales with MXN 1,485,405.00.
- Central region achieved the highest gross margin at 28.55%.
- West region had the lowest gross margin at 26.64%.

The region with the highest sales volume was not the region with the highest gross margin.

### 6. Monthly Sales Trends

- March recorded the highest net sales: MXN 614,745.00.
- September ranked second with MXN 529,742.00.
- January achieved the highest gross margin: 31.87%.
- November recorded the lowest gross margin: 25.29%.

These results indicate that higher sales volume does not necessarily translate into higher profitability.

### 7. Sales Channel Performance

- Physical stores generated the highest net sales: MXN 1,607,414.50.
- Telephone sales recorded the highest number of orders: 203.
- Telephone sales achieved the highest gross margin: 27.54%.

Gross margins were relatively consistent across all three channels.

### 8. Salesperson Performance

- Mario Castillo led net sales with MXN 841,688.50.
- Mario Castillo also generated the highest gross profit: MXN 232,158.50.
- Andrea Ruiz achieved the highest gross margin: 27.87%.
- Andrea Ruiz handled the highest number of delivered orders: 110.

### 9. Product Performance

- Laptop 15 pulgadas was the top product by net sales, generating MXN 1,716,075.00.
- Mouse óptico achieved the highest gross margin at 58.73%.
- Audífonos combined a 49.94% gross margin with 165 units delivered.
- Laptop 15 pulgadas generated the highest absolute gross profit: MXN 387,675.00.

### 10. Customer Analysis

- Miguel Hernández was the highest-ranked customer by delivered sales, with MXN 116,000.00.
- The top 10 customers each had only one delivered order.
- 233 customers generated delivered sales.
- 169 customers made more than one delivered purchase.
- Customer repeat rate was 72.53%.
- The highest number of delivered orders by one customer was 9.

### 11. Key Business Recommendations

1. Evaluate accessory cross-selling opportunities with high-value technology products.
2. Investigate the factors behind the lower gross margins in November.
3. Review product pricing and discount strategies for the laptop category.
4. Study the sales mix in the Central region to understand its higher gross margin.
5. Analyze repeat customers to identify opportunities for retention and customer lifetime value.

### 12. Conclusion

The analysis identified the main drivers of delivered sales, profitability, product performance, regional performance, and customer recurrence.

The project demonstrates practical SQL skills, data quality management, business analysis, and the translation of transactional data into actionable business insights.
