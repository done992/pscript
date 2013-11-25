params = {"host":"node1", "port":"8888", "uid":"tom", "passwd":"secret"}
print ["%s=%s" %(k,v) for k,v in params.items()]
print ";".join(["%s=%s" %(k,v) for k,v in params.items()])

mylist = ['host=node1', 'port=8888', 'uid=tom', 'passwd=secret']
mystr = ";".join(mylist);
print mystr
splitedlist = mystr.split(";");
print splitedlist
print mystr.split(";", 1)
