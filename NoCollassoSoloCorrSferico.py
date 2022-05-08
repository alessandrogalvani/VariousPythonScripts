import numpy as np
from matplotlib.pyplot import *
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

params= {'text.latex.preamble' : [r'\usepackage{amsmath}']}
rcParams.update(params)
params= {'text.latex.preamble' : [r'\usepackage{amssymb}']}
rcParams.update(params)

rc('font', size=16)
rc('text', usetex=True)
rcParams["mathtext.fontset"] = "dejavuserif"
#rc('font', size=16,**{'family' : "sans-serif"})

#L_list = [32,48,64,96,128,192]
#data_list = ["1pt_031.dat", "1pt_047.dat", "1pt_063.dat" ,"1pt_095.dat", "1pt_127.dat", "1pt_191.dat"]

a1              = 0.72533 #         +/- 0.01255      (1.731%)
b1              = 2.02825  #        +/- 0.009246     (0.4559%)
a2              = 2.51023   #       +/- 0.03778      (1.505%)
b2              = 4.85802    #      +/- 0.05226      (1.076%)
a3              = 9.39762     #     +/- 0.1053       (1.121%)
b3              = 13.9356      #    +/- 0.1422       (1.02%)


data = np.loadtxt("solocorrelazionisferico.dat")
X        = np.transpose(data)[0]
Y        = np.transpose(data)[1]
#Yerr     = np.transpose(data)[2]

fig = figure()
ax = fig.add_subplot('111',facecolor='white')

ax.set_xlabel(r"$\mathfrak{D}_{g}(x,y)$")
#ax.set_title(r"$L=64\qquad g=\delta/{\gamma_{(\Delta_\phi^{CB})}}^2\qquad \bar{\chi}=0.0019$")
ax.set_title(r"$L=12\qquad g=\delta/\gamma^2$")
#ax.set_xlabel(r"$\mathfrak{D}_{\delta/{\gamma_{(\Delta_\phi^{CB})}}^2}(x,y)$")
#ax.set_xlabel(r"$\mathfrak{D}$")
ax.set_ylabel('$\langle\phi(x)\phi(y) \\rangle$')


#XX = np.linspace(0, 7, 201)
#YY = 1+a1*np.exp(-b1*XX)+a2*np.exp(-b2*XX)+a3*np.exp(-b3*XX)

ax.errorbar(X, Y, fmt='o', clip_on=True, markersize=2)
#ax.plot(XX, YY)

#ee=.1

#rect = [0.44-ee,0.53-ee,0.375+ee,.325+ee]

#ax_inset = fig.add_axes(rect,anchor='NW',facecolor=None)

#ax_inset.set_xlabel(r"$\mathfrak{D}_{\delta/{\gamma_{(\Delta_\phi^{CB})}}^2}(x,y)$")
#ax_inset.set_xlabel(r"$\mathfrak{D}_{g}(x,y)$")
#ax_inset.set_xlabel(r"$\mathcal{D}_{\delta/{\gamma_{(\Delta_\phi^{CB})}}^2}(x,y)$")
#ax_inset.set_ylabel(r'$r(x,y)$')

#ax_inset.set_xlim(0.15, 2.5)
#ax_inset.set_ylim(0.0002, 2)

#ax_inset.set_xlim(0.15, 1.25)
#ax_inset.set_ylim(.9, 3.5)

#ax_inset.tick_params(labelsize=12)

#ax_inset.set_xscale("log", nonposx='clip')
#ax_inset.set_yscale("log", nonposy='clip')

#ax_inset.errorbar(X, Y, Yerr, fmt='o', clip_on=True, markersize=1)
#ax_inset.plot(XX, YY)

savefig('SoloCorrelazioniSferico.pdf', bbox_inches='tight')
