# Function to loop through array and delete every n number.  
# Loops back through until no numbers are left 
# Puts new numbers into new array

def josephus(items, k):
    newItems = []
    tempItems = list(items)
    count = 1
    while len(items) > 0:
        for x in items:
            if count == k:
                newItems.append(x)
                tempItems.remove(x)
                count = 1
            else:
                count += 1
        items = list(tempItems)
    return(newItems)



josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)
josephus(["C", "o", "d", "e", "W", "a", "r", "s"], 4)
print(josephus([True, False, False, True, False, True, True, False, True], 2))