from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg

spark = SparkSession.builder.appName("SalesDataETL").getOrCreate()

# Load data
input_path = "wasbs://[container]@[storage_account].blob.core.windows.net/sample_sales_data.csv"
sales_data = spark.read.csv(input_path, header=True, inferSchema=True)

# Data Transformation
transformed_data = sales_data.withColumn("revenue", col("quantity") * col("price"))
kpi_data = transformed_data.groupBy("date").agg(
    sum("revenue").alias("total_revenue"),
    avg("revenue").alias("avg_order_value")
)

# Save to Azure SQL Database
sql_url = "jdbc:sqlserver://[server_name].database.windows.net;database=[database_name]"
sql_properties = {"user": "[username]", "password": "[password]", "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"}

kpi_data.write.jdbc(sql_url, "daily_sales_kpis", mode="overwrite", properties=sql_properties)
