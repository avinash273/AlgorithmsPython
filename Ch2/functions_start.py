#
# Example file for working with functions
#

# define a basic function
def fun1():
    print("I am preparing for amazon")
    return 0;


# function that takes arguments
def fun2(arg1, arg2):
    print(arg1, " ", arg2)


# function that returns a value
def cube(x):
    return x * x * x;


# function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        print("value of i: ", i)
        result = result * num
    return result


# function with variable number of arguments
def multiAdd(*args):
    result = 0
    for x in args:
        result = result + x
    return result


fun1()
fun2(2, 20)
print(power(10,5))
print(multiAdd(1, 2, 3))
