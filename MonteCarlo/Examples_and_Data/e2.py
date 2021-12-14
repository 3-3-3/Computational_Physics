import numpy as np
import matplotlib.pyplot as plt
from numpy.random import rand

def simulation(n=15, lam=0.01, dt=0.01):
    n_left = n
    p_decay = lam*dt
    n_t = np.array([n_left])

    while n_left > 0:
        n_start = n_left
        for n in range(n_start):
            r = rand()
            if r < p_decay:
                n_left -= 1

        n_t = np.append(n_t, n_left)

    return n_t

def exponential_decay(t, n=15, lam=0.01):
    return n*np.exp(-lam*t)


if __name__ == '__main__':
    largest_x = 0
    dt = 0.01
    sum = np.array([])
    sims = 10
    for _ in range(sims):
        sim = simulation(dt=dt)
        print(sim)

        for i in range(len(sim)):
            if i >= len(sum):
                sum = np.append(sum, sim[i])
            else:
                sum[i] = sum[i] + sim[i]

        plt.plot(np.arange(len(sim))*dt, sim)
        if len(sim) > largest_x:
            largest_x = len(sim)



    average = sum / sims




    plt.plot(np.arange(largest_x)*dt, np.array([exponential_decay(x) for x in np.arange(largest_x)]))
    plt.plot(np.arange(largest_x)*dt, average)
    plt.xlabel('time')
    plt.ylabel('Number of Particles')

    plt.show()
