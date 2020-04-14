from itertools import permutations


def palindrome_permutation(str1):
    str1 = str1.lower()
    str1 = str1.replace(" ", "")
    print(str1)
    str_permu = []

    for each in list(permutations(str1)):
        str_permu.append("".join(each))

    for each in str_permu:
        if each == each[::-1]:
            return True
    return False


print(palindrome_permutation("Tact Coa"))
print(palindrome_permutation("Mala yalam"))
print(palindrome_permutation("Av aii"))
