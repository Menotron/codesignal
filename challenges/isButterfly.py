isButterfly = lambda a: sum(sum(a[i]) * (not a[i][i]) for i in range(len(a))) == 12