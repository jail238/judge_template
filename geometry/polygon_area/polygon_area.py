def polygon_area(arr): #already clockwise sorting
    x, y = [], []
    for i in range(len(arr)):
        x.append(arr[i][0])
        y.append(arr[i][1])
    x.append(arr[0][0])
    y.append(arr[0][1])
    r1, r2 = 0, 0
    for i in range(len(arr)):
        r1 += x[i]*y[i+1]
        r2 += y[i]*x[i+1]
    return abs(r1-r2)/2
