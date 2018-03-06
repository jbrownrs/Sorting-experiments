def bubbleSort(input):
    length = len(input)
    # Sort list to length - 1 as comparing one number with next
    # will go off the end of the list otherwise
    sortTo = length-1
    sorted = False

    while sorted != True :
        sorted = True
        # Go through the list until it is sorted, moving
        # the biggest unsorted number to its final position
        for x in range(0, sortTo) :
            # swap numbers if left number is bigger
            # than right number
            if input[x] > input[x+1] :
                input[x],input[x+1] = input[x+1],input[x]
                sorted = False
        sortTo = sortTo - 1
    return input
