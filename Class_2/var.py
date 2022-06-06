# string , int , float , double , list , dict , tuple , set
name = "Janak"
print(name)
print(type(name))

count = 10
print(count)
print(type(count))

count1 = 100.1
print(count1)
print(type(count1))

list = ["Janak Panchal" , 22 , "Mumbai", 20000000 , 10.10]
print(list)
print(type(list))

student = dict(
	name = "janak",
	location = "Mumbai",
	age = 20
)
print(student)
print(type(student))
print(student["name"])
print((student["location"]))

example_of_tuple = (
	["10" , 100.1 , "hello", 10],
	dict(
	name = "janak",
	age = 20,
	hometown = "Mumbai"
), "10")

print(type(example_of_tuple))
print(example_of_tuple)

example_of_set = {"Janak" ,"Rohan", "Raj","Roy", "Raj ", "Bob", "Amitab" , "Janak"}
print(example_of_set)
#print(set(example_of_set))