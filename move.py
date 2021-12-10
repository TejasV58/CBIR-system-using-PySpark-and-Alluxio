import sys, os, glob, shutil
new_dir1 = './ImageClef5952/'
new_dir2 = './ImageClef11963/'
new_dir3 = './ImageClef17953/'
new_dir4 = './ImageClef20000/'
in_dir = './iaprtc12/images/'
print(len(os.listdir(new_dir1)))
print(len(os.listdir(new_dir2)))
print(len(os.listdir(new_dir3)))
print(len(os.listdir(new_dir4)))
# dirs = os.listdir(in_dir)
# c=1
# for dir in dirs:
#     img_files = os.listdir(in_dir+dir+'/')
#     for img in img_files :
#         if c<=5952 :
#             shutil.copy(in_dir+dir+'/' +img, new_dir1)
#             shutil.copy(in_dir+dir+'/' +img, new_dir2)
#             shutil.copy(in_dir+dir+'/' +img, new_dir3)
#             shutil.copy(in_dir+dir+'/' +img, new_dir4)
#         elif c<=11963 :
#             shutil.copy(in_dir+dir+'/' +img, new_dir2)
#             shutil.copy(in_dir+dir+'/' +img, new_dir3)
#             shutil.copy(in_dir+dir+'/' +img, new_dir4)
#         elif c<=17953 :
#             shutil.copy(in_dir+dir+'/' +img, new_dir3)
#             shutil.copy(in_dir+dir+'/' +img, new_dir4)
#         elif c<=20000 :
#             shutil.copy(in_dir+dir+'/' +img, new_dir4)

#         print(c)
#         c = c +1
#         if c == 20001:
#             break
    
