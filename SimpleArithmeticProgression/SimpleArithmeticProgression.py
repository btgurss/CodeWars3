def solve(arr):
    count = 0
    
    for num in arr:
        adder = 1
        while(adder < arr[len(arr)-1]):
            if (num + adder) in arr and (num + adder + adder) in arr:
                count += 1
            adder += 1
    return (count)


solve([1, 2, 3, 4, 5])
solve([1, 2, 3, 5, 7, 9])
solve([0, 1, 2, 3, 5, 8, 11, 13, 14, 16, 18, 19])