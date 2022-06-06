def checknumber(func):
	def inner1(*args):
		if type(args[0]).__name__ == "int" == type(args[1]).__name__ == "int":
			returnval = func(*args)
			returnval *= 100
			return returnval
		else:
			return "error"
	return inner1
	
	
@checknumber
def add(num,num2):
	return num * num2
# class A:
#
	# @classmethod
	# def add(self,num,num2):
	# 	return num + num2
	#
	#
	# @classmethod
	# def add(self,num,num2):
	# 	return num * num2

	
print("{}".format(add("20",10)))