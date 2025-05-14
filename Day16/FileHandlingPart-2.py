"""
part-1 recap
file handling in python-2
Types of files
opening a file
closing a file
various properties of a file
different modes of files(w,r,a)
Read data from a file
write data to a file
append data to a file
-------
seek and tell methods
---------------
seek--> move cursor to a specific location or index
tell--> return where the location of cursor is
by default first character will be 0 as a index number
To avoid reduntant processing--> efficiently reading large files
log monitoring, downloads, video streaming, file-based API's
"""
f=open("abc.txt","r")
print(f.tell())
print(f.read(2))
print(f.tell())
print(f.seek(0))
f.close()
