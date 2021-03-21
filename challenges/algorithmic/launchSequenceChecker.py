s = {}
r = []
for x,y in zip(*eval(dir()[0])):
    r+=s.get(x,0) < y,
    s[x] = y
return all(r)