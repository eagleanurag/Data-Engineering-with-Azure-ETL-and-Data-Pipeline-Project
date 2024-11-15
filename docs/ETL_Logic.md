# ETL Logic for Sales Data Pipeline

## Overview
The ETL pipeline extracts raw sales data from an FTP server, transforms it to calculate daily KPIs, and loads it into an Azure SQL Database for analysis. The ETL process runs daily to ensure updated insights for the sales team.

### ETL Steps

1. **Extraction**
   - Use Azure Data Factory (ADF) to connect to the FTP server and download the sales data in CSV format.
   - Load data from the FTP server into Azure Blob Storage for staging.

2. **Transformation**
   - Ingest data from Azure Blob Storage into Databricks, where PySpark processes it.
   - Perform transformations:
     - **Data Cleansing**: Remove duplicates, handle missing values.
     - **Revenue Calculation**: Calculate `revenue = quantity * price` for each transaction.
     - **Daily KPIs**: Aggregate metrics, including total revenue and average order value.

3. **Loading**
   - Write the transformed data to Azure SQL Database, creating or updating the `daily_sales_kpis` table.
   - This table enables quick querying and analytics by the sales team.
