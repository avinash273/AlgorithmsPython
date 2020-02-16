#code to find the GCD of two numbers

def GCD(a, b):
    if(b == 0):
        return a
    return GCD(b,a%b)

print(GCD(20,8))