def merge_sort(array):
    n = len(array)
    if n < 2:
        return array
    
    middle = int(n/2)
    # split array into two parts
    left = array[:middle]
    right = array[middle:]

    # call recursively to get individual parts
    a = merge_sort(left)
    b = merge_sort(right)
    
    return merge(a, b)

def merge(a, b):
    # function to merge arrays/lists
    array = []
    while len(a) > 0 and len(b) > 0:
        if a[0] > b[0]:
            array.append(b.pop(0))
        else:
            array.append(a.pop(0))
            
    while len(a) > 0:
        array.append(a.pop(0))
        
    while len(b) > 0:
        array.append(b.pop(0))
    
    return array

in_list = [float(x) for x in input("What is your list for sorting? (space separated numbers please)\n").split()]
# need to add something for dealing with invalid input
#set_list = [1,5,3,2,7,6,6]
sorted_list = merge_sort(in_list)
print("sorted array is:",sorted_list)
