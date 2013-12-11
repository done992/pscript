#-----len()
your_name = "Tom Green"
print("%s 's length is %d" %(your_name, len(your_name)))
city_map = {'shanghai':'shanghai', 'beijing':'beijing', 'hubei':'wuhan', 'shanxi':'xian'}
print("city_map's length = %d" % len(city_map))
color_list = ['red', 'white', 'black', 'blue', 'green']
for x in range(0, len(color_list)):
	print("color_list[%d] = %s" % (x, color_list[x]))

#-----max,min()
str = "s, t, r, i, n, g, S, T, R, I, N, G"
print("max(str) = %s" % (max(str)))
num_list = [4, 9, 5, 1, 2]
print("max(num_list) = %d, min(num_list) = %d" % (max(num_list),min(num_list)))
print(max(100, 50, 1, 23, 45))

guess_this_number = 61
player_guessed = [37, 45, 2, 90]
if max(player_guessed) > guess_this_number:
	print("Boom! you lose")
else:
	print("you win")

#-----range(a, b) range(a, b, step) list()
step_downs = range(40, 10, -2)
print(step_downs)
step_ups =  list(range(0, 100, 2))
print(step_ups)

for x in range(0, 5):
	print(x)

#------sum()
print(sum(step_ups))