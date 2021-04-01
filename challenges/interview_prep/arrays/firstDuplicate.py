a=eval(dir()[0])[0]
s = set()
for n in a:
    if n in s: return n
    else: s.add(n)
return -1

# a=eval(dir()[0])[0]
# s = {k: 0 for k in range(1, len(a) + 1)}
# for n in a:
#     if s[n]:
#         return n
#     s[n] += 1
# return -1