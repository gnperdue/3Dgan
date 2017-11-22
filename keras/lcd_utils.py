from __future__ import print_function
import numpy
import h5py
import os
# TODO - import, use, `logging`


def lcd_3Ddata():
    data_dir = '.'
    try:
        data_dir = os.environ['H5DATADIR']
    except KeyError:
        print('Environment variable H5DATADIR is not defined.')
    except Exception as e:
        print(e)
    h5file = data_dir + '/EGshuffled.h5'
    print('Using h5 file: {}'.format(h5file))
    f = h5py.File(h5file, 'r')
    data = f.get('ECAL')
    dtag = f.get('TAG')
    xtr = numpy.array(data)
    tag = numpy.array(dtag)
    # xtr = xtr[..., numpy.newaxis]
    # xtr = numpy.rollaxis(xtr, 4, 1)
    print('xtr.shape = ', xtr.shape)
    f.close()
   
    return xtr, tag.astype(bool)
