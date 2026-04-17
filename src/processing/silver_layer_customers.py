from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, current_timestamp
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, DoubleType, IntegerType, BooleanType
from config import create_spark_session

KAFKA_SERVER = "localhost:9092"

BRONZE_PATH = "parquet_output/customers"
SILVER_PATH = "parquet_output/silver_layer/customers"

