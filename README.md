# Data Engineering Portfolio — Langrim

This repository showcases practical, interview-ready data engineering skills.

## Stack (current focus)
- **PySpark**, **Python**, **SQL**
- **Airflow** for orchestration (local demonstration)
- **AWS refresh labs**: S3 → Glue → Athena (Terraform skeleton)

## Projects
1) `projects/batch-etl` — Ingest a CSV, transform with PySpark, and write partitioned **Parquet**.
2) `orchestration/airflow` — A sample DAG orchestrating extract → transform → validate → load.
3) `aws-labs` — Notes and Terraform skeleton for S3/Glue/Athena.

## Getting started (local dev)
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
> Tip: You can run the PySpark batch job without installing Java locally by using a Docker image or Databricks Community; for now the script is vanilla `SparkSession` and should work in a local Spark setup.

## Roadmap / TODO
- [ ] Add Great Expectations checks for the batch ETL
- [ ] Add a proper `docker-compose` for local Airflow
- [ ] Complete AWS lab: upload sample data to S3, create Glue crawler/job, query via Athena
- [ ] Add CI (pre-commit, flake8/ruff, black, pytest)
