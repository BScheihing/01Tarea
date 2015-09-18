import numpy as np
import matplotlib.pyplot as plt
from astropy import constants as const
from scipy import integrate

def argIntPlanckFunction(y):
    denom=(np.tan(y)**3)
    numer=(np.exp(np.tan(y))-1)*(np.cos(y)**2)
    return denom/numer

#Constantes
AU=const.au.value
T=5778.0
kB=const.k_B.value
h=const.h.value
c=const.c.value

data=np.loadtxt('sun_AM0.dat')
wavelen=[]
spectra=[]
for i in range(len(data)):
    wavelen.append(data[i][0])
    spectra.append(data[i][1])

##Luminosidad fuera de la atmosfera terrestre
integral=0;
for i in range(len(data)-1):
    dx=data[i+1][0]-data[i][0]
    fi=(data[i+1][1]+data[i][1])/2.0
    integral=integral+dx*fi

luminosity=4*np.pi*(AU**2)*integral
print luminosity
print const.L_sun

##Integral de funcion de Planck
C=2*np.pi*h*((kB*T/h)**4)/(c**2)

N=500
epsilon=np.pi/(2*(N-1))
y=np.linspace(0+epsilon,np.pi/2-epsilon,N-2)
denom=(np.tan(y)**3)
numer=(np.exp(np.tan(y))-1)*(np.cos(y)**2)
integrand=np.divide(denom,numer)
integrand=np.insert(integrand,0,0)
integrand=np.append(integrand,0)
P=C*(epsilon/2)*(2*sum(integrand))

Rsol = np.sqrt(luminosity/(P*4*np.pi))

print Rsol
print const.R_sun

Ppy=np.trapz(integrand,dx=epsilon)
intpy=np.trapz(spectra,x=wavelen)
#intpyq=np.quad(integrand,dx=epsilon)
Ppyq=integrate.quad(argIntPlanckFunction,0,np.pi/2)

print Ppy, intpy
print Ppyq, np.pi**4/15
print P/C, integral
