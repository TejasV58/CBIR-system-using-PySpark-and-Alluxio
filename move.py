import sys, os, glob, shutil
new_dir1 = '/home/sanika/Documents/CBIR-system-using-PySpark-and-Alluxio/ImageNet-200/'
new_dir2 = '/home/sanika/Documents/CBIR-system-using-PySpark-and-Alluxio/ImageNet-500/'
new_dir3 = '/home/sanika/Documents/CBIR-system-using-PySpark-and-Alluxio/ImageNet-1000/'
new_dir4 = '/home/sanika/Documents/CBIR-system-using-PySpark-and-Alluxio/ImageNet-2000/'
new_dir5 = '/home/sanika/Documents/CBIR-system-using-PySpark-and-Alluxio/ImageNet-5000/'
in_dir = '/home/sanika/Documents/CBIR-system-using-PySpark-and-Alluxio/TinyImageNet/'
img_files = os.listdir(in_dir)
c=1
for img in img_files :
    if c<=200 :
        shutil.copy(in_dir +img, new_dir1)
        shutil.copy(in_dir +img, new_dir2)
        shutil.copy(in_dir +img, new_dir3)
        shutil.copy(in_dir +img, new_dir4)
        shutil.copy(in_dir +img, new_dir5)
    elif c<=500 :
        shutil.copy(in_dir +img, new_dir2)
        shutil.copy(in_dir +img, new_dir3)
        shutil.copy(in_dir +img, new_dir4)
        shutil.copy(in_dir +img, new_dir5)
    elif c<=1000 :
        shutil.copy(in_dir +img, new_dir3)
        shutil.copy(in_dir +img, new_dir4)
        shutil.copy(in_dir +img, new_dir5)
    elif c<=2000 :
        shutil.copy(in_dir +img, new_dir4)
        shutil.copy(in_dir +img, new_dir5)
    elif c<=5000 :
        shutil.copy(in_dir +img, new_dir5)

    print(c)
    c = c +1
    if c == 5001:
        break
    
