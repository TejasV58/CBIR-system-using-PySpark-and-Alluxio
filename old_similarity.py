from __future__ import print_function

from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import functions as F

import cv2
import numpy as np
from pyspark import SparkContext
from pyspark.sql import SQLContext,SparkSession
import time

from skimage.feature import hog
from scipy.spatial import distance

def collect_top5_files(data):
    filenames.append(data.fileName)
    return data

if __name__ == "__main__":
    # sc = SparkSession.builder\
    #     .master('local[*]')\
    #     .config("spark.driver.memory","2g")\
    #     .appName("Simialrity")\
    #     .getOrCreate()
    sc = SparkContext(appName="feature_extractor")
    memory = sc._conf.get('spark.driver.memory')
    sqlContext = SQLContext(sc)
    feature_parquet_path = "alluxio://localhost:19998/ImageNet20000Features"
    
    features = sqlContext.read.parquet(feature_parquet_path)
    # features.show()
    # features = features.head(20)
    # features = sqlContext.createDataFrame(features)
    query_img = cv2.imread("/home/tejasv55/Documents/CBIR-system-using-PySpark-and-Alluxio/Query_Image.jpg")
    # query_img = cv2.resize(query_img, (300,300))
    query_img = cv2.cvtColor(query_img, cv2.COLOR_BGR2GRAY)
    qfeatures = hog(query_img)
    distance_udf = F.udf(lambda x: float(distance.euclidean(np.array(x),qfeatures)),FloatType())
    distancedf = features.select(F.col("fileName"),distance_udf(F.col("features")).alias("distance"))
    sorted_distance = distancedf.sort("distance")
    print("==================================================")
    print("sorting files part done")
    print("==================================================")
    sd = sorted_distance.limit(5)
    sdfiles = sd.select(F.col("fileName"))
    sdfiles.show()
    # sd = sd.rdd.map(collect_top5_files)
    # data = sd.collect()
    # print(data)
    

    # print("====================================================")
    # print("############## IMAGECLEF 2011 DATASET ##############")
    # print("====================================================")
    # print(f"Reading features time         : {time2 - time1}")
    # print(f"Query feature extraction time : {time3 - time2}")
    # print(f"Parallel KNN time             : {time4 - time3}")
    # print(f"Total time required           : {time4 - time1}")
    # print("=====================================================")



