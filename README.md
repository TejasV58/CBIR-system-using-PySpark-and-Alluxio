# CBIR-system-using-PySpark-and-Alluxio

1. Copying local files to Alluxio : ./bin/alluxio fs copyFromLocal '/home/sanika/Documents/Projects/CBIR spark project/Image Dataset'${ALLUXIO_HOME} /Dataset
2. Starting alluxio : ./bin/alluxio-start.sh local SudoMount
3. Visit http://localhost:19999 and http://localhost:30000
4. Stopping alluxio : ./bin/alluxio-stop.sh local
