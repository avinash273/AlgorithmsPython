# Todo recursive merge sorting
# Todo This algorithm has a complexity of O(n log n)
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def mergesort(dataset):
    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        mergesort(leftarr)
        mergesort(rightarr)

        # Todo merging operation
        i = 0  # index into left array
        j = 0  # index into right array
        k = 0  # index into merged array

        # todo while both arrays have content
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else:
                dataset[k] = rightarr[j]
                j += 1
            k += 1

        # todo if left array still has values
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1
        # todo if right array still has values
        while j < len(rightarr):
            dataset[k] = rightarr[j]
            i += 1
            k += 1
    return dataset

print(items)
print(mergesort(items))
