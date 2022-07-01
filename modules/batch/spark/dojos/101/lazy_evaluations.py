import pandas as pd

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

df_pandas = pd.DataFrame(data=data,columns=columns)



if __name__ == '__main__':
    sum_pandas = df_pandas["users_count"].sum()
    sum_spark_not_evaluated = df_spark.select("users_count").groupBy().sum()
    sum_spark = sum_spark_not_evaluated.collect()
