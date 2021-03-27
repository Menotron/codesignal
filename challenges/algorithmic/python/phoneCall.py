m, *n, s = eval(dir()[0])
r = 0
while s - m >= 0:
    r += 1
    s -= n[r > 9]
return r