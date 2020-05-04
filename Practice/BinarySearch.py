items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def BinarySearch(item, dataset):
    listSize = len(dataset) - 1
    lowerIdx = 0
    upperIdx = listSize

    while lowerIdx <= upperIdx:
        mid = (lowerIdx + upperIdx) // 2

        if dataset[mid] == item:
            return mid

        if item > dataset[mid]:
            lowerIdx = mid + 1
        else:
            upperIdx = mid - 1

    if lowerIdx > upperIdx:
        return None

print(BinarySearch(10, items))
