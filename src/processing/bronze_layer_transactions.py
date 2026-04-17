from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import from_json, col, current_timestamp
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, DoubleType, IntegerType, BooleanType
from config import create_spark_session

KAFKA_SERVER = "localhost:9092"
TRANSACTIONS_TOPIC = "finstream.transactions"

TRANSACTION_SCHEMA = StructType([
    StructField("transaction_id", StringType(), True),
    StructField("customer_id", StringType(), True),
    StructField("transaction_type", StringType(), True),
    StructField("transaction_category", StringType(), True),
    StructField("amount", DoubleType(), True),
    StructField("merchant", StringType(), True),
    StructField("transaction_date", StringType(), True),
    StructField("description", StringType(), True),
])

def process_bronze_layer_transactions(spark, topic: str) -> DataFrame:
    df = spark.read\
        .format("kafka")\
        .option("kafka.bootstrap.servers", KAFKA_SERVER)\
        .option("subscribe", topic)\
        .option("startingOffsets", "earliest")\
        .load()
    return df

def parse_bronze_data_transactions(df: DataFrame) -> DataFrame:
    parsed_df = df\
        .selectExpr("CAST(value AS STRING) as json_data", "timestamp as kafka_timestamp")\
        .select(from_json(col("json_data"), TRANSACTION_SCHEMA).alias("data"),
                col("kafka_timestamp"))\
        .select("data.*", "kafka_timestamp")\
        .withColumn("processed_at", current_timestamp())
    return parsed_df

def save_to_parquet_transactions(df: DataFrame, path: str):
    df.write.mode("append").parquet(path)

if __name__ == "__main__":
    spark = create_spark_session("FinStream-Bronze-Layer-Transactions")

    print(f"Reading from KAFKA topic : {TRANSACTIONS_TOPIC}")
    raw_data = process_bronze_layer_transactions(spark, TRANSACTIONS_TOPIC)
    processed_data = parse_bronze_data_transactions(raw_data)
    save_to_parquet_transactions(processed_data, "parquet_output/transactions")

    processed_data.show(truncate=False)

    spark.stop()

