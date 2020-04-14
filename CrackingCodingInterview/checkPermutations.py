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
        for each in newone:
            if (contains(each, str2)):
                return True
        return False

def check_permutations2(str1, str2):
    if len(str1) is not len(str2):
        return False
    else:
        sort_str1 = sorted(str1)
        sort_str2 = sorted(str2)
        str1f = "".join(sort_str1)
        str2f = "".join(sort_str2)

        if str1f == str2f:
            print(str1f, str2f)
            return True
        else:
            return False


print(check_permutations2("abc", "cba"))
print(check_permutations2("avinash", "cat"))
print(check_permutations2("nashavi", "avinash"))
