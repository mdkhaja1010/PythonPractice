"""
working with directories
"""
# import os
# print(os.getcwd())
# print(os.path.dirname((os.getcwd())))
# # os.mkdir("sub_directoy")
# os.makedirs("sub1/sub2/sub3")
#os.rmdir("sub_directoy")
# os.removeddirs("sub1/sub2")
# os.remove("path.txt"
#os.rename("sub_directory","renamed_directory")
# print(os.listdir(os.getcwd()))
# print(os.listdir("."))
# for root, dirs, files in os.walk("."):
#     print("Root:",root, "Dirs:", dirs, "Files:", files)
"""
get information of the file
"""
import os,time

f=os.stat("abcd.txt")
print(f.st_size)
print(time.ctime(f.st_mtime))
print(time.ctime(f.st_atime))
print(time.ctime(f.st_ctime))

#pickling(serialization) and unpickling(Deserialiazation)
"""
pickling is the process of serializing a python object into a byte stream for storage or transmission
unpickling is the process of deserializing the byte stream back intoo the original python object allowing for retrieval of its structure and data.
"""


