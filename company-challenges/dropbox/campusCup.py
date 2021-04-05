s = {}
b = [0, 3, 8, 15, 15, 25]
for e in eval(dir()[0])[0]:
    d = e[e.index('@') + 1:]
    s[d] = s.get(d, 0) + 20
return [c[0] for c in sorted(s.items(), key=lambda k: (-b[k[1] // 100], k[0]))]