# Function to find the sum of intervals.  Overlapping intervals do not count

def sum_of_intervals(intervals):
    # Setting variables
    sum = 0
    temp = []
    # Using for loop to got through tuples
    for a, b in intervals:
        # Finding sum
        sum = sum + abs(b - a)
        # For loop to go through range and add to new list if not already in list
        for x in range(a, b):
            if x not in temp:
                temp.append(x)
    # Subtracting the length of new list to determine final total
    sum = sum - (sum - len(temp))
    return sum
sum_of_intervals([(1, 5), (1, 5)])