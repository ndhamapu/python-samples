x1 = complex(1j)
x2 = list(("apple", "banana", "cherry"))
x3 = tuple(("apple", "banana", "cherry"))
x4 = range(6)
x5 = dict(name="John", age=36)
x6 = set(("apple", "banana", "cherry"))
x7 = frozenset(("apple", "banana", "cherry"))
x8 = bool(5)
x9 = bytes(5)
x10 = bytearray(5)
x11 = memoryview(bytes(5))
x12 = str("Hello World")
x13 = int(20)
x14 = float(20.5)


for count in range(1, 15):

    concatedName = f"x{count}"
    print(" Variable Name= " + concatedName)
    # Get the actual variable value
    concated_variable_value = globals().get(concatedName)
    if concated_variable_value is not None:
        print(f"{concatedName} is of type {type(concated_variable_value)}")


