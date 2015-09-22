'''
Este script define el metodo implementado para
calcular la luminosidad total del Sol a partir
de un arreglo con datos, y si se ejecuta desde
el mismo archivo, calcula e imprime en pantalla
la luminosidad total del Sol.
'''

import numpy as np
from astropy import constants as const

##Luminosidad fuera de la atmosfera terrestre
def luminosity(data):
    '''
    Este metodo calcula la luminosidad total
    del Sol a partir de un arreglo de datos,
    donde cada elemento es el par longitud de
    onda - flujo por longitud de onda, en ese
    orden. Se realiza la integracion de estos
    datos mediante la regla de los trapecios
    y luego se multiplica por el area total
    sobre la que incide el flujo con ese valor.
    '''
    integral=0;
    for i in range(len(data)-1):
        dx=data[i+1][0]-data[i][0]
        fi=(data[i+1][1]+data[i][1])/2.0
        integral=integral+dx*fi
    lumin=4*np.pi*(const.au.value**2)*integral
    return lumin

if __name__ == '__main__':
    info=np.loadtxt('sun_AM0.dat')
    print "Luminosidad total del Sol:",
    print luminosity(info), "[W]"
