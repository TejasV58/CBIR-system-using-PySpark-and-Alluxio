from __future__ import print_function
import logging
import io
import sys
import os

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import functions as F

import cv2
import numpy as np
from pyspark import SparkContext
from pyspark.sql import SQLContext, Row
import base64
import time

from skimage.feature import hog
from skimage import data, exposure

def extract_SIFT_features(img):
    # extractor = cv2.SIFT_create()
    # kp = extractor.detect(img, None)
    # kp,des = extractor.compute(img,kp)
    fd = hog(img)
    return fd

def extract_opencv_features(imgfile_imgbytes):
    try:
        imgfilename, imgbytes = imgfile_imgbytes
        decodeimg = base64.b64decode(imgbytes)
        nparr = np.frombuffer(decodeimg, np.uint8)
        img = cv2.imdecode(nparr,0)
        img = cv2.resize(img,(300,300))
        d = extract_SIFT_features(img)
        print(d.shape)
        return [(imgfilename, d)]
    except Exception as e:
        logging.exception(e)
        return []


if __name__ == "__main__":
    sc = SparkContext(appName="feature_extractor")
    sqlContext = SQLContext(sc)

    try:
        feature_name = "SIFT"
        image_seqfile_path = "alluxio://localhost:19998/SequenceFiles"
        feature_parquet_path = "alluxio://localhost:19998/parquetHOGFeatures"
    except:
        print("Usage: spark-submit feature_extraction.py <feature_name(sift or surf)> "
              "<image_sequencefile_input_path> <feature_sequencefile_output_path> <partitions>")
    start = time.time()
    images = sc.sequenceFile(image_seqfile_path)
    features = images.flatMap(extract_opencv_features)
    end = time.time()
    #features = features.filter(lambda x: x[1] != None)
    features = features.map(lambda x: (Row(fileName=x[0], features=x[1].tolist())))
    featuresSchema = sqlContext.createDataFrame(features)
    featuresSchema.show()
    featuresSchema.registerTempTable("images")
    featuresSchema.write.parquet(feature_parquet_path)
    
    print("============================================")
    print(f"Total time required : {end - start}")
    print("============================================")

