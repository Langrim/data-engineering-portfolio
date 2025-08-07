# AWS Labs — S3 → Glue → Athena (Terraform skeleton)

**Goal:** Refresh AWS skills by building a simple, low-cost pipeline:
- Upload `sample_orders.csv` to S3
- Create a Glue database/table (via crawler or Glue job)
- Query with Athena

## Steps
1. Create an S3 bucket (name must be globally unique).
2. Upload sample data from `projects/batch-etl/data/input/sample_orders.csv`.
3. Configure Glue Crawler → discover schema → create table.
4. Query with Athena; save results to a separate S3 prefix.
5. Bonus: Replace crawler with a Glue Job that writes Parquet.

See `main.tf` for Terraform skeleton.
