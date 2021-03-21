a, b, c = eval(dir()[0])
x = y = z = 0
r = []
l = len
while x < l(a) and y < l(b) and z < l(c):
    L = a[x], b[y], c[z]
    m = min(L)
    r += max(L)-m,
    x += m == a[x]
    y += m == b[y]
    z += m == c[z]
return min(r) * 2