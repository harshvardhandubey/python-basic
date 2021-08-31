fo = open("foo.txt","wb")

print "Name of File", fo.name
print "Is Closed", fo.closed
print "Mode:", fo.mode
print "Softspace flag", fo.softspace

fo.close()
print "Closed or not :", fo.closed

fo = open("foo.txt","w+")
fo.write("Python")
fo.close()

fo = open("foo.txt","r")
file_data = fo.read()
print "Data ", file_data
fo.close() 
