#File Handling in python
'''
programming requirement--> store our data for future purpose --> files --> common permanant storage areas
Data Driven Testing--> Test Data --> txt, json, excel files, csv files, etc
Types of files
text files--> stores character data
.txt,.csv,.excel etc
binary files--> store binary data
video, audio, images etc

Open a file-->
 in built function open()
    f=open(filename,mode)
mode--> r, w, a read, write, append
r+--> read and write
w+--> write and read
a+--> append and read

Close a file-->
  in builf function close()
  f.close()
it is always recommeded to close the file otherwise will get the data corrupted

Various properties a file
name of the file
mode
closed
readable()
writable()

'''
# f=open("file1.txt","w")
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.write("this is the testing")
# f.close()
# print(f.closed)
#Write data to a file
"""
write("str")
writelines(list of lines)
when we try to open the file in w mode --> data will overridden
"""
f=open("file1.txt", "w")
f.write("Learning\n")
f.write("python\n")
f.write("is very easy\n")
list=["sunny\n","chinny\n","bunny\n","vinny\n"]
f.writelines(list)

f.close()
# Read Data from a file
"""
read()--> read total data from a file
read(n)--> only specific characters from the file
readline()--> Read only one line
readlines()--> read all lines into list
"""
f=open("file1.txt","r")
#s=f.read()
#print(s)
#print(f.read(10))
# line1=f.readline()
# print(line1)
# line2=f.readline()
# print(line2)
# line3=f.readline()
# print(line3)
lines=f.readlines()
# for line in lines:
#     print(line.strip())
# last_line=lines[-10:]
# for line in last_line:
#     print(line)
#
# lines[:10]
# lines[5:10]
#----------------
#context manager or with statement
"""
To close a file automatically once perform operation we can go for context manager
"""
with open("file1.txt","w") as x:
    x.write("file\n")
    x.write("handling\n")
    x.write("session")
    print(x.closed)
print(x.closed)
# check a particular file is existed or not
"""
os.path.exists(file_path)--> checks both files and directories
os.path.isfile(file_path)--> checks only files
pathlib.path(file_path).exists--> recommended for python 3.4+
checks both files and directories we need to import from pathlib from pathlib import path

Sys module vs os module
--------------------
Os is like windows file explorer - we can create/delete folders, open files, and run system programs

sys is like python's control panel--> it helps python understand its environment and control script execution.
"""
#check file existance
import os
from pathlib import Path
filepath=r"C:\Users\moham\PycharmProjects\PythonProject\pythonSeleniumDemo\Day15\file1.txt"
# os.path.isfile("C:\Users\moham\PycharmProjects\PythonProject\pythonSeleniumDemo\Day15\//file1.txt")
os.path.isfile("C:\\Users\\moham\\PycharmProjects\\PythonProject\\pythonSeleniumDemo\\Day15\\file1.txt")
os.path.exists("C:\\Users\\moham\\PycharmProjects\\PythonProject\\pythonSeleniumDemo\\Day15\\file1.txt")
Path.exists(r"C:\Users\moham\PycharmProjects\PythonProject\pythonSeleniumDemo\Day15\file1.txt")
# append the data from the file
# f=open("file1.txt", "a")
# f.write("Learning\n")
# f.write("python\n")
# f.write("is very easy\n")
# list=["sunny\n","chinny\n","bunny\n","vinny\n"]
# f.writelines(list)
#
# f.close()