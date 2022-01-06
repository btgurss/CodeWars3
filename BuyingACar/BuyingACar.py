def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    savings = 0
    count = 1
    while savings + startPriceOld < startPriceNew:
        if(count % 2 == 0):
            percentLossByMonth = percentLossByMonth + 0.5
        startPriceOld = startPriceOld * (1-(percentLossByMonth/100))
        startPriceNew = startPriceNew * (1-(percentLossByMonth/100))
        savings = savings + savingperMonth
        count += 1
    
    leftover = int(savings + startPriceOld - startPriceNew)
    count -= 1
    
    return[count, leftover]

print(nbMonths(2000, 8000, 1000, 1.5))
nbMonths(12000, 8000, 1000, 1.5)