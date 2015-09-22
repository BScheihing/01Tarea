import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt('sun_AM0.dat')
wavelen=[]
spectra=[]
for i in range(len(data)):
    wavelen.append(data[i][0]/1000) #micron
    spectra.append(data[i][1]*(10**(7+3-4))) #erg/seg * cm^-2 * um^-1

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(wavelen,spectra)
ax.set_xlim(0,3)
ax.set_xlabel('Longitud de onda [$\mu m$]')
ax.set_ylabel('Flujo por longitud de onda \
[$erg \cdot s^{-1} \cdot cm^{-2} \cdot \mu m^{-1}$]')
ax.yaxis.get_major_formatter().set_powerlimits((0, 1))
ax.set_title('Espectro del Sol medido desde la Tierra')
plt.savefig('espectro.eps')

fig2 = plt.plot(wavelen,spectra)
plt.yscale('log')
plt.xlim(0,10**2)
plt.ylim(10**(-2),10**7)
plt.title('Espectro del Sol medido desde la Tierra, escala semilogaritmica')
plt.savefig('espectrolog.eps')

fig3 = plt.plot(wavelen,spectra)
plt.yscale('log')
plt.xscale('log')
plt.xlim(0,10**3)
plt.ylim(10**(-5),10**7)
plt.title('Espectro del Sol medido desde la Tierra, escala logaritmica')
plt.savefig('espectrologlog.eps')
