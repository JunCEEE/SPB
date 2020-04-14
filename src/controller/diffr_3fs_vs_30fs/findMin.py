import numpy as np

comList = []
with open('angle.txt','r') as f:
    lines = f.readlines()
    for i,line in enumerate(lines):
        #if (i%4==0):
        if (len(line.split())>3):
            s1 = line.strip('[')
            s2 = s1.replace(']','')
            x = np.array(s2.split())
            y = x.astype(float)
            y = [abs(ele) for ele in y]
            comList.append([i+1,np.sum(y)])
            #print(np.sum(y))
def takeSecond(elem):
    return elem[1]
comList.sort(key=takeSecond)
print (comList)


