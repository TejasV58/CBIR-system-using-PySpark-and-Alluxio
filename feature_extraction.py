from __future__ import print_function
import logging

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

def extract_opencv_features(imgfile_imgbytes):
    try:
        imgfilename, imgbytes = imgfile_imgbytes
        decodeimg = base64.b64decode(imgbytes)
        nparr = np.frombuffer(decodeimg, np.uint8)
        img = cv2.imdecode(nparr,0)
        d = hog(img)
        return [(imgfilename, d)]
    except Exception as e:
        logging.exception(e)
        return []


if __name__ == "__main__":
    sc = SparkContext(appName="feature_extractor")
    sqlContext = SQLContext(sc)
    
    image_seqfile_path = "alluxio://localhost:19998/SeqImageClef11963"
    feature_parquet_path = "alluxio://localhost:19998/SeqImageClef11963Features"
    
    Total_start = time.time()
    images = sc.sequenceFile(image_seqfile_path)
    read_end = time.time()
    features = images.flatMap(extract_opencv_features)
    extract_end = time.time()
    #features = features.filter(lambda x: x[1] != None)
    features = features.map(lambda x: (Row(fileName=x[0], features=x[1].tolist())))
    featuresSchema = sqlContext.createDataFrame(features)
    featuresSchema.registerTempTable("images")
    store_time = time.time()
    featuresSchema.write.parquet(feature_parquet_path)
    Total_end = time.time()
    print("===================================================")
    print("############## IMAGECLEF 5952 DATASET ##############")
    print("===================================================")
    print(f"Sequence file read time : {read_end - Total_start}")
    print(f"Feature extraction time : {extract_end - read_end}")
    print(f"Conversion df time      : {store_time - extract_end}")
    print(f"Features storing time   : {Total_end - store_time}")
    print(f"Total time required     : {Total_end - Total_start}")
    print("====================================================")

