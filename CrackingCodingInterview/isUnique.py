def isUnique(str1):
    """
    complexity
    Time: O(2n)
    Space: O(1)
    :param str1:
    :return:
    """
    str1 = sorted(str1)
    print(str1)

    for i in range(len(str1)-1):
        if str1[i] == str1[i + 1]:
            return False
    return True


print(isUnique("uoaieau"))
print(isUnique("asdfghjkl"))