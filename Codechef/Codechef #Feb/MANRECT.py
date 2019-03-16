for _ in range(int(input())):
    x0, y0 = 0, 0
    print('Q', x0, y0)
    A1 = int(input())
    x1 = A1 // 2
    y1 = A1 - x1
    print('Q', x1, y1)
    A2 = int(input())
    if A2 != 0:
        print('Q', x1 + A2, y1)
        A3 = int(input())
        if A3 == 0:
            xl, yl = x1 + A2, A1 - x1 - A2
        else:
            xl, yl = A1 - y1 - A2, y1 + A2
    else:
        xl, yl = x1, y1
    #print("A", xl, yl) 
    
    x0, y0 = 10 ** 9, 10 ** 9
    print('Q', x0, y0)
    A1 = int(input())
    x1 = x0 - A1 // 2
    y1 = y0 - (A1 - A1 // 2)
    print('Q', x1, y1)
    A2 = int(input())
    if A2 != 0:
        print('Q', x1, y1 - A2)
        A3 = int(input())
        if A3 == 0:
            xr, yr = 10 ** 9 - (A1 - (10 ** 9 - (y1 - A2))) , y1 - A2
            
        else:
            xr, yr = x1 - A2, 10 ** 9 - (A1 - (10 ** 9 - (x1 - A2)))
    else:
        xr, yr = x1, y1

    #print('A', xr, yr)
    print('A', xl, yl, xr, yr)
    Answer = int(input())
    