# Given a list of integers and a single sum value, return the first two values (parse from the left please) 
# in order of appearance that add up to form the sum.

def sum_pairs(ints, s):
    temp = [0,0]
    checker = len(ints)
    for i in range(len(ints)-1):
        for j in range(i+1, len(ints)):
            if ints[i] + ints[j] == s and j < checker:
                checker = j
                temp[0] = ints[i]
                temp[1] = ints[j]
    if temp == [0,0]:
        return "None"
    return temp
test = [1, 4, 8, 7, 3, 15]
test2 = [1, -2, 3, 0, -6, 7]
print(sum_pairs(test2, 14))