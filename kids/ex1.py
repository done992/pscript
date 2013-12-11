foods = ['noodle', 'rice', 'meat']
hobbies = ['reading', 'swimming', 'programming']
favorites = foods + hobbies
print(favorites)

buildings = 3
renzhe = 25
tunnel = 2
wushi = 40
print('%d renzhes and %d wushis are going to battle.' %(buildings * renzhe, tunnel * wushi))

firstname = 'Tom'
lastname = 'Green'
print('Good morning, %s %s' % (firstname, lastname))

mpirun -mca ras yarn -mca plm yarn -mca state yarn -mca odls yarn --verbose --np 4 /Users/caoj7/program/mpi/hello