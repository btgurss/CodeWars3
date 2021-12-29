# Function to determine if numbers in fibonacci sequence will multiply to certain value

def productFib(prod):
    temp=0
    fib1 = 0
    fib2 = 1
    while temp < prod:
       temp = fib1 * fib2
       fibtemp = fib2
       fib2 = fib1 + fib2
       fib1 = fibtemp      

    if prod == 0:
        return [fib1, fib2, True] 
    elif temp == prod:
        return [fib2-fib1, fib1, True]
    else:
        return [fib2-fib1, fib1, False]


# Online versions - more efficient
def product(prod):
    a, b = 0, 1
    while prod > a * b:
        a, b = b, a + b
    return [a, b, prod == a * b]
test = 4895
test2 = 5895
print(productFib(test2))