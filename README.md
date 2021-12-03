# CBIR-system-using-PySpark-and-Alluxio

Copying local files to Alluxio : ./bin/alluxio fs copyFromLocal '/home/sanika/Documents/Projects/CBIR spark project/Image Dataset'${ALLUXIO_HOME} /Dataset
Starting alluxio : ./bin/alluxio-start.sh local SudoMount
Visit http://localhost:19999 and http://localhost:30000
Stopping alluxio : ./bin/alluxio-stop.sh local
