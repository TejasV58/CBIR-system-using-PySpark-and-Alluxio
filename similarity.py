from __future__ import print_function

from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import functions as F

import cv2
import numpy as np
from pyspark import SparkContext
from pyspark.sql import SQLContext, Row
import time

from skimage.feature import hog

def extract_HOG_features(img):
    fd = hog(img)
    return fd


if __name__ == "__main__":
    sc = SparkContext(appName="feature_extractor")
    sqlContext = SQLContext(sc)

    feature_parquet_path = "alluxio://localhost:19998/ImageClef-1000_HOG"
    
    time1 = time.time()
    features = sqlContext.read.parquet(feature_parquet_path).cache()
    time2 = time.time()
    query_img = cv2.imread("/home/sanika/Documents/CBIR-system-using-PySpark-and-Alluxio/Query_Image.JPEG")
    #query_img = cv2.cvtColor(query_img, cv2.COLOR_BGR2GRAY)
    #query_img = cv2.resize(query_img, (360,360))
    qfeatures = extract_HOG_features(query_img)
    time3 = time.time()
    distance_udf = F.udf(lambda f: float(np.linalg.norm(f-qfeatures)),DoubleType())
    distancedf = features.select(F.col("fileName"),distance_udf("features").alias("distance"))
    sorted_distance = distancedf.sort("distance")
    time4 = time.time()
    #sorted_distance.show(truncate=5)
    
    print("======================================================")
    print("############## ImageClef-1000 DATASET ##############")
    print("======================================================")
    print("====================================================")
    print(f"Reading features time         : {time2 - time1}")
    print(f"Query feature extraction time : {time3 - time2}")
    print(f"Parallel KNN time             : {time4 - time3}")
    print(f"Total time required           : {time4 - time1}")
    print("=====================================================")

    