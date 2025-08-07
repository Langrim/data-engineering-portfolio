# Batch ETL (PySpark)

**Goal:** Ingest sample CSV → transform → write partitioned Parquet.

## Run
```bash
python projects/batch-etl/batch_etl.py
# or with spark-submit if configured
# spark-submit projects/batch-etl/batch_etl.py
```
## What it does
- Casts `amount` to double
- Derives `event_date` from `event_time`
- Drops invalid rows and filters non-positive amounts
- Writes Parquet partitioned by `country` to `data/output/orders_parquet`
