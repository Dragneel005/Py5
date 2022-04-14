#def myinput()
y = lambda x,z :z>x
u = lambda x,z : x if x>y else y
print(y(11,10))
print(u(11,10))