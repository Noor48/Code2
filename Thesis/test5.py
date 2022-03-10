import matplotlib.pyplot as plt
import numpy as np


datas=np.loadtxt("REFLECTIVITY.dat",dtype=np.float64,skiprows=1) 

fig, axs = plt.subplots(3,2,figsize=(10,8))
axs[0,0].plot(datas[:,0], datas[:,1],linewidth=1.5, label='xx', color='orange')
axs[0,0].legend()
axs[0,1].plot(datas[:,0], datas[:,2],linewidth=1.5, label='yy', color='blue')
axs[0,1].legend()
axs[1,0].plot(datas[:,0], datas[:,3],linewidth=1.5, label='zz', color='red')
axs[1,0].legend()
axs[1,1].plot(datas[:,0], datas[:,4],linewidth=1.5, label='xy', color='green')
axs[1,1].legend()
axs[2,0].plot(datas[:,0], datas[:,5],linewidth=1.5, label='yz', color='black')
axs[2,0].legend()
axs[2,1].plot(datas[:,0], datas[:,6],linewidth=1.5, label='zx', color='violet')
axs[2,1].legend()
fig.suptitle('Reflectivity', fontsize=20)
fig.supylabel('cm^-1', fontsize=10)
fig.supxlabel('Energy (eV)', fontsize=10)
fig.tight_layout()
plt.show()

fig, axs = plt.subplots(3,2,figsize=(10,8))
axs[0,0].plot(datas[:,0], datas[:,1],linewidth=1.5, label='xx', color='orange')
axs[0,0].legend()
axs[0,1].plot(datas[:,0], datas[:,2],linewidth=1.5, label='yy', color='blue')
axs[0,1].legend()
axs[1,0].plot(datas[:,0], datas[:,3],linewidth=1.5, label='zz', color='red')
axs[1,0].legend()
axs[1,1].plot(datas[:,0], datas[:,4],linewidth=1.5, label='xy', color='green')
axs[1,1].legend()
axs[2,0].plot(datas[:,0], datas[:,5],linewidth=1.5, label='yz', color='black')
axs[2,0].legend()
axs[2,1].plot(datas[:,0], datas[:,6],linewidth=1.5, label='zx', color='violet')
axs[2,1].legend()
fig.suptitle('Reflectivity', fontsize=20)
fig.supylabel('cm^-1', fontsize=10)
fig.supxlabel('Energy (eV)', fontsize=10)
fig.tight_layout()
plt.savefig("testref.svg")
