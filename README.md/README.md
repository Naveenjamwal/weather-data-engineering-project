# 🌦️ Weather Data Engineering Pipeline

## 📌 Overview

This project demonstrates an end-to-end Azure Data Engineering pipeline that ingests weather data from a REST API, processes it using Databricks, and loads it into Snowflake for analytics.

---

## 🏗️ Architecture

REST API → ADF → ADLS (Bronze)
→ Databricks (Silver & Gold - Delta Lake)
→ ADLS (CSV Output)
→ Snowflake (External Stage + COPY INTO)

---

## ⚙️ Tech Stack

* Azure Data Factory (ADF)
* Azure Data Lake Storage Gen2 (ADLS)
* Azure Databricks (PySpark)
* Snowflake
* Delta Lake

---

## 🔄 Pipeline Flow

1. ADF extracts weather data using REST API
2. Stores raw data in ADLS (Bronze layer)
3. Databricks processes data into Silver & Gold layers
4. Gold data converted to CSV and stored in ADLS
5. Snowflake loads data using external stage
6. ADF triggers COPY INTO using Script Activity

---

## 🚀 Key Features

* Dynamic ingestion using ForEach loop (multiple cities)
* Medallion Architecture (Bronze, Silver, Gold)
* Incremental load using Snowflake (FORCE = FALSE)
* Automated pipeline execution in ADF
* Error handling using ON_ERROR

---

## 📊 Data Volume

* Processes ~10–50 MB per run (scalable design)

---

## 📁 Project Structure

```
weather-data-engineering-project/
│
├── adf/
├── databricks/
├── sql/
├── data/
└── README.md
```

---

## 🔐 Security Note

Sensitive information like keys, tokens, and passwords are not included. Placeholders are used for security.

---

## 🔗 GitHub

https://github.com/Naveenjamwal

---

## 📌 Future Enhancements

* Implement watermark-based incremental load
* Add logging and monitoring
* Optimize using Parquet format
