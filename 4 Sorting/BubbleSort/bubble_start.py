# Bubble sort algorithm


def bubbleSort(dataset):
    # TODO: start with the array length and decrement each time
    for i in range(len(dataset)):
        for j in range(len(dataset)):
            if(dataset[i] < dataset[j]):
                temp = dataset[i]
                dataset[i] = dataset[j]
                dataset[j] = temp
        print("Current state: ", dataset)
    return dataset


def main():
    list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    bubbleSort(list1)
    print("Result: ", list1)


if __name__ == "__main__":
    main()
