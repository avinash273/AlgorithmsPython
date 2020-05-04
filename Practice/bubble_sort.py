copyright()
def bubble_sort(array):
    # for i in range(len(array) -1):
    #     for j in range(i):
    #         if (array[j] < array[j+1]):
    #             temp = array[j]
    #             array[j] = array[j+1]
    #             array[j+1] = temp
    #     print(array)
    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
            # print(array)
    return array

array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(bubble_sort(array))
