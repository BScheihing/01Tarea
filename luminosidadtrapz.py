import numpy as np
from astropy import constants as const

def luminosityTrapz(wavelen,spectra):
    intpy=np.trapz(spectra,x=wavelen)
    return 4*np.pi*(const.au.value**2)*intpy

if __name__ == '__main__':
    data=np.loadtxt('sun_AM0.dat')
    wavelen=[]
    spectra=[]
    for i in range(len(data)):
        wavelen.append(data[i][0])
        spectra.append(data[i][1])
    print "Luminosidad total del Sol (calculada mediante .trapz):",
    print luminosityTrapz(wavelen,spectra)
