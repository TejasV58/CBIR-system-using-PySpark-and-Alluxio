from pyspark import SparkContext
from pyspark.sql import SQLContext, Row
from io import StringIO
from PIL import Image
import cv2
import os
import numpy as np
import base64
import time

from skimage.feature import hog


def extract_HOG_features(img):
    fd = hog(img)
    return fd

if __name__ == "__main__":

    img_size= []
    for img_path in os.listdir("./small_dataset"):
        try:
            img = cv2.imread("/home/tejasv55/Documents/CBIR-system-using-PySpark-and-Alluxio/small_dataset/"+img_path)
            f = extract_HOG_features(img)
            size = f.shape
            if size not in img_size:
                img_size.append(size)
        except:
            print(img_path)
            continue
    print(img_size)
    