for _ in range(int(input())):
    x0, y0 = 0, 0
    print('Q', x0, y0)
    A1 = int(input())
    print('Q', A1, 0)
    yl = int(input())
    xl = A1 - yl
    
    # neg bol baruun dood bulan
    print('Q', xl, yl)
    test1 = int(input())
    if test1 != 0:# esvel yl
        xl, yl = xl + test1 // 2, yl - test1 // 2
    
    x1, y1 = 10**9, 10**9
    print('Q', x1, y1)
    A2 = int(input())
    print('Q', x1 - A2, y1)
    yr_1 = int(input())
    xr = A2 - yr
    
    # neg bol baruun dood bulan
   # print('Q', x1 - xr, y1 - yr)
    test2 = int(input())
    if test2 != 0:# esvel yl
        xr, yr = xl + test2 // 2, yl - test2 // 2
    print('A', xl, yl, x1 - xr, y1 - yr)
    
    
    
    