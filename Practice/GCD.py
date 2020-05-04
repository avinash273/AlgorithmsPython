def GCD_Recursive(a, b):
    if b == 0:
        return a
    return GCD_Recursive(b, a % b)


def GCD_Loop(a, b):
    while b != 0:
        temp = a
        a = b
        b = temp % b
    return a


print(GCD_Recursive(20, 8))
print(GCD_Recursive(60, 96))
print(GCD_Loop(20, 8))
print(GCD_Loop(60, 96))
