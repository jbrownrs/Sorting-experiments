'''
Implements quicksort as per the Lomuto partition
scheme using the last value as the pivot
'''
def quicksort(alist):
    quicksort_main(alist, 0, len(alist)-1)

def quicksort_main(alist, lo, high):
    if lo < high:
        split_point = partition(alist, lo, high)
        # split into two separate lists
        # then run quicksort on these lists
        #print('split_point',split_point)
        sortleft = quicksort_main(alist,lo, split_point-1)
        #print('sort left',sortleft)
        sortright = quicksort_main(alist,split_point+1, high)
        #print('sort right',sortright)  
    #return sortleft + sortright

def partition(alist, lo, high):
    # use last index as pivot value i.e. high
    pivot_value = alist[high]
    for i in range(lo,high):
        # for all the elements before the pivot
        # we want to reorder them so that those
        # less than pivot are to the left of where the pivot will end
        # and those greater than the pivot are to the right of where pivot will end
        if alist[i] < pivot_value:
            alist[i],alist[lo] = alist[lo],alist[i]
            lo += 1
        #print('lo value is...',lo)
    alist[lo],alist[high] = alist[high],alist[lo]
    return lo

set_list = [2,7,4,5,1]
set_list_1 = [5,2,3,7,4]
quicksort(set_list)
print("Sorted list is:",set_list)
