# Take each number of array and add to it its place in the array.  Numbers over 10 will use last digit

def incrementer(num):
    # Initializing a new list and a staring counter
    new = []
    count=1
    # Looping through digits in the list
    for digit in num:
        # Setting temporary variable to digits
        temp = digit + count
        # Using if statement to change number if greater than 10
        if temp > 9:
            # Turning number to string and then back to integer after removing last digit
            temp = int(str(temp)[-1])
        # Counting
        count += 1
        # Adding temporary number to new list
        new.append(temp)
    return(new)
        

test = [1, 2, 3]
test2 = [4, 6, 9, 1, 3]
incrementer(test2)