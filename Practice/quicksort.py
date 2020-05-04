items = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def quickSort(dataset, first, last):
    if first < last:
        pivotIdx = partition(dataset, first, last)

        quickSort(dataset, first, pivotIdx - 1)
        quickSort(dataset, pivotIdx + 1, last)
    return dataset


def partition(dataValues, first, last):
    pivotValue = dataValues[first]

    lower = first + 1
    upper = last

    done = False

    while not done:
        while lower <= upper and dataValues[lower] <= pivotValue:
            lower += 1

        while upper >= lower and dataValues[upper] >= pivotValue:
            upper -= 1

        if upper < lower:
            done = True
        else:
            temp = dataValues[lower]
            dataValues[lower] = dataValues[upper]
            dataValues[upper] = temp

    temp = dataValues[first]
    dataValues[first] = dataValues[upper]
    dataValues[upper] = temp

    return upper


print(items)
print(quickSort(items, 0, len(items) - 1))
