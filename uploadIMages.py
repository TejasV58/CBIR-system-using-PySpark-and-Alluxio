from pyspark import SparkContext
from pyspark.sql import SQLContext, Row
from io import StringIO
from PIL import Image
import cv2
import os
import numpy as np
import base64


if __name__ == "__main__":
    sc = SparkContext(appName="feature_extractor")
    sqlContext = SQLContext(sc)
    imglist = []
    for img_path in os.listdir("./TinyImageNet/"):
        img = cv2.imread("./TinyImageNet/"+img_path)
        retval, buffer = cv2.imencode('.jpg', img)
        imgtext = base64.b64encode(buffer)
        # decodeimg = base64.b64decode(imgtext)
        # nparr = np.fromstring(decodeimg, np.uint8)
        # img1 = cv2.imdecode(nparr,3)
        imglist.append([img_path,imgtext])
    rddimglist = sc.parallelize(imglist)
    #x = sc.binaryFiles("/home/tejasv55/Documents/PDC-SPARK-CBIR/small_dataset")
    rddimglist.map(lambda data: (data[0], data[1])).saveAsSequenceFile("alluxio://localhost:19998/SequenceFiles-10K")
    alluxioFile = sc.sequenceFile("alluxio://localhost:19998/SequenceFiles-10K") 
    print(alluxioFile.count())
    print("===========================")
    print("===========================")

