class Myclass:
	def __init__(self):
		print("print init")
	
	@classmethod
	def getname(cls,name):
		return name
	
	@classmethod
	def getsalary(cls,amount):
		return amount