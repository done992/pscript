mylist = [1, 2, 3, 4]
print mylist
print [elem*2 for elem in mylist]
print mylist
mylist = [elem*3 for elem in mylist]
print mylist

print "------------------------"
params = {"host":"node1", "port":"8888", "uid":"jimmy", "passwd":"secret"}
print params.keys()
print params.values()
print params.items()
print [k for k, v  in params.items()]
print [v for k, v  in params.items()]
print ["%s=%s" %(k, v) for k, v  in params.items()]
