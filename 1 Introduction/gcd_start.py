# Find the greatest common denominator of two numbers
# using Euclid's algorithm


def gcdRecursive(a, b):
    if(b == 0):
        return a
    return gcd(b, a%b)

def gcd(a, b):
    while b != 0:
        t = a
        a = b
        b = t % b
    return a



        
# try out the function with a few examples
print("While ", gcd(60, 96))  # should be 12
print("While ",gcd(20, 8))   # should be 4

print("Recursive ",gcdRecursive(60, 96))  # should be 12
print("Recursive ",gcdRecursive(20, 8))   # should be 4