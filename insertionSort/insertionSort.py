def insertionSort(numbers):
    ' Starting at index 1 because the first index (0) has nothing to compare to on its left '
    index_length = range(1, len(numbers))

    ' loop through each item in the list of numbers '
    for item in index_length:
        value_to_sort = numbers[item]

    '''
     If the value to the left is higher than the current value then... 
     Also need to check that the item is >0 because -ve indexing is allowed
     '''
    while numbers[item-1] > value_to_sort and item>0:
            '...swap the  values'
            numbers[item], numbers[item-1] = numbers[item-1], numbers[item]
            ' incrementing down the list '
            item -= 1

    return numbers

print (insertionSort([5,6,2,2,13,5,35,35,15,26,36,236,1,61,36,6]))

