a=128
b=32
dem=0

if(a==0):
	for i in range(1,b+1):
		if(b%i==0):
			dem=dem+1
elif(b==0):
	for i in range(1,a+1):
		if(a%i==0):
			dem=dem+1
elif(a<b):
    for i in range(1,a+1):
        if(a%i==0 and b%i==0):
            dem=dem+1
else:
    for i in range(1,b+1):
        if(a%i==0 and b%i==0):
            dem=dem+1
print(dem)