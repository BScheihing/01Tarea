import numpy as np
from luminosidadsol import luminosity
from planckintegral import planckIntegral
from astropy import constants as const

#Luminosidad del Sol
info=np.loadtxt('sun_AM0.dat')
lumin=luminosity(info)

#Constantes
T=5778.0
kB=const.k_B.value
h=const.h.value
c=const.c.value

#Integral de funcion de Planck
C=2*np.pi*h*((kB*T/h)**4)/(c**2)
P=C*planckIntegral(10**(-12))
print "Energia por unidad de area por unidad de tiempo emitida",
print "por un cuerpo negro con la temperatura efectiva del Sol:",
print P, "[W/(s*m^2)]"

#Radio efectivo del Sol
Rsol = np.sqrt(lumin/(P*4*np.pi))
print "Radio efectivo del Sol:", Rsol, "[m]"
