# Function to determine bonus amounts based on days taken off

def bonus(arr, s):
    totalHours = sum(arr)
    payPerson = []
    for num in arr:
        payPerson.append(round(851 - float(s/totalHours * num), 2))

    return payPerson


print(bonus([18, 15, 12], 851))