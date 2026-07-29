def quick_sort(integers):
    if len(integers) == 0:
        return []
    if len(integers) == 1:
        return integers

    pivot = integers[0]

    less = []
    equal = []
    greater = []

    for i in integers:
        if i < pivot:
            less.append(i)
        if i > pivot:
            greater.append(i)
        if i == pivot:
            equal.append(i)

    less = quick_sort(less)
    greater = quick_sort(greater)

    full_list = less + equal + greater
    return full_list

print(quick_sort([]))
print(quick_sort([20, 3, 14, 1, 5]))
print(quick_sort([83, 4, 24, 2]))
print(quick_sort([4, 42, 16, 23, 15, 8]))
print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]))