l,*r = eval(dir()[0])
while l:
    r += l.value,
    l = l.next
return r == r[::-1]