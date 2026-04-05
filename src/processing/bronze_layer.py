from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import from_json, col, current_timestamp, lit
from config import create_spark_session

KAFKA_SERVER = "localhost:9092"
CUSTOMERS_TOPIC = "finstream.customers"

def process_bronze_layer(spark, topic: str) -> DataFrame:
    df = spark.read\
        .format("kafka")\
        .option("kafka.bootstrap.servers", KAFKA_SERVER)\
        .option("subscribe", topic)\
        .option("startingOffsets", "earliest")\
        .load()
    return df


if __name__ == "__main__":
    spark = create_spark_session("FinStream Bronze Layer Test")

    print("Reading from KAFKA topic...")

    raw_data = process_bronze_layer(spark, CUSTOMERS_TOPIC)
    print("Schema :")
    raw_data.summary().show()
    decoded_data = raw_data.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)", "timestamp")

    print("Raw Data from KAFKA :")
    decoded_data.show(5, truncate=False)
    spark.stop()
