# using a hashtable to count individual items


# define a set of items that we want to count

x = print(counter)
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
paragraph = paragraph.lower()
paragraph = paragraph.replace(',','')
paragraph = paragraph.replace('.','')
print(paragraph)

words = paragraph.split()
# TODO: create a hashtable object to hold the items and counts
counter = dict()

# TODO: iterate over each item and increment the count for each one
for item in words:
    if(item in counter.keys()):
        counter[item] += 1
    else:
        counter[item] = 1

# print the results
