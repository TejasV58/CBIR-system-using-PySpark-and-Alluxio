from pyspark import SparkContext
from pyspark.sql import SQLContext, Row
from io import StringIO
from PIL import Image
import cv2
import os
import numpy as np
import base64
import time

if __name__ == "__main__":
    sc = SparkContext(appName="image_uploader")
    sqlContext = SQLContext(sc)
    imglist = []
    start = time.time()
    count = 0
    for img_path in os.listdir("./ImageClef5952"):
        try:
            img = cv2.imread("/home/tejasv55/Documents/CBIR-system-using-PySpark-and-Alluxio/ImageClef11963/"+img_path)
            img = cv2.resize(img,(300,300))
            retval, buffer = cv2.imencode('.jpg', img)
            imgtext = base64.b64encode(buffer)
            imglist.append([img_path,imgtext])
        except:
            count+=1
    print(str(count) + " Number of images Failed to Load.")
    rddimglist = sc.parallelize(imglist)
    rddimglist.map(lambda data: (data[0], data[1])).saveAsSequenceFile("alluxio://localhost:19998/SeqImageClef11963")
    end = time.time()
    alluxioFile = sc.sequenceFile("alluxio://localhost:19998/SeqImageClef11963")
    print(alluxioFile.count())
    print("=============================")
    print(f"Time taken: {end-start}")
    print("=============================")
