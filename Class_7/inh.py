# class BaseClass():
# 	#body of class
#
# class DerivedClass(BaseClass):
# 	#body of DerivedClass


# class BaseClass():
# 	#body of class
# class DerivedClass(BaseClass):
# 	#body of DerivedClass
# class SubDerivedClass(DerivedClass):
#   #body of SubDerivedClass
#this is the command
#this is new command

class Customer():
	CID = [101,102,103]
	LOANID = [101,102]
	
	def __init__(self, cid):
		self.cid = cid
		
	@classmethod
	def SavingAccount(cls,cid):
		if cid in cls.CID:
			return 20000
		else:
			return None
		
	@classmethod
	def IsLoanPresent(cls,cid):
		# Value  if codition  else value
		return True if cid in cls.LOANID else False
	
	@classmethod
	def InterstValue(cls,AccountType,cid):
		if AccountType == "Saving":
			return 4.10
		else:
			return None
		
		
class LoanDept(Customer):
	
	def __init__(self):
		Customer.__init__(self,101)
		
	def LoanMothlyIntAmount(self,cid, amount):
		if Customer.IsLoanPresent(cid) == True:
			return 10000 * 100 / 720
		else:
			return amount * 100 / 720
			

class CreditScore(LoanDept):
	def IsCustomerEq(self,cid,amount):
		#is loan is present after check balanace > someamt
		if LoanDept.IsLoanPresent(cid) != True:
			if LoanDept.SavingAccount(cid) > 5000:
				return dict(
					IsEligible = True,
					IntAmount = LoanDept.LoanMothlyIntAmount(self,cid,amount)
				)
		else:
			return None


c = CreditScore()
print(c.IsCustomerEq(103,5000))