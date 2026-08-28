def selection_sort(list):
    cur = 0 
    end = len(list) - 1

    while cur <= end:
        temp = list[cur:]
        for index, item in enumerate(temp):
            if list[cur] > temp[index]:
                list[cur], list[index + cur] = temp[index], list[cur]
        cur += 1

    return list

print(selection_sort([33, 1, 89, 2, 67, 245]))
print(selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3]))
print(selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]))