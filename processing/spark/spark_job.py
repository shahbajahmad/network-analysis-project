from pyspark.sql import SparkSession

def run_spark_job():
    spark = SparkSession.builder.appName('DataProcessing').getOrCreate()
    df = spark.read.json('hdfs://namenode:9000/data/network_devices.json')
    df.show()

if __name__ == "__main__":
    run_spark_job()
