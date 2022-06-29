# importing sparksession from
# pyspark.sql module
from pyspark.sql import SparkSession

# creating sparksession and giving
# app name
spark = SparkSession.builder.appName('sparkdf').getOrCreate()

columns = ["language","users_count"]
data = [("Java", 20000), ("Python", 100000), ("Scala", 3000)]

df_spark = spark.createDataFrame(
    data=data,
    schema=columns
)



if __name__ == '__main__':
    sum_spark_not_evaluated = df_spark.select("users_count").groupBy().sum()
    sum_spark = sum_spark_not_evaluated.collect()
    sum_spark_optimized = df_spark.rdd.map(lambda x: (1, x[1])).reduceByKey(lambda x, y: x + y).collect()[0][1]

    # Avoid GroupByKey
    # https://databricks.gitbooks.io/databricks-spark-knowledge-base/content/best_practices/prefer_reducebykey_over_groupbykey.html