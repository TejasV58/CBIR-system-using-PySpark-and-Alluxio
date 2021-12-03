import sys, os, glob, shutil
new_dir = '/home/sanika/Documents/Projects/CBIR-system-using-PySpark-and-Alluxio/TinyImageNet/'
in_dir = '/home/sanika/Downloads/archive/TinyImageNet/train/'
c = 1
for i in range(0,100):
    img_files = os.listdir(in_dir + str(i)+"/")
    for img in img_files :
        shutil.move(in_dir + str(i)+"/"+img, new_dir)
        print(c)
        c = c +1
    
