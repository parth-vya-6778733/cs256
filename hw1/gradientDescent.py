def f(x1,x2):
    return 1.5*(x1**2) + (x2**2) - 2*(x1*x2) + 2*(x1**3) + 0.5*(x1**4)

def fx1prime(x1,x2):
    return 3*x1 - 2*x2 + 6*x1**2 + 2*x1**3

def fx2prime(x1,x2):
    return 2*x2 - 2*x1

def testf(x1):
    return x1**2 - 4

def testfprime(x1):
    return 2*x

def alg(xInitial):
    i = 0
    theta = 0
    eta = 2
    maxIterations = 100

    while i != maxIterations:
        testfprime(xInitial)




print("Solution f(x): ", f(1,-3))
print("Solution f'(x1): ", fx1prime(1,-3))
print("Solution f'(x2): ", fx2prime(1,-3))


print("Solution f(x): ", f(.978,1.287))
print("Solution f'(x1): ", fx1prime(.978,1.287))
print("Solution f'(x2): ", fx2prime(.978,1.287))