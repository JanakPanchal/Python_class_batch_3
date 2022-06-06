import os
import time
#r , w , a , x

# AssertionError	Raised when an assert statement fails.
# AttributeError	Raised when attribute assignment or reference fails.
# EOFError	Raised when the input() function hits end-of-file condition.
# FloatingPointError	Raised when a floating point operation fails.
# GeneratorExit	Raise when a generator's close() method is called.
# ImportError	Raised when the imported module is not found.
# IndexError	Raised when the index of a sequence is out of range.
# KeyError	Raised when a key is not found in a dictionary.
# KeyboardInterrupt	Raised when the user hits the interrupt key (Ctrl+C or Delete).
# MemoryError	Raised when an operation runs out of memory.
# NameError	Raised when a variable is not found in local or global scope.
# NotImplementedError	Raised by abstract methods.
# OSError	Raised when system operation causes system related error.
# OverflowError	Raised when the result of an arithmetic operation is too large to be represented.
# ReferenceError	Raised when a weak reference proxy is used to access a garbage collected referent.
# RuntimeError	Raised when an error does not fall under any other category.
# StopIteration	Raised by next() function to indicate that there is no further item to be returned by iterator.
# SyntaxError	Raised by parser when syntax error is encountered.
# IndentationError	Raised when there is incorrect indentation.
# TabError	Raised when indentation consists of inconsistent tabs and spaces.
# SystemError	Raised when interpreter detects internal error.
# SystemExit	Raised by sys.exit() function.
# TypeError	Raised when a function or operation is applied to an object of incorrect type.
# UnboundLocalError	Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.
# UnicodeError	Raised when a Unicode-related encoding or decoding error occurs.
# UnicodeEncodeError	Raised when a Unicode-related error occurs during encoding.
# UnicodeDecodeError	Raised when a Unicode-related error occurs during decoding.
# UnicodeTranslateError	Raised when a Unicode-related error occurs during translating.
# ValueError	Raised when a function gets an argument of correct type but improper value.
# ZeroDivisionError	Raised when the second operand of division or modulo operation is zero.
class FileOpr():
	
	@classmethod
	def readfile(cls,filename):
		with open(filename , "r") as f:
			temp = []
			listoflines = [0,1,3]
			for a, line in enumerate(f):
				if a in listoflines:
					temp.append(line.strip())
				else:
					pass
		f.close()
		return str(temp)
	
	@classmethod
	def writetext(cls,filename,data):
		try:
			with open(filename,"w") as f :
				f.writelines(data)
				f.close()
			return True
		except RuntimeError as error:
			return error
		
	@classmethod
	def appendData(cls,filename,data):
		try:
			with open(filename,"a") as f :
				f.write(data)
				f.close()
			return True
		except RuntimeError as error:
			return error
		
	@classmethod
	def createTxtfile(cls,filename):
		with open(filename , "x") as f:
			f.close()
		return "file is created"
	
	@classmethod
	def deleteTextfile(cls,filename):
		time.sleep(3)
		os.remove(filename)
		return "file is removed"
	

f = FileOpr()
print(f.readfile("abc.txt"))
# print(f.deleteTextfile("name1.txt"))
