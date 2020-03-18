# 
# Example file for variables
#
f = 0
print(f)
# Declare a variable and initialize it
f = 'abc'
print(f)

# # re-declaring the variable works
print("this is string " + f + str(123))

# # ERROR: variables of different types cannot be combined


# Global vs. local variables in functions
def someFunction():
    global f
    f = 'def'
    print(f)

someFunction()
print(f)
del(f)
print(f)