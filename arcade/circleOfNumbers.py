circleOfNumbers = lambda n, f: abs([1,-1][f > n // 2] * f + n // 2) % n
