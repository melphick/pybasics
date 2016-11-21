#!/usr/bin/python
...
A function that returns the multiplication product of three parameters--x, y,
and z has a default value of 1.
a. Call the function with all positional arguments.
b. Call the function with all named arguments.  
c. Call the function with a mix of positional and named arguments.
d. Call the function with only two arguments and use the default value for z.
...

def multiply(x,y,z=1):
    return x*y*z


print "Call the function with all positional arguments."

print multiply(10,5,2)

print "Call the function with all named arguments."

print multiply(x=10,y=5,z=2)

print "Call the function with a mix of positional and named arguments."

print multiply(5,y=2,z=10)

print "Call the function with only two arguments and use the default value for z."

print multiply(x=10,y=5)
