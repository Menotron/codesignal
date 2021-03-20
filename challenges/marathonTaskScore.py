l, m, s, t = eval(dir()[0])
# return 0 if t <= 0 else m if t <= 1 else max(m - 10 * (s - 1) - (m / 2) * (1 / l) * t, m/2)
return (t>-1) * max(m - 10 * (s - 1) - (m / 2) * (1 / l) * t, m/2)