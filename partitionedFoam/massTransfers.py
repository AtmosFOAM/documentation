from pylab import *

# Experimenting on how S01 should depend on w and on Dw/Dt

# sub-grid variability in w (a few options)
wp = array([0.01, 0.1, 1., 4., 10])

# range of values of w
w = linspace(-4,4,81)

ion()
figure(1)
clf()
axvline(0, color='k', linestyle=':')
for i in range(len(wp)):
    S = exp(w/wp[i])/wp[i]
    plot(w, S, label=r'$w^\prime =$'+str(wp[i]))
    ylim(0,2)
    xlabel(r'$w_0$')

legend()
draw()
savefig('S01_as_exp.pdf')

