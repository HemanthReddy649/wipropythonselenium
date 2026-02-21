#Destructors - when we want to destroy the object
#post conditions - closing of the browser
#clean up operations
#for proper memory usage destructors should be used
#when db connection has to be closed
#when db connection has to be closed
#free the memory(garbage collection which automatically called


class Desct:

    def __init__(self):
        print("Object Created")

    def __del__(self):
        print("closing the db connection")

a=Desct()
print("End of the program")
del a

#desct in file handling

class FileHandler:
    def __init__(self,filename):
        self.file=open(filename,"w")
        print("File is opened")

    def readfile(self,filename):
        print("reading the file")

    def __del__(self):
        self.file.close()
        print("file closed")
f=FileHandler("test.txt")
f.readfile("test.txt")
del f
