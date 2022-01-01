# Function to rearrange digits of a number to make largest possible number

def next_bigger(n):
    temp = []
    for i in range(len(str(n))):
        temp.append(max([int(c) for c in str(n)]))
    print(temp)
        

next_bigger(12)
        


