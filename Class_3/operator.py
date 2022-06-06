# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators


# Arithmetic operators
# + , - , * , / , % ,  **  , //

print(5+2)
print(5 * 10)

for i in range(1,10):
	print(" 5  *  {} = {}".format( i ,5 * i))
	
for i in range(1,10):
	print(" 50  -  {} = {}".format( i ,50 - i))
	
# Assignment operators
# = , += , -=  , *= , /= , %= , **= , &=

counter = 0
fatchby = counter

a,b = 4,8
print(counter)
print(a)
print(b)
print("---------------")
count = 10
count = count + 1
print(count)
count += 10
print(count)
count -= 5
print(count)
count *= 5
print(count)



# Comparison operators
#== , < , > , >=, <= , !=
num = 10
num2 = 20
num3 = 10
print(num == num2)
print(num < num2)
print(num > num2)
print(num != num3)


# Logical operators
# and , or , not
#both condition should be true
print("------Logical operators -------")
print(num  == num3 and num2 > num and num3 != num2)
#either any of the condition is true it will return true
print(num != num3 or num2 == num3)
print(num  == num3 != num2 > num )



# Identity operators
# is , not is
print("----# Identity operators ----")
name = ["Janak", "Abhay"]
name2 = name
name3 = name2
print(name2 is name)
print(name3 is name2)
print(name3 is not name)



# Membership operators
# in , not in
print("=======Membership operators =======")
list = [ 10 , 20 ,30 , 40 , 50]
print(100 in list)
print(50 not in list)