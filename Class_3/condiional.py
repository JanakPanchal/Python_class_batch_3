#if


name = "Janak"
if name == "Janak":
	print("TRUE")

#if else

if name != "Janak":
	print("TRUE")
else:
	print("FALSE")

#if elif elif else

if name == "Rohan":
	print("C1")
elif name == "Komal":
	print("C2")
elif name == "Janak":
	print("C3")
else:
	print("False")


#
# def f(x):
#     match x:
#         case 'a':
#             return 1
#         case 'b':
#             return 2
#         case _:
#             return 0

def f(x):
    return {'a': 1, 'b': 2,"c": 10}.get(x , "def")
print(f("z"))
	
			

