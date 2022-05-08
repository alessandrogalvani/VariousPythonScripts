import numpy as np
import sys, os, argparse
import tensorflow as tf
from tensorflow.python.framework import dtypes

import matplotlib.pyplot as plt
import pandas as pd

from matplotlib.pyplot import *


dati=pd.read_table('alpha1.75perbinder.txt',delim_whitespace=True, names=["L", "h" ,"am","m2","m4"]) #,header=None)
#dati=pd.read_table('perbinderattorno33.txt',delim_whitespace=True, names=["L", "h" ,"m2","m4"]) #,header=None)



lista=[]
listah=[]
#np.append(lista,np.array(datitemp['h'], datitemp['m2']**2/datitemp['m4'])
#print(dati)
for L in [64,128,256,512]:
    datitemp=dati.loc[dati['L'] == L]
    #lista[i]=np.append(lista[i], datitemp['m2']**2/datitemp['m4'] )
    lista.append( 1-(datitemp['m4']/(3*( datitemp['m2']**2) ) ).to_numpy()  )
    

for L in [64]:
    datitemp=dati.loc[dati['L'] == L]
    listah.append(datitemp['h'].to_numpy() )
    
#listah=listah..flatten()
listah=listah[0]

#fig = figure()

plt.xlabel("h")
plt.ylabel("$U=1-\\langle m^4\\rangle/(3\\langle m^2 \\rangle ^2 )$")
#plt.legend(['$L=96$','$L=80$','$L=64$' ,'$L=48$','$L=32$'])
plt.plot(listah,lista[0],'c',listah,lista[1],'b',listah,lista[2],'m',listah,lista[3],'k' )
plt.gca().legend(('L=64','L=128','L=256','L=512')) 
#plt.legend(loc="upper right")
plt.show()