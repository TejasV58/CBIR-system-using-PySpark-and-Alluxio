from __future__ import print_function

from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import functions as F

import cv2
import numpy as np
from pyspark import SparkContext
from pyspark.sql import SQLContext, Row
import time

from skimage.feature import hog,ORB,SIFT

def extract_HOG_features(img):
    # hog = cv2.HOGDescriptor()
    # des = hog.compute(img)
    # extractor = cv2.SIFT_create()
    # kp = extractor.detect(img, None)
    # kp,des = extractor.compute(img,kp)
    fd = hog(img)
    return fd


if __name__ == "__main__":
    sc = SparkContext(appName="feature_extractor")
    sqlContext = SQLContext(sc)

    feature_parquet_path = "alluxio://localhost:19998/parquetHOGFeatures-10K"
    
    features = sqlContext.read.parquet(feature_parquet_path).cache()
    start = time.time()
    query_img = cv2.imread("./Query_Image.jpg")
    query_img = cv2.cvtColor(query_img, cv2.COLOR_BGR2GRAY)
    query_img = cv2.resize(query_img, (300,300))
    qfeatures = extract_HOG_features(query_img)
    distance_udf = F.udf(lambda f: float(np.linalg.norm(f-qfeatures)),DoubleType())
    distancedf = features.select(F.col("fileName"),distance_udf("features").alias("distance"))
    sorted_distance = distancedf.sort("distance")
    end = time.time()
    sorted_distance.show()
    

    print("============================================")
    print(f"Total time required : {end - start}")
    print("============================================")

    # query_rdd = sc.parallelize(qfeatures)
    # features_rdd = features.rdd
    # print(features_rdd.collect()[0]['features'])
    # distances = features_rdd.map(lambda x: compute_distance(x['fileName'],x['features'],query_rdd))
    

    