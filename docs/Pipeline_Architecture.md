# Pipeline Architecture

## Overview
The pipeline is designed to extract, transform, and load data in a scalable way, using Azure services to handle data ingestion, processing, and storage.

### Architecture Components

1. **Azure Data Factory (ADF)**
   - Orchestrates the ETL process, triggering pipeline activities such as file copying and Databricks notebook execution.

2. **Azure Blob Storage**
   - Serves as a staging area where ADF loads raw data from the FTP server.
   - Provides scalable storage for both raw and intermediate data.

3. **Azure Databricks**
   - Processes data using PySpark, handling large data volumes and distributed transformations.
   - Connects to Blob Storage for input data and Azure SQL Database for final data storage.

4. **Azure SQL Database**
   - Stores the final, processed data in the `daily_sales_kpis` table.
   - Enables efficient querying and supports reporting and analytics.

### Data Flow Diagram
1. **Data Ingestion**: FTP server → ADF → Blob Storage
2. **Transformation**: Databricks reads from Blob Storage → Processes with PySpark → Loads into SQL Database
3. **Final Data Storage**: Azure SQL Database stores transformed KPI data
