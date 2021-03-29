def lineUp(co):
    s = True
    r = 0
    p = 'A'
    for c in co:
        n = c
        if not s and (p == n != 'A' or p == 'R' and n == 'L' or p == 'A' and n != 'A') or s and n == 'A':
            s = True
            r += 1
        else:
            s = False
        p = n
    return r


print(lineUp("LLARL"))
print(lineUp("RLR"))
print(lineUp(""))
print(lineUp("L"))
print(lineUp("A"))
print(lineUp("AAAAAAAAAAAAAAA"))
print(lineUp("RRRRRRRRRRLLLLLLLLLRRRRLLLLLLLLLL"))
print(lineUp("AALAAALARAR"))