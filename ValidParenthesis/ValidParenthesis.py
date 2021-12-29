# Function to determine whether a string has valid parentheses

def valid_parentheses(string):
    # Setting intial counter to 0
    count = 0
    # Using for loop to go through all parts of string
    for part in string:
        # Using if/else statements to check 
        if part == '(' and count >= 0:
            count += 1
        elif part == ')' and count >= 0:
            count -= 1
        # This shows either parentheses out of order or too many facing left
        elif count < 0:
            return False
    # If statement returning boolean if count is true
    if count == 0:
        return True
    else:
        return False

test = "()"
test2 = "(()())"
test3 = "((())))("
test4 = ")("
test5 = "(Hell)(opiu)"
print(valid_parentheses(test5))