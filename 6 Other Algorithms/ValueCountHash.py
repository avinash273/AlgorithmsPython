Fruits = ["apple", "pear", "orange", "banana", "apple",
          "orange", "apple", "pear", "banana", "orange",
          "apple", "kiwi", "pear", "apple", "orange"]

counter = dict()

for item in Fruits:
    if item in counter.keys():
        counter[item] += 1
    else:
        counter[item] = 1

print(counter)

# https://www.linkedin.com/learning/programming-foundations-design-patterns-2/don-t-reinvent-the-wheel?u=56687537
# dummy commit
