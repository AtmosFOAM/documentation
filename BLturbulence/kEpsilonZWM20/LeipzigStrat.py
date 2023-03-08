import numpy as np
import matplotlib.pyplot as plt

beta = 4.7
L = 580
ustar = 0.65
g = 9.81
Theta0 = 288

z0 = 0.3
kappa = 0.41

sigmaTheta = 0.74

Ztop = 3000
n = 1000
dz = Ztop/n

z = np.linspace(0.5*dz,Ztop-0.5*dz, n)

G = -(sigmaTheta + beta*z/L)*ustar**2/(sigmaTheta*kappa**2*z*L)
G = np.where(z<100, G, G*np.exp(-(z-100)/520))

dthetadz = -sigmaTheta*Theta0/g*G

plt.plot(100*dthetadz, z/1000, 'k-', label='Stable')
plt.legend()
plt.ylim([0,1.5])
plt.xlabel(r'$d\theta/dz\ ^o$C/100m')
plt.ylabel('Height (km)')
plt.axvline(color='k', lw=0.5, ls=':')
plt.savefig('Leipzig_dthetadz_stable.pdf')

print('dthetadz = ', dthetadz)
