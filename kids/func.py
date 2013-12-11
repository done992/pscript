mylist = range(3,10)
print(mylist)

def print_name(fname,lname):
	print("hello, %s, %s" %(fname, lname))

def get_max(a, b):
	if a > b:
		return a
	else:
		return b


print_name("Bill", "Gates")
print(get_max(4, 3))


#---------------------
import time
print(time.asctime())

import sys
print("please input your name:")
line = sys.stdin.readline()
print(line)

#about sys.stdin.readline
print("please input your age")
age = sys.stdin.readline()
if age > 10 and age < 80:
	print("it is difficult for me!")
else: 
	print("hur?")



