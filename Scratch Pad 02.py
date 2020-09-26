# Check if parent object's values changes inside a function
data = [1,2,3]
def append_element(some_list, some_element):
    some_list.append(some_element)
append_element(data, 4)
print(data) # Yes, parent object altered

# Check if an object is of int instance
a = 5
print(isinstance(a, int)) #Yes, a is an instance of int type

a = 'foo'
print(a.count('o')

# getattr
a = 'foo'
getattr(a, 'capitalize')

# is iterable function
def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

isiterable('foo')
isiterable([1, 2, 3])
isiterable(5)