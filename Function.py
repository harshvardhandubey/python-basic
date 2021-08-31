def printme(str):
	print str
	return

def changeme(mylist):
	mylust=[1,2,3]
	mylist.append(mylust)
	print "Values inside the function: ", mylist
	return


printme("calling first function")
mylist=[10,20,30]
changeme(mylist)

print "list is: ", mylist
