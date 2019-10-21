hour= [13,13,14]
minute = [0,15,45]
dem = 0
xuat=[0]
for i in range(0,3):
    h= hour[i]
    m = minute[i]+20
    if m>60:
        m = m-60
        h = h+1
        if h >=24:
            h=h-24
    j= 0
    dem = 0
    while j<3:
        if hour[i]==hour[j]:
            if minute[i]<=minute[j] and minute[j]<= minute[i]+20:
                dem=dem+1
                xuat.append(dem)
        else:
            if h == hour[j]:      
                if minute[j] <= m:
                    dem = dem+1 
                    xuat.append(dem)
        j=j+1
    pass
print(max(xuat))   