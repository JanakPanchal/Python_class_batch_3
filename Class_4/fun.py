#def

def funname(tNumb):
	for a in range(1,10):
		print("{} * {} = {}".format(tNumb,a, tNumb*a))
		

def fullName(fname,lname):
	return fname+ " "+ lname

print(fullName("Janak","Panchal"))

def concatString(*argv):
	temp = []
	for a in argv:
		temp.append(a)
	return temp

print(concatString("Janak","panchal","Janak@gm.con","8079695030202"))
print(concatString("Janak","panchal"))

#
# x = lambda arg : expresion

x = lambda a : funname(a)
print(x(2))
print(x(5))
print(x(15))