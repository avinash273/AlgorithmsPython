def string_compression(str1):
    result =""
    count = 1
    i = 0
    j = 0
    str1_len = len(str1)

    while i < str1_len and j < str1_len - 1:
        j = i + 1
        #print("str1[i]: ",str1[i], "str2[i]: ",str1[j])
        if str1[i] == str1[j]:
            count += 1
            i += 1
        else:
            result = result + str1[i] + str(count)
            #print(result)
            count = 1
            i += 1
    result = result + str1[i] + str(count)
    return result


print(string_compression("aabcccccaaa"))