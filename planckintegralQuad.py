'''
Este script define la funcion a usar para
calcular la integral de la funcion de Planck
mediante scipy.integrate.quad. Si se ejecuta
desde este archivo, calcula e imprime en
pantalla el valor de la integral. El resultado
debiese ser pi^4/15.
'''

from scipy import integrate
import numpy as np

def argIntPlanckFunction(y):
    '''
    Este metodo define la funcion argumento a
    integrar para calcular la integral de la
    funcion de Planck mediante integrate.quad.
    '''
    denom=(np.tan(y)**3)
    numer=(np.exp(np.tan(y))-1)*(np.cos(y)**2)
    return denom/numer

if __name__ == '__main__':
    integralQuad=integrate.quad(
        argIntPlanckFunction,0,np.pi/2)
    print "Valor de integral calculada \
        (mediante .quad):", integralQuad[0]
