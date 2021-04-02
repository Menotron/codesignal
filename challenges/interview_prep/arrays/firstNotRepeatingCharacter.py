s = eval(dir()[0])[0]
for c in s:
    if s.find(c) == s.rfind(c):
        return c
return '_'


# s = eval(dir()[0])[0]
# m = {}
# for k in s:
#     m[k] = m.get(k, 0) + 1
# return next(iter([k for k, v in m.items() if v == 1]), '_')