def insertion_sort(alist):
    n = len(alist)
    for i in range(1,n):
        unsorted_value = alist[i]
        j = i - 1
        while j >= 0 and alist[j] > unsorted_value:
            alist[j+1] = alist[j]
            j -= 1
        alist[j+1] = unsorted_value
    return alist


set_list = [3,5,2,6]
sorted_list = insertion_sort(set_list)
print("Sorted list is:",sorted_list)

