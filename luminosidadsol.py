import numpy as np
from astropy import constants as const

##Luminosidad fuera de la atmosfera terrestre
def luminosity(data):
    integral=0;
    for i in range(len(data)-1):
        dx=data[i+1][0]-data[i][0]
        fi=(data[i+1][1]+data[i][1])/2.0
        integral=integral+dx*fi
    lumin=4*np.pi*(const.au.value**2)*integral
    return lumin

if __name__ == '__main__':
    info=np.loadtxt('sun_AM0.dat')
    print "Luminosidad total del Sol:", luminosity(info), "[W]"
