import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt('sun_AM0.dat')
wavelen=[]
spectra=[]
for i in range(len(data)):
    wavelen.append(data[i][0]/1000) #micron
    spectra.append(data[i][1]*(10**(7+3-4))) #erg/seg * cm^-2 * um^-1

fig = plt.plot(wavelen,spectra)
plt.xlim(0,3)
plt.savefig('espectro.eps')
