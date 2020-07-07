def bubblSort(numbers):

    ' Infinite loop until list is sorted'
    while True:
        corrected_list = False
        ' -1 because I compare the penultimate to last item'
        for item in range(0,len(numbers) -1):
            ' If the current item is greater than the next item...'
            if numbers[item] > numbers[item + 1]:
                ' ...swap the items'
                numbers[item], numbers[item+1] = numbers[item+1], numbers[item]
                corrected_list = True
        ' "not" is a logical operator that flips the value'
        if not corrected_list:
            return numbers

print(bubblSort([1, 3, 4, 7, 8, 2]))
print(bubblSort([1, 3, 42, 7, 3, 20]))
print(bubblSort([0, 3, 41, 27, 8, 2]))