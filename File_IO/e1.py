import numpy as np
import matplotlib.pyplot as plt
import random

amp = 5
t_array = np.linspace(0,0.20,num=240)
s_60hz = lambda x : np.sin((60*2*np.pi)*x)
s_wave = amp*np.array([s_60hz(i) for i in t_array])

s_wave = np.random.default_rng().normal(s_wave, amp/5.0, t_array.size)
np.savez('s_wave.npz', t_array, s_wave)
