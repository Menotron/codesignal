def get_pages(c, t, o=10):
    k = [o // 2 + 1, o // 2 + 2][o % 2 != 0]
    n = t - o // 2 + 1
    return [x + 1 + [0, c - k][c > k] - [0, c - n][c > n] for x in range(o)]