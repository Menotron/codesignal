incorrectPasscodeAttempts = lambda p, a: ''.join(['0'] * 10) in ''.join(['1' if i == p else '0' for i in a])
