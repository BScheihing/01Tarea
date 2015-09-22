import numpy as np

def planckIntegral(tolerancia):
    valor=(np.pi**4)/15
    N=16
    #Vuelta de inicio
    dx=np.pi/(2*(N-1))
    y=np.linspace(dx,np.pi/2-dx,N-2)
    denom=(np.tan(y)**3)
    numer=(np.exp(np.tan(y))-1)*(np.cos(y)**2)
    integrand=np.divide(denom,numer)
    integrand=np.insert(integrand,0,0)
    integrand=np.append(integrand,0)
    integral=(dx/2)*(2*sum(integrand))
    #Iteracion hasta alcanzar tolerancia deseada
    while np.fabs(integral-valor)>tolerancia:
        integral=integral/dx
        N=2*N-1
        dx=np.pi/(2*(N-1))
        y=np.linspace(dx,np.pi/2-dx,(N-1)/2)
        denom=(np.tan(y)**3)
        numer=(np.exp(np.tan(y))-1)*(np.cos(y)**2)
        integrand=np.divide(denom,numer)
        integral=dx*(integral+sum(integrand))
    return integral

if __name__ == '__main__':
    tol=input("Ingrese tolerancia para calculo de integral:")
    print "Valor de integral calculada:", planckIntegral(tol)
    print "Valor real:", np.pi**4/15
