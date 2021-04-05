a,=eval(dir()[0])
j = sorted(a)
return [j.pop((i > 0) * j.count(-1)) for i in a]