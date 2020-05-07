import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('9fs_0.txt')
dt = data[1,0] - data[0,0]
print (dt)
t_shift = np.linspace(0,data[:,0].max(),data.shape[0])

new_dt = 0.05 # unit: fs 
bins = np.arange(0,t_shift.max()+2*new_dt,new_dt)
int_rebin = np.histogram(t_shift, bins=bins, weights=data[:,1]*dt)
# t = np.arange(0.5*new_dt,t_shift.max()+0.5*new_dt+new_dt,new_dt)
t = np.arange(0,t_shift.max()+new_dt,new_dt)

print (data[:,1].sum()*dt,int_rebin[0].sum())

plt.plot(t_shift,data[:,1])
plt.plot(t,int_rebin[0]/new_dt)
plt.show()

new_data = np.vstack((t_shift,data[:,1]))
# new_data = np.vstack((t,int_rebin[0]/new_dt))

np.savetxt('profile.txt',new_data.T,fmt='%.6e')

