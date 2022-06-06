#try
#except
#finally


# try:
# 	#
# 	#
# 	#
# 	#
# except:
# 	#
# 	#
# 	#
# finally:
# 	###
import os
try:
	with open("./name.txt") as f:
		line = f.readline()
	print(line)
except:
	print("file can't be readble")
finally:
	print("running")
	f.close()

