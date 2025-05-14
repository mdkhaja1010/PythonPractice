"""
different modes of files
  Text files--> r,w, a, r+,w+, a+
  Binary Files--> rb, wb, ab, r+b, w+b, a+b
if we want to read the data file must exist
if we want to write the data--> if file does not exists then is created automatically
"""
f1=open("download.jpeg","rb")
#print(f1.read())
bytes=f1.read()
f2=open("newimage.jpg","wb")
f2.write(bytes)
f1.close()
f2.close()

#zipping and unzipping
"""
why we need to zip
     save memory by reducing size
     Transfer the file fastly
     Improve performance
zipfile--> module --> zipfile class to require to zip and unzip the files
Types of compression(zipping)
------------------
ZIP_DEFLATED--> with compression

ZIP_STORED--> without compression --> default value for compression parameter

"""
from zipfile import ZipFile, ZIP_DEFLATED, ZIP_STORED
with open("abcd.txt","w") as f:
    f.write("this is test file\n"*100)
# with ZipFile("no_compression.zip","w",compression=ZIP_STORED) as k:
#     k.write("abcd.txt")
# with ZipFile("with_compression.zip","w",compression=ZIP_DEFLATED) as k:
#     k.write("abcd.txt")

with ZipFile("with_compression.zip","w") as k:
    print(k.namelist())
    k.extractall("unzippedfile")
    k.extract("abce2.txt","filename folder")



