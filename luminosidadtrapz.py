'''
Este script define el metodo que calcula la
integral del espectro del Sol medido desde la
Tierra, usando scipy.integrate.trapz (en este
caso, numpy.trapz). Si se ejecuta desde este
archivo, calcula e imprime en pantalla el
valor calculado de la luminosidad del Sol a
partir de los datos de sun_AM0.dat.
'''

import numpy as np
from astropy import constants as const

def luminosityTrapz(wavelen,spectra):
    '''
    Este metodo calcula la luminosidad total
    del Sol a partir del espectro de radiacion,
    en forma de dos arreglos: uno con las
    longitudes de onda y el otro con el flujo
    de energia por unidad de longitud de onda
    asociada. Utiliza el metodo numpy.trapz.
    '''
    intpy=np.trapz(spectra,x=wavelen)
    return 4*np.pi*(const.au.value**2)*intpy

if __name__ == '__main__':
    data=np.loadtxt('sun_AM0.dat')
    wavelen=[]
    spectra=[]
    for i in range(len(data)):
        wavelen.append(data[i][0])
        spectra.append(data[i][1])
    print "Luminosidad total del Sol \
(calculada mediante .trapz):",
    print luminosityTrapz(wavelen,spectra),
    print "[W]"
