"""
The contents of this module were copied from `pymicro`. See `pymicro.file.file_utils`.

https://github.com/heprom/pymicro/blob/26961707df6e31ab01b77d0b76f360471038eca5/pymicro/file/file_utils.py

Kudos @heprom!
"""

import os, sys
import numpy as np
import struct


def HST_info(info_file):
    """Read the given info file and returns a dictionary containing the data size and type.
    
    .. note::
    
       The first line of the file must begin by ! PyHST or directly by NUM_X. 
       Also note that if the data type is not specified, it will not be present in the dictionary.
    
    :param str info_file: path to the ascii file to read.
    :return: a dictionary with the values for x_dim, y_dim, z_dim and data_type if needed.
    """
    info_values = {}
    f = open(info_file, 'r')
    # the first line must contain PyHST or NUM_X
    line = f.readline()
    if line.startswith('! PyHST'):
        # read an extra line
        line = f.readline()
    elif line.startswith('NUM_X'):
        pass
    else:
        sys.exit('The file does not seem to be a PyHST info file')
    info_values['x_dim'] = int(line.split()[2])
    info_values['y_dim'] = int(f.readline().split()[2])
    info_values['z_dim'] = int(f.readline().split()[2])
    try:
        info_values['data_type'] = f.readline().split()[2]
    except IndexError:
        pass
    return info_values


def HST_read(scan_name, zrange=None, data_type=np.uint8, verbose=False,
             header_size=0, autoparse_filename=False, dims=None, mmap=False, pack_binary=False):
    '''Read a volume file stored as a concatenated stack of binary images.
    The volume size must be specified by dims=(nx, ny, nz) unless an associated
    .info file is present in the same location to determine the volume
    size. The data type is unsigned short (8 bits) by default but can be set
    to any numpy type (32 bits float for example).
    The autoparse_filename can be activated to retreive image type and
    size:
    ::
      HST_read(myvol_100x200x50_uint16.raw, autoparse_filename=True)
    will read the 3d image as unsigned 16 bits with size 100 x 200 x 50.
    .. note::
      If you use this function to read a .edf file written by
      matlab in +y+x+z convention (column major order), you may want to
      use: np.swapaxes(HST_read('file.edf', ...), 0, 1)
    :param str scan_name: path to the binary file to read.
    :param zrange: range of slices to use.
    :param data_type: numpy data type to use.
    :param bool verbose: flag to activate verbose mode.
    :param int header_size: number of bytes to skeep before reading the payload.
    :param bool autoparse_filename: flag to parse the file name to retreive the dims and data_type automatically.
    :param tuple dims: a tuple containing the array dimensions.
    :param bool mmap: activate the memory mapping mode.
    :param bool pack_binary: this flag should be true when reading a file written with the binary packing mode.
    '''
    if autoparse_filename:
        s_type = scan_name[:-4].split('_')[-1]
        data_type = np.dtype(s_type)
        s_size = scan_name[:-4].split('_')[-2].split('x')
        dims = (int(s_size[0]), int(s_size[1]), int(s_size[2]))
        if verbose:
            print('auto parsing filename: data type is set to', data_type)
    if dims is None:
        infos = HST_info(scan_name + '.info')
        [nx, ny, nz] = [infos['x_dim'], infos['y_dim'], infos['z_dim']]
        if 'data_type' in infos:
            if infos['data_type'] == 'PACKED_BINARY':
                pack_binary = True
                data_type = np.uint8
            else:
                data_type = np.dtype(infos['data_type'].lower())  # overwrite defaults with .info file value
    else:
        (nx, ny, nz) = dims
    if zrange is None:
        zrange = range(0, nz)
    if verbose:
        print('data type is', data_type)
        print('volume size is %d x %d x %d' % (nx, ny, len(zrange)))
        if pack_binary:
            print('unpacking binary data from single bytes (8 values per byte)')
    if mmap:
        data = np.memmap(scan_name, dtype=data_type, mode='c', shape=(len(zrange), ny, nx))
    else:
        f = open(scan_name, 'rb')
        f.seek(header_size + np.dtype(data_type).itemsize * nx * ny * zrange[0])
        if verbose:
            print('reading volume... from byte %d' % f.tell())
        # read the payload
        payload = f.read(np.dtype(data_type).itemsize * len(zrange) * ny * nx)
        if pack_binary:
            data = np.unpackbits(np.fromstring(payload, data_type))[:len(zrange) * ny * nx]
        else:
            data = np.fromstring(payload, data_type)
        # convert the payload into actual 3D data
        data = np.reshape(data.astype(data_type), (len(zrange), ny, nx), order='C')
        f.close()
    # HP 10/2013 start using proper [x,y,z] data ordering
    data_xyz = data.transpose(2, 1, 0)
    return data_xyz
