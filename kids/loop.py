mylist = [0, 1, 2, 3, 4, 5]
print(mylist[2:5])

for x in range(0,5):
	print("hello, %d" %x)


wizard = ['apple', 'green orange', 'egg', 'tomato']
for x in wizard:
	print(x)

x = 40
y = 70
while x < 45 and y < 80:
	x = x + 1
	y = y + 1
	print("x = %d, y = %d" %(x, y))

while True:
	x = x + 1
	if (x == 50):
		break
	print("x = %d" %x)