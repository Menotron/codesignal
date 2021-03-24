fancyRide = lambda l, f: 'Uber' + 'X XL Plus Black SUV'.split()[max([i for i,r in enumerate(f) if (r * l) <= 20])]
