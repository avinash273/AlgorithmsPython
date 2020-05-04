itemsa = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

hashtable = dict()
listval = []
for each in itemsa:
    hashtable[each] = 0

for item in hashtable:
    print(item)

print(set(hashtable.keys()))
# print(listval)
