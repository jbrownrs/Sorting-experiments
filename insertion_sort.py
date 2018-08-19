def insertion_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    for i in range(1,n):
        # go through list (left to right)
        # using the first unsorted index
        unsorted_value = alist[i]
        j = i - 1
        while j >= 0 and alist[j] > unsorted_value:
            # if sorted value is greater than unsorted
            # shift the sorted value to the right and
            # select next comparison value as next to left
            alist[j+1] = alist[j]
            j -= 1
        # place the 'unsorted' value in position now that it has
        # gone along until it is the bigger than the sorted value
        alist[j+1] = unsorted_value
    return alist


set_list = [3, 4,1,6,8,4]
sorted_list = insertion_sort(set_list)
print("Sorted list is:",sorted_list)

