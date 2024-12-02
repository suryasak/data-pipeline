-- DATA ENGINEERING PROJECT--

This project is an ETL (Extract, Transform, Load) pipeline that processes e-commerce transaction data. It demonstrates how raw data is extracted from a CSV file, transformed through cleaning and data processing, and then loaded into an SQLite database for further analysis. The pipeline is automated and orchestrated using Apache Airflow, allowing for scheduled execution and monitoring. The transformation process involves type conversions and date formatting, while the loading phase inserts the cleaned data into a structured SQLite database. This project highlights the integration of Python for data processing, Airflow for orchestration, and SQLite for data storage, making it an efficient and scalable solution for handling transactional data.

Features

1) Extract: Reads raw e-commerce transaction data from a CSV file.
2) Transform: Cleans and processes the data (e.g., type conversion, formatting).
3) Load: Stores the cleaned data into an SQLite database for further analysis.
4) Automation: The entire pipeline is scheduled and orchestrated using Apache Airflow.
