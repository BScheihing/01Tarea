'''
Este script define el metodo implementado para
calcular la integral de la funcion de Planck
dada una tolerancia deseada. Si se ejecuta
desde este archivo, recibe una tolerancia como
input y calcula e imprime en pantalla el valor
de la integral.
'''

import numpy as np

def planckIntegral(tolerancia):
    '''
    Este metodo calcula la integral asociada
    al calculo de la integral de la funcion de
    Planck, recibiendo como parametro la
    tolerancia para el valor de la misma con
    respecto al valor que se obtiene de forma
    analitica. Primero realiza una integracion
    sobre una particion del intervalo (que
    arbitrariamente parte con 16 puntos), y
    luego va refinando el valor de la integral
    sumando los valores de la funcion en los
    puntos intermedios. El ciclo de refinacion
    consiste en:
        1)Dividir la integral previa por el
        paso de su particion.
        2)Calcular la funcion en los puntos
        intermedios a los del paso anterior.
        3)Sumar los valores calculados de la
        funcion a la integral anterior.
        4)Multiplicar por el nuevo paso de la
        particion. (En este momento tenemos
        hecho el calculo de la integral)
        5)Verificar si satisface la tolerancia
        pedida. Si no, repetir desde 1).
    Finalmente retorna la integral.
    '''
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
    tol=input("Ingrese tolerancia para calculo \
de integral:")
    print "Valor de integral calculada:",
    print planckIntegral(tol)
    print "Valor real:", np.pi**4/15
