l = eval(dir()[0])[0]
return [i[-1:] + i[:-1] for i in l[-1:] + l[:-1]]
