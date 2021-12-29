from __future__ import print_function

from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import functions as F

import cv2
import sys
import numpy as np
from pyspark import SparkContext
from pyspark.sql import SQLContext,SparkSession
import time

from skimage.feature import hog
from scipy.spatial import distance

def find_distance(feature,qfeature):
    try:
        dist = float(distance.euclidean(feature[1],qfeature))
        return (feature[0],dist)
    except:
        return (feature[0],sys.float_info.max)


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
    features_rdd = features.limit(5000).rdd

    query_img = cv2.imread("/home/tejasv55/Documents/CBIR-system-using-PySpark-and-Alluxio/Query_Image.jpg")
    # query_img = cv2.resize(query_img, (300,300))
    query_img = cv2.cvtColor(query_img, cv2.COLOR_BGR2GRAY)
    qfeature = hog(query_img)

    distances = features_rdd.map(lambda x: find_distance(x,qfeature))
    top5 = distances.sortBy(lambda x: x[1]).take(5)
    print("==============================================================")
    print(top5)
    print("==============================================================")



