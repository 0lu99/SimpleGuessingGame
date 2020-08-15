def remove_dupe1(x)
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y


# using sets
def remove_dupe2(x):
    return list(set(x))


a = [1, 2, 3, 4, 3, 2, 1]
print(a)
print(remove_dupe1(a))
print(remove_dupe2(a))
