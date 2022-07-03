from pyspark.shell import spark

if __name__ == '__main__':
    # in Python
    flightData2015 = spark \
        .read \
        .option("inferSchema", "true") \
        .option("header", "true") \
        .csv("./data/2015-summary.csv")

    flightData2015

