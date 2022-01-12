# Function to determine the number of sets of 3 with equal parts

def solve(arr):
    # Setting counter
    count = 0
    
    # Loop to look through all numbers in array
    for num in arr:

        #Counter that resets at beginning of each input
        adder = 1

        # Loop to go through all number of array
        while(adder < arr[len(arr)-1]):

            # Checking for set of 3
            if (num + adder) in arr and (num + adder + adder) in arr:
                count += 1
            adder += 1
    return (count)


solve([1, 2, 3, 4, 5])
solve([1, 2, 3, 5, 7, 9])
solve([0, 1, 2, 3, 5, 8, 11, 13, 14, 16, 18, 19])