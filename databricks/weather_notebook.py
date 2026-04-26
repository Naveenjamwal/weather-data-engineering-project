# Databricks notebook source
spark.conf.set(
  "fs.azure.account.key.weatherlocal.dfs.core.windows.net",
  "<STORAGE_ACCOUNT_KEY>"
)

df = spark.read.json(
  "abfss://bronze@weatherlocal.dfs.core.windows.net/initial/"
)

# COMMAND ----------

# Flatten JSON
from pyspark.sql.functions import col

df_clean = df.select(
    col("name").alias("City"),
    col("main.temp").alias("temperature"),
    col("main.humidity").alias("humidity"),
    col("weather")[0]["main"].alias("weather_condition")
)

# COMMAND ----------

# Add processing date
from pyspark.sql.functions import current_timestamp, to_date
df_clean = df_clean.withColumn("Processed_Date", to_date(current_timestamp(),'yyyy-MM-dd'))
  


# COMMAND ----------

df_clean.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(
  "abfss://silver@weatherlocal.dfs.core.windows.net/mid/"
)

# COMMAND ----------

df_silver = spark.read.format("delta").load(
  "abfss://silver@weatherlocal.dfs.core.windows.net/mid/"
)

# COMMAND ----------

from pyspark.sql.functions import avg
df_silver = df_clean.groupBy("Processed_Date","City",).agg(avg("temperature").alias("Avg_Temperature"))

  

# COMMAND ----------

df_silver.write.format("csv").mode("overwrite").option("header", "true").save(
  "abfss://gold@weatherlocal.dfs.core.windows.net/ready/") 