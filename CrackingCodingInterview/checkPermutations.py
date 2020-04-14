from itertools import permutations


def contains(s, other):
    return s.__contains__(other)


def check_permutations(str1, str2):
    if len(str1) is not len(str2):
        return False
    else:
        str1_permut = permutations(str1)
        newone = []
        for perm in list(str1_permut):
            newone.append(''.join(perm))
        print(newone)
        for each in newone:
            if (contains(each, str2)):
                return True
        return False


print(check_permutations("abc", "cba"))
# print(permutations_check("avinash", "cat"))
# print(permutations_check("avi", "avinash"))
