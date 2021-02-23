# is sebagai komparasi object identity
print('=====object identity(is)====')
x = 5 #ini adalah assignment membuat object
y = 5
print('niliai x =',x,',id = ',hex(id(x)))
print('niliai y =',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)
