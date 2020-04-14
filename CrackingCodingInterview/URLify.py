def URLify(str1, true_length):
    fin_str = []
    for i in range(true_length):
        if str1[i] == ' ':
            fin_str.append('%20')
        else:
            fin_str.append(str1[i])
    return "".join(fin_str)

result = URLify("Hi I am avinash shanker    ",23)
print(result)


