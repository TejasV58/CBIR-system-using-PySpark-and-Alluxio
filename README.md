# CBIR-system-using-PySpark-and-Alluxio

![Sample CBIR image](https://user-images.githubusercontent.com/64249206/147738939-f88c2230-f610-45a5-8ba2-87ad8ff5d45e.jpg)

The task of Content Based Image Retrieval (CBIR) is becoming increasingly complex due to the large number of images available on the internet. This task involves retrieval of similar images based on an input image given by the user. To enable faster computation of similar images, the proposed work uses Apache Spark and Alluxio, previously known as Tachyon. Spark is an open-source software used for processing Big Data. It provides parallelism that reduces computational time. Alluxio on the other hand is a virtual distributed storage system. Although models using Spark for CBIR have been proposed earlier, the proposed model aims at reducing the retrieval time of images by optimizing this task by modifying the feature extraction mechanism. Histogram of oriented gradients (HOG) feature descriptor has been used to find the similarity between images. The K Nearest Neighbours (KNN) algorithm has been used and optimized to compute the top K similar images to query images.

## Requirements

The Linux Operating System is required for the project. The basic requirements include installed and working Apache Spark and Alluxio in your system. The detailed explanation of steps to install  spark and alluxio are given in following sections. The other libraries and packages include:

1. opencv-python
2. pyspark
3. scikit-image

## Steps to run

1. Copying local files to Alluxio : ./bin/alluxio fs copyFromLocal '/home/sanika/Documents/Projects/CBIR spark project/Image Dataset'${ALLUXIO_HOME} /Dataset
2. Starting alluxio : ./bin/alluxio-start.sh local SudoMount
3. Visit http://localhost:19999 and http://localhost:30000
4. Stopping alluxio : ./bin/alluxio-stop.sh local


## SPARK STEPS

Refer this [link](https://computingforgeeks.com/how-to-install-apache-spark-on-ubuntu-debian/) to install spark on your system.

## ALLUXIO STEPS

Download Alluxio from this page. Select the desired release followed by the distribution built for default Hadoop. Unpack the downloaded file with the following commands.
```console
$ tar -xzf alluxio-2.7.2-bin.tar.gz
$ cd alluxio-2.7.2
```
In the ${ALLUXIO_HOME}/conf directory, create the conf/alluxio-site.properties configuration file by copying the template file.
```console
$ cp conf/alluxio-site.properties.template conf/alluxio-site.properties
```          
Set alluxio.master.hostname in conf/alluxio-site.properties to localhost.
```console
$ echo "alluxio.master.hostname=localhost" >> conf/alluxio-site.properties
```
Alluxio provides commands to ensure the system environment is ready for running Alluxio services. Run the following command to validate the environment for running Alluxio locally:

```console
$ ./bin/alluxio validateEnv local
```

Alluxio needs to be formatted before starting the process. The following command formats the Alluxio journal and worker storage directories.

```console
$ ./bin/alluxio format
$ ./bin/alluxio-start.sh local SudoMount
```

### SPARK SETUP FOR ALLUXIO

The Alluxio client jar must be distributed across the all nodes where Spark drivers or executors are running. Place the client jar on the same local path (e.g. /<PATH_TO_ALLUXIO>/client/alluxio-2.7.2-client.jar) on each node.
```shell
spark.driver.extraClassPath   /<PATH_TO_ALLUXIO>/client/alluxio-2.7.2-client.jar
spark.executor.extraClassPath /<PATH_TO_ALLUXIO>/client/alluxio-2.7.2-client.jar
```
