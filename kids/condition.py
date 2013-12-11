age = 20
if age >= 20:
	print("you are too old")
else:
	print("your age is less than 20")

name = "tom"
if name == "tom":
	print("a pig fell in the mud")
else: 
	print("you are not tom")


money = 50
if money < 50:
	print("money < 50")
elif money == 50:
	print("money == 50")
else:
	print("money > 50")


member = 40
if member >= 30 and member <= 50:
	print("larger than 30, and less than 50")
elif member < 10 or member > 90:
	print("less than 10 or larger than 90")
else:
	print("10<=x<30 or 50<x<=90")

val = None
if val == None:
	print("val == None")