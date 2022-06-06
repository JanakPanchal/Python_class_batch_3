from myclass import Myclass

class First():
	fname = ""
	salary = ""
	def __init__(self):
		print("fun is calling ")
		self.fname = Myclass.getname("Janak")
		
	def add_salary(self,salary):
		print("fun is calling salary")
		return "{} is {}".format(self.fname,salary)
	
	
a = First()
print(a.add_salary("10000"))