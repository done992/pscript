fd_r = open("/Users/caoj7/zk/loop.py")
text = fd_r.read()
print(text)

fd_w = open("copy.py", "w")
fd_w.write(text)
fd_w.close()

fd_r2 = open("copy.py")
text_r2 = fd_r2.read()
print(text_r2)

