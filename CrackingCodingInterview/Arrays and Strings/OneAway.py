def oneAway(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)
    tolerance = 0
    i = 0
    j = 0
    if (str1_len == str2_len) or (str1_len == str2_len - 1) or (str1_len == str2_len + 1):
        while i < str1_len and j < str2_len:
            #print(str1[i],str2[j])
            if str1[i] != str2[j]:
                tolerance += 1
            if str1_len == str2_len:
                i += 1
                j += 1
            if str1_len == str2_len - 1:
                j += 1
            if str1_len == str2_len + 1:
                i += 1

        if tolerance <= 1:
            return True
        else:
            return False
    else:
        return False


print(oneAway("pale", "ple"))
# print(oneAway("pales", "pale"))
# print(oneAway("pale", "kale"))
# print(oneAway("pale", "bae"))
