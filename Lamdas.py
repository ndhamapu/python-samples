# lambda arguments : expression

x = lambda a, b : a * b
print(x(5, 6))


# this function is returning a lambda funcion so here value if n is set
def myfunc(n):
   return lambda a : a * n

# mydoubler  is like lambda a:a*2
mydoubler = myfunc(2)
mytripler = myfunc(3)

# here the value of a is set
print(mydoubler(11))
print(mytripler(11))