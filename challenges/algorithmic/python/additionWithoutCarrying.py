a,b = eval(dir()[0])
c = 1
r = 0
while not a == b == 0:
     r += ((a + b) % 10) * c
     a //= 10 
     b //= 10
     c *= 10
return r

# additionWithoutCarrying = f = lambda a, b, c=1: 0 if a == b == 0 else ((a + b) % 10) * c + f(a // 10, b // 10, c * 10)