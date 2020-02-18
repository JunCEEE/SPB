"""Explore s2e diffraction dataset

"""
import numpy, h5py, os
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
from matplotlib.colors import LogNorm

def print_name(name, obj):
    print (name)

def print_attrs(name, obj):
    print (name)
    for key, val in obj.attrs.iteritems():
        print ("    %s: %s" % (key, val))

def print_data(name, obj):
    print (name)
    is_dataset = isinstance(obj, h5py.Dataset)
    if (is_dataset):
        if (len(obj.shape) == 0):
            print ("    %s" % (obj[()]))
        elif (len(obj) < 2):
            print ("    %s" % (obj[0]))
        else:
            print ("    shape: %s" % (str(obj.shape)))

def getFileName(root,index):
    file = os.path.join(root, 'diffr_out_%07d.h5' % (index))
    return file

def listEntry(data_root_path,pattern_index=0,d_type='diffr'):
    file = getFileName(data_root_path, pattern_index)
    with h5py.File(file,"r") as h5:
        h5.visititems(print_data)


def getData(data_root_path,pattern_index=0,d_type='diffr'):
    file = os.path.join(data_root_path, 'diffr_out_%07d.h5' % (pattern_index))
    with h5py.File(file,"r") as h5:
        d = h5['data/'+d_type][...]
    return d

def plotLog(data, vmin=None, vmax=None, cmap="viridis"):
    fig, ax = plt.subplots()
    colormap = plt.get_cmap(cmap)
    im = ax.imshow(data,norm=LogNorm(vmin=vmin,vmax=vmax),cmap=colormap)
    fig.colorbar(im)
    return fig,ax,im

def listOrientation(data_root_path, pattern_index=0):
    with h5py.File(os.path.join(data_root_path, 'diffr_out_%07d.h5' % (pattern_index)) ,"r") as f:
        print (f['data/angle'][...])


