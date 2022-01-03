def is_constructable(a):
    for area in a:
        print(area)
        for i in range(1, int(area ** (1/2))+1):
            print(i)
            if area ** (1/2) == i:
                print(True)
            elif i**2 + 
            isinstance(((area - i**2)**(1/2)), int) == True:
                print(True)
            else:
                print(False)

        
is_constructable([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])