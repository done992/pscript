import sys
#----abs()
a = -10
print(abs(a))

if abs(a) > 0:
	print("moving...")

#----bool()
rc = None
print(bool(0))
print(bool(rc))
print(bool(""))
print(bool(''))

print(bool(-500))

mylist = []
print("bool(mylist) = %s" % bool(mylist))
#----input()
year = input("input the year of your birth:")
if not bool(year):
	print("you need to enter value for your year of birth")

#----dir()
print(dir(['a', 'root', '/usr']))
print(dir(1))

str = 'I love U'
print(dir(str))

#print(help(str.upper))
#----upper()
print(str.upper())

#-----eval
input_str = input("input your calculation (e.g., '3*5'):")
print(eval(input_str))

#-----exec
two_cmds = '''print('hello, ')
print('world!')'''
exec(two_cmds)

#-----float
age = input("input your age:")
f_age = float(age)
print(f_age)
if f_age > 33:
	print("you are older than me about %s years" % (f_age - 33))
else:
	print("you are yonger than me about %s years" % (33 - f_age))


#-------int()
pi = 3.14
year_str = "2014"
print(int(pi))
print(int(year_str))





