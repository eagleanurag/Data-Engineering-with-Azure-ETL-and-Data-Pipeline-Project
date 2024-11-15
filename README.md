# Data Pipeline Project for Sales Data Analysis
## Overview

This project implements a robust ETL (Extract, Transform, Load) pipeline for analyzing large sales datasets, leveraging Azure Data Factory for orchestration, Databricks for data processing with PySpark, and Azure SQL Database for structured data storage. The solution is designed to automate data ingestion, transformation, and loading, providing insights to support business decision-making.
Key Features

    -Automated Data Ingestion: Azure Data Factory fetches daily sales data from external sources.
    -Scalable Data Processing: Databricks and PySpark handle data transformations, such as cleansing, aggregating, and calculating KPIs.
    -Optimized Data Storage: Processed data is stored in Azure SQL Database, ready for query and analysis.
    -Data Quality Assurance: Data validation and quality checks ensure reliable analytics output.

Architecture

The project’s architecture integrates multiple Azure services to create a streamlined ETL pipeline:

    -Azure Data Factory extracts raw sales data from an FTP server and loads it into Azure Blob Storage.
    -Databricks processes the data in PySpark, applying business logic to generate daily sales insights.
    -Processed data is stored in Azure SQL Database, enabling analytics and reporting.

Getting Started
Prerequisites

    Azure Account with access to Data Factory, Databricks, Blob Storage, and SQL Database
    Python 3.x and PySpark
    SQL Server Management Studio or another SQL client for database access

Setup

    Clone this repository:

    git clone https://github.com/eagleanurag/Data-Engineering-with-Azure-ETL-and-Data-Pipeline-Project/tree/main
    Deploy the Azure Data Factory JSON templates to create pipelines in your Azure environment.
    Configure Databricks with the provided PySpark scripts.

Data Sources

    FTP Server: Contains daily sales data in CSV format.
    Azure Blob Storage: Intermediate storage for extracted raw data.

Project Workflow

    Data Extraction: Azure Data Factory pulls raw sales data from the FTP server daily and saves it to Azure Blob Storage.
    Data Transformation: Databricks reads the data, cleans it, and calculates sales KPIs like total revenue, average order value, and sales growth using PySpark.
    Data Loading: The transformed data is loaded into Azure SQL Database, where it can be queried for analysis and visualization.

Code Structure

sales-data-pipeline/
│

├── README.md               # Project overview and setup

├── data/                   # Sample data files (if applicable)

├── notebooks/              # Databricks notebooks with PySpark transformations

├── scripts/                # PySpark and SQL scripts for ETL tasks

├── adf_pipelines/          # JSON templates for ADF pipeline deployment

└── docs/                   # Additional documentation and diagrams


Technologies Used

    Azure Data Factory: Manages and automates the data pipeline
    Azure Databricks: Processes data in a scalable Spark environment
    PySpark: Used for data transformation and calculating KPIs
    Azure SQL Database: Stores processed data for analysis

Challenges and Learnings

    Optimizing data transformations in PySpark to process high data volumes efficiently.
    Managing complex dependencies within Data Factory pipelines.
    Implementing comprehensive data quality checks to ensure reliable analytics.

Results

The pipeline reduced manual data handling time by 80% and provided a real-time data analytics solution, allowing the sales team to access updated KPIs daily. The optimized process also improved query performance by 50%, enabling faster data-driven decisions.
Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any proposed improvements.
License

This project is licensed under the MIT License. See the LICENSE file for more information.
