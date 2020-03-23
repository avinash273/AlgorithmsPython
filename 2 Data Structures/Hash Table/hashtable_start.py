# TODO: demonstrate hashtable usage


# TODO: create a hashtable all at once
items1 = dict({"key1":1, "key2":2, "key3":"three", "key4":4})

# TODO: create a hashtable progressively
print(items1)

# TODO: try to access a nonexistent key
items2 = {}
items2["key5"] = 5
items2["key6"] = 6
items2["key7"] = 7
items2["key8"] = 8
items2["key9"] = 9

# TODO: replace an item
print(items2["key7"])

# TODO: iterate the keys and values in the dictionary

for key, value in items2.items():
    print(key," : ",value)
