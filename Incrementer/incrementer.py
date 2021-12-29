# Take each number of array and add to it its place in the array.  Numbers over 10 will use last digit

def incrementer(num):
    new = []
    count=1
    for digit in num:
        temp = digit + count
        if temp > 9:
            temp = int(str(temp)[-1])
        count += 1
        new.append(temp)
    return(new)
        

test = [1, 2, 3]
test2 = [4, 6, 9, 1, 3]
incrementer(test2)