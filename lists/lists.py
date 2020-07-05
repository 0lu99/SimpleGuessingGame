'''
*************************************************************
Lists are a collection of ordered and changeable items.
They allow for duplicate members
*************************************************************
'''

names = ["Jim", "Timmy", "Arthur", "Mary", "Jane"]
numbers = [3, 1, 2, 5, 4]

'''
This will print out everything in the list 
Output: ['Jim', 'Timmy', 'Arthur', 'Mary', 'Jane']
'''
print(names)


'''
This will print the value held at the given index 
Output: Timmy
'''
print(names[1])

'''
Negative indexing will print out items beginning from the end
Output: Mary
'''
print(names[-2])


'''
This will print the range of values within the disclosed indices 
Output: ['Jim', 'Timmy', 'Arthur']
'''
print(names[0:3])


'''
This will replace the value held within that index
Output: Olu 
'''
names[2] = "Olu"
print(names[2])

'''
To sort a list in alphabetical or numerical order, the sort method can be used
Output: ['Jane', 'Jim', 'Mary', 'Olu', 'Timmy']
        [1, 2, 3, 4, 5]
'''
names.sort()
numbers.sort()
print(names)
print(numbers)


'''
The extend method will add lists together
Output: ['Jim', 'Timmy', 'Olu', 'Mary', 'Jane', 1, 2, 3, 4, 5]
'''
names.extend(numbers)
print(names)


'''
The append method will add another item to the END of a list
Output: ['Jim', 'Timmy', 'Olu', 'Mary', 'Jane', 1, 2, 3, 4, 5, 'Christopher']
'''
names.append("Christopher")
print(names)


'''
The insert method will allow you to insert an item at a specified index
and will shift everything else to thr right
Output: ['Chris', 'Jim', 'Timmy', 'Olu', 'Mary', 'Jane', 1, 2, 3, 4, 5, 'Christopher']
'''
names.insert(0, "Chris")
print(names)


'''
The remove method will remove an item from the list
Output: ['Chris', 'Jim', 'Timmy', 'Olu', 'Mary', 'Jane', 1, 2, 3, 4, 5]
'''
names.remove("Christopher")
print(names)


'''
The pop method removes the last item in the list
Output: ['Chris', 'Jim', 'Timmy', 'Olu', 'Mary', 'Jane', 1, 2, 3, 4]
'''
names.pop()
print(names)


'''
To figure out the index value of an item in a list you can use this
Output: 4
'''
print(names.index("Olu"))

'''
A copy method will take a copy of a list and store it
['Chris', 'Jane', 'Jim', 'Mary', 'Olu', 'Timmy', 1, 2, 3, 4]
'''
names2 = names.copy()
print(names2)


'''
The clear method will remove everything within a list
Output: []
'''
names.clear()
print(names)

