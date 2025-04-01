# Try fails then except
try:
  print(x)
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")



# Try works then else
try:
  print("hello")
except:
  print("Hello Print Went wrong")
else:
  print("Nothing went wrong")


y = "hello"

if not type(y) is int:
  print("Y is not integer")  
  raise TypeError("Only integers are allowed") 