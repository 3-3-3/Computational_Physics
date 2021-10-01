import numpy as np
import matplotlib.pyplot as plt
import h5py

amp = 5
t_array = np.linspace(0,0.20,num=240)
s_60hz = lambda x : np.sin((60*2*np.pi)*x)
s_wave = amp*np.array([s_60hz(i) for i in t_array])
s_wave = np.random.default_rng().normal(s_wave, amp/5.0, t_array.size)

hdf_file = h5py.File('s_wave.h5', 'w')
data = hdf_file.create_dataset('data', s_wave.shape, dtype='f')
data[:] = s_wave

t = hdf_file.create_dataset('time', data=t_array)
description = hdf_file.create_dataset('log_entry', data='Fake 60hz signal with noise and associated time array')

hdf_file.close()
