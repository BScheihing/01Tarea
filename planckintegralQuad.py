from scipy import integrate
import numpy as np

def argIntPlanckFunction(y):
    denom=(np.tan(y)**3)
    numer=(np.exp(np.tan(y))-1)*(np.cos(y)**2)
    return denom/numer

if __name__ == '__main__':
    integralQuad=integrate.quad(argIntPlanckFunction,0,np.pi/2)
    print "Valor de integral calculada (mediante .quad):", integralQuad[0]
