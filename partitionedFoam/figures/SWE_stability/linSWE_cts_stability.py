# Find and plot the imaginary eigenvalues of the linear system representing
# the linearised, conditionally averaged SWE

import numpy as np
import matplotlib.pyplot as plt

# The coefficients of the quartic polynomial how roots are the eigenvalues

U0 = np.round(np.arange(-1,1.001, 0.01), decimals = 4)
U1 = np.round(np.arange(-1,1.001, 0.01), decimals = 4)
# Polynomial coefficients
def polyCoeffs(U,gH):
    u0 = U[0]; u1 = U[1];
    gH0 = gH[0]; gH1 = gH[1];
    return [1.,
           2*(u0+u1),
           u0**2 + u1**2 + 4*u0*u1 - gH0 -gH1,
           2*(u0*u1*(u0 + u1) - gH1*u0 - gH1*u1),
           ((u0*u1)**2 - gH1*u0**2 - gH0*u1**2)]

# Function to find the Matrix of largest imaginary part of eigenvalues
def calcIroots(U0, U1, gH):
    SMALL = 1e-16
    Iroots = np.zeros([len(U1), len(U0)])
    #
    for i in range(len(U0)):
        for j in range(len(U1)):
            roots = np.roots(polyCoeffs([U0[i], U1[j]],gH))
            Iroots[j,i] = max(np.imag(roots))
            if Iroots[j,i] < SMALL:
                Iroots[j,i] = np.nan
    return Iroots

# Plot Iroots for different values of g
gHvals = [[1, 1], [1, 2], [1, 0.5], [0.5,0.5], [2,2], [0.5,2]]
figNames = ['Iroots_gH11.pdf', 'Iroots_gH12.pdf', 'Iroots_gH105.pdf',
            'Iroots_gH0505.pdf', 'Iroots_gH22.pdf', 'Iroots_gH052.pdf'];

for ifig in range(len(gHvals)):
    Iroots = calcIroots(U0, U1, gHvals[ifig])
    plt.figure(ifig)
    plt.ion()
    plt.clf()
    contourVals = np.arange(0,1.001,0.1)
    plt.contourf(U0, U1, Iroots, contourVals, extend='max')
    plt.colorbar()
    plt.xlabel('$U_0$')
    plt.ylabel('$U_1$')
    plt.title('$gH_0 = ' + str(gHvals[ifig][0])
              +',\ \ gH_1 = ' + str(gHvals[ifig][1]) + '$')
    plt.savefig(figNames[ifig], bbox_inches="tight")


