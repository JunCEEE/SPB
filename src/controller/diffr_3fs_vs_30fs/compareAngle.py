import sys
import glob
import numpy as np
from timeit import default_timer as timer


sys.path.insert(0, '../toolkit')
import toolkit

data_root = '/gpfs/exfel/data/user/grotec/2NIP_S2E/sim_5kev_30fs_35_2NIP_EMC_Compton/diffr'
data_root2 = '/gpfs/exfel/data/user/grotec/2NIP_S2E/5keV_3fs_2NIP/diffr/diffr_Compton'

start = timer()

for i,filepath in enumerate(glob.iglob(data_root+'/*.h5')):
    angle = toolkit.getDataWfile(filepath,'angle')
    if i == 1:
        break
    for j,filepath2 in enumerate(glob.iglob(data_root2+'/*.h5')):
        #if j == 100:
            #end = timer()
            #print(end - start) # Time in seconds, e.g. 5.38091952400282
            #break
        angle2 = toolkit.getDataWfile(filepath2,'angle')
        quaterion = angle2 - angle
        abs_sum = np.sum([abs(ele) for ele in quaterion])
        if (abs_sum < 0.2):
            print (quaterion)
            print (filepath)
            print (filepath2)
            print ("")

end = timer()
print(j,end - start) # Time in seconds, e.g. 5.38091952400282

