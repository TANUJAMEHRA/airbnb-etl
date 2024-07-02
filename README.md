# Airbnb NYC ETL Pipeline

This project demonstrates a scalable ETL (Extract, Transform, Load) pipeline using the Airbnb New York City dataset. The
pipeline involves data ingestion, transformation, and loading into a PostgreSQL database. Additionally, the ETL workflow
is managed using Metaflow.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Project Setup](#project-setup)
3. [Database Setup](#database-setup)
4. [Running the ETL Pipeline](#running-the-etl-pipeline)
5. [ETL Process Explanation](#etl-process-explanation)
6. [Project Structure](#project-structure)
7. [References](#references)

## Prerequisites

- PostgreSQL installed locally or on a cloud instance
- Python environment with necessary libraries installed (`pandas`, `SQLAlchemy`, `Metaflow`, etc.)
- Git installed for version control

## Project Setup

1. **Clone the Repository:**
   ```sh
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Create a Virtual Environment and Install Dependencies:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

## Database Setup

1. **Install PostgreSQL:**
    - Follow the instructions [here](https://www.postgresql.org/download/) to install PostgreSQL on your machine.

2. **Create a Database:**
   ```sh
   psql -U postgres
   CREATE DATABASE airbnb_nyc;
   ```

3. **Update Database Credentials:**
    - Modify the database connection string in your scripts (
      e.g., `postgresql://username:password@localhost:5432/airbnb_nyc`).

## Running the ETL Pipeline

1. **Run the Data Loading Script:**
   ```sh
   python data_loading.py
   ```

2. **Run the ETL Pipeline with Metaflow:**
   ```sh
   export METAFLOW_CONFIG=/path/to/metaflow_config.py
   python etl_pipeline.py
   ```

## ETL Process Explanation

### Data Ingestion

- **Dataset Selection:** The Airbnb New York City dataset from Kaggle is used.
- **Data Loading:** The dataset is loaded into a PostgreSQL table using `pandas` and `SQLAlchemy`.

### Data Transformation

- **Normalization:** Date and time are separated into different columns.
- **Calculations:** Additional metrics like average price per neighborhood are calculated.
- **Missing Values:** Handled appropriately by filling, removing, or flagging them.

### Data Loading

- The transformed data is loaded into a new PostgreSQL table.

### Workflow Management with Metaflow

- **Steps Implemented:**
    - `start`: Initial step
    - `extract`: Extract data from PostgreSQL
    - `transform`: Transform the data
    - `load`: Load transformed data into PostgreSQL
    - `end`: Final step indicating successful completion

## Project Structure

```
.
├── data_loading.py         # Script for loading data into PostgreSQL
├── etl_pipeline.py         # Metaflow script for ETL pipeline
├── requirements.txt        # List of dependencies
├── README.md               # Project documentation
└── metaflow_config.py      # Metaflow configuration file
```

## References

- [Metaflow Documentation](https://docs.metaflow.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Airbnb New York City Dataset on Kaggle](https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data)
