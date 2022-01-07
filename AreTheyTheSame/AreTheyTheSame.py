# Function to determine if one array is squared of the other.

def comp(array1, array2):
    array1.sort()
    array2.sort()
    if len(array1) != len(array2):
        return False
    for i in range(0, len(array1)):
        if array1[i] ** 2 != array2[i]:
            return False
        
    return True


a = [121, 144, 19, 161, 19, 144, 19, 11]
b=  [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b)
comp([], [])