Data Engineering Pipeline Project

This repository contains an ETL (Extract, Transform, Load) pipeline project that processes e-commerce transaction data. The project demonstrates the use of Python, Apache Airflow, and SQLite to handle raw data, clean and transform it, and load it into a database for analysis.

Features
Extract: Reads raw e-commerce transaction data from a CSV file.
Transform: Cleans and processes the data (e.g., type conversion, formatting).
Load: Stores the cleaned data into an SQLite database for further analysis.
Automation: Scheduled and orchestrated using Apache Airflow.

Directory Structure
.
├── data
│   └── raw_transactions.csv         # Raw input data
├── dags
│   └── etl_pipeline.py              # Airflow DAG for the ETL pipeline
├── scripts
│   ├── transform_data.py            # Python script for data transformation
│   └── load_data.py                 # Python script for loading data into SQLite
├── requirements.txt                 # Dependencies for the project
└── README.md                        # Project documentation

Prerequisites
Python 3.7+
Apache Airflow
SQLite (comes pre-installed with Python)
Install dependencies using requirements.txt:
pip install -r requirements.txt

How to Run the Project
Step 1: Set Up the Environment
Clone the repository:
git clone https://github.com/suryasaketh/data-pipeline.git
cd data-pipeline

Install the required Python packages:
pip install -r requirements.txt

Step 2: Run the ETL Pipeline
Initialize Airflow's database:
airflow db init

Start the Airflow webserver and scheduler in separate terminals:
Webserver:
airflow webserver --port 8080

Scheduler:
airflow scheduler

Open the Airflow web UI in your browser at http://localhost:8080.

Activate the ecommerce_etl_pipeline DAG to run the pipeline.


Step 3: Verify the Results
After running the DAG, check the following:
Transformed Data: Located in data/cleaned_transactions.csv.
SQLite Database: Open the database (ecommerce.db) to verify the loaded data:

sqlite3 ecommerce.db
SELECT * FROM transactions;

Sample Data
The project processes a sample dataset (raw_transactions.csv):
transaction_id,customer_id,product_id,amount,date
1,101,501,50.5,2023-01-01
2,102,502,20.0,2023-01-02
3,103,503,35.0,2023-01-03



Here’s a README.md file you can use for your Data Engineering project:

Data Engineering Pipeline Project
This repository contains an ETL (Extract, Transform, Load) pipeline project that processes e-commerce transaction data. The project demonstrates the use of Python, Apache Airflow, and SQLite to handle raw data, clean and transform it, and load it into a database for analysis.

Features
Extract: Reads raw e-commerce transaction data from a CSV file.
Transform: Cleans and processes the data (e.g., type conversion, formatting).
Load: Stores the cleaned data into an SQLite database for further analysis.
Automation: Scheduled and orchestrated using Apache Airflow.
Directory Structure
plaintext
Copy code
.
├── data
│   └── raw_transactions.csv         # Raw input data
├── dags
│   └── etl_pipeline.py              # Airflow DAG for the ETL pipeline
├── scripts
│   ├── transform_data.py            # Python script for data transformation
│   └── load_data.py                 # Python script for loading data into SQLite
├── requirements.txt                 # Dependencies for the project
└── README.md                        # Project documentation
Prerequisites
Python 3.7+
Apache Airflow
SQLite (comes pre-installed with Python)
Install dependencies using requirements.txt:
bash
Copy code
pip install -r requirements.txt
How to Run the Project
Step 1: Set Up the Environment
Clone the repository:

bash
Copy code
git clone https://github.com/suryasaketh/data-pipeline.git
cd data-pipeline
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Step 2: Run the ETL Pipeline
Initialize Airflow's database:

bash
Copy code
airflow db init
Start the Airflow webserver and scheduler in separate terminals:

Webserver:
bash
Copy code
airflow webserver --port 8080
Scheduler:
bash
Copy code
airflow scheduler
Open the Airflow web UI in your browser at http://localhost:8080.

Activate the ecommerce_etl_pipeline DAG to run the pipeline.

Step 3: Verify the Results
After running the DAG, check the following:
Transformed Data: Located in data/cleaned_transactions.csv.
SQLite Database: Open the database (ecommerce.db) to verify the loaded data:
bash
Copy code
sqlite3 ecommerce.db
SELECT * FROM transactions;
Sample Data
The project processes a sample dataset (raw_transactions.csv):
transaction_id,customer_id,product_id,amount,date
1,101,501,50.5,2023-01-01
2,102,502,20.0,2023-01-02
3,103,503,35.0,2023-01-03

Technologies Used
Programming Language: Python
Data Orchestration: Apache Airflow
Database: SQLite
Libraries: pandas, sqlite3




