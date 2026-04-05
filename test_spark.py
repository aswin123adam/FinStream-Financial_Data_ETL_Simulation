from pyspark.sql import SparkSession

spark = SparkSession.builder\
    .appName("FinStream Test")\
    .master("local[*]")\
    .getOrCreate()

print("SparkSession created successfully!")
print(f"Spark version: {spark.version}")

spark.stop()