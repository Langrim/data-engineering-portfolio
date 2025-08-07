from pyspark.sql import SparkSession, functions as F

def main():
    spark = (
        SparkSession.builder
        .appName("portfolio-batch-etl")
        .getOrCreate()
    )

    # Input/Output
    input_path = "projects/batch-etl/data/input/sample_orders.csv"
    output_path = "projects/batch-etl/data/output/orders_parquet"

    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(input_path)
    )

    # Basic transforms
    df_tr = (
        df.withColumn("amount_usd", F.col("amount").cast("double"))
          .withColumn("event_date", F.to_date(F.col("event_time").substr(1, 10)))  # YYYY-MM-DD
          .dropna(subset=["amount_usd", "country"])
          .filter(F.col("amount_usd") > 0)
    )

    # Write partitioned parquet
    (
        df_tr.write
        .mode("overwrite")
        .partitionBy("country")
        .parquet(output_path)
    )

    print(f"Wrote parquet to {output_path}")
    spark.stop()

if __name__ == "__main__":
    main()
