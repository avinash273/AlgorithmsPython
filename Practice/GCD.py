def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)

print(GCD(60, 96))