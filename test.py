import math
def kiemtraNguyenTo(x):
  if (x<=1):
  	return False
  for i in range(2,int(math.sqrt(x))+1):
    print(i)
    if (x%i==0):
    	return False
  return True

print(kiemtraNguyenTo(26))