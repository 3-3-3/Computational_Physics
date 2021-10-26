import matplotlib.pyplot as plt
import scipy.constants as sc
import numpy as np

def euler_pendulum(th_0, l, tau, periods=5, om_0=0.0):
    '''
    th_0: Starting position of Pendulum
    l: length of Pendulum
    om_0: initial angular velocity of pendulum
    '''
    th_old = th_0
    om = om_0
    t = 0.0

    th_array = np.array([th_old])
    om_array = np.array([om])
    t_array = np.array([t])
    me_array = np.array([0.5*(l*om)**2 + sc.g*l*(1-np.cos(th_old))])

    T_est = 2*np.pi*np.sqrt(l/sc.g)
    t_max = T_est*periods


    while t < t_max:
        th = th_old + om * tau
        om = om - sc.g / l * np.sin(th_old) * tau
        print(f'Omega: {om}')
        me = 0.5 * (l * om)**2 + sc.g * l * (1 - np.cos(th_old)) #mechanical energy of system per unit mass


        th_old = th
        t = t + tau

        th_array = np.append(th_array, th)
        om_array = np.append(om_array, om)
        me_array = np.append(me_array, me)
        t_array = np.append(t_array, t)

    return (th_array, om_array, me_array, t_array)

if __name__ == '__main__':
    fig, (ax1, ax2) = plt.subplots(2,1)
    th_array, om_array, me_array, t_array = euler_pendulum(np.pi/6, 10, tau=0.001)
    ax1.plot(t_array, th_array)
    ax1.set_title('Angluar Position')
    ax2.plot(t_array, me_array)
    ax2.set_title('Mechanical Energy')
    plt.show()
