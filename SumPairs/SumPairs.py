# Given a list of integers and a single sum value, return the first two values (parse from the left please) 
# in order of appearance that add up to form the sum.

def sum_pairs(ints, s):
    temp = ['a','b']
    checker = len(ints)
    for i in range(len(ints)-1):
        for j in range(i+1, len(ints)):
            if ints[i] + ints[j] == s and j < checker:
                checker = j
                temp[0] = ints[i]
                temp[1] = ints[j]
    if temp == ['a','b']:
        return 
    return temp

def sum_pairs_efficient(ints, s):
    # Creating empty set
    set1 = set()
    # Looping through numbers in list
    for num in ints:
        # Checking if sum subtracted by num is in set
        if s - num in set1:
            return [s - num, num]
        set1.add(num)


test = [1, 4, 8, 7, 3, 15]
test2 = [1, -2, 3, 0, -6, 7]
print(sum_pairs(test2, 14))