ratingThreshold = lambda t, r: [i for i, v in enumerate(r) if sum(v) / len(v) < t]
