a,b = eval(dir()[0])
return ''.join(map(bin, range(a,b+1))).count('1')