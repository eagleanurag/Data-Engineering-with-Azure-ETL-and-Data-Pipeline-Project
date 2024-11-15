# Schema Design

## Azure SQL Database Table: daily_sales_kpis

### Table Description
Stores daily aggregated metrics, providing insights into sales performance. This table is updated daily with new KPI data.

### Table Schema

| Column           | Data Type | Description                       |
|------------------|-----------|-----------------------------------|
| date             | DATE      | The date of the sales data       |
| total_revenue    | FLOAT     | Total revenue generated per day  |
| avg_order_value  | FLOAT     | Average value per order per day  |

### Source Data
The data in `daily_sales_kpis` is derived from raw sales data extracted daily, aggregated to show key performance indicators.

## Example SQL Query
To retrieve total revenue for a specific date range:

```sql
SELECT date, total_revenue
FROM daily_sales_kpis
WHERE date BETWEEN '2024-11-01' AND '2024-11-05';
