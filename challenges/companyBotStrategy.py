l = [a for a, b in eval(dir()[0])[0] if b == 1]
return sum(l)/len(l) if len(l) > 0 else 0
