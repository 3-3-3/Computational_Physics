import matplotlib.pyplot as plt
import scipy.constants as sc
import numpy as np

def euler_aprox(y_0, m, c_d, rho, A, tau):
    '''
    y_0: initial height of object
    m: mass of object
    c_d: drag coefficient
    rho: density of fluid
    A: cross sectional area of object
    returns tuple of: (y_array, v_array, t_array)
    '''

    y_old = y_0
    v = 0.0
    t = 0.0

    y_array = np.array([y_old])
    v_array = np.array([v])
    t_array = np.array([t])

    while (y_old > 0):
        y = y_old + v*tau
        a = (-m*sc.g+0.5*c_d*rho*A*v**2)/m #Acceleration, dependent on gravitational and drag forces
        v = v + a*tau

        y_old = y
        t = t + tau

        y_array = np.append(y_array, y)
        v_array = np.append(v_array, v)
        t_array = np.append(t_array, t)

    return (y_array, v_array, t_array)

if __name__ == '__main__':
    y_0 = 100
    tau = 0.05
    rho = 1.2 #Assumed density of air
    c_d = 0.5
    A = np.pi*0.15**2

    y_m1, v_m1, t_m1 = euler_aprox(y_0, 100, c_d, rho, A, tau)
    y_m2, v_m2, t_m2 = euler_aprox(y_0, 1, c_d, rho, A, tau)

    fig, (ax1, ax2) = plt.subplots(2,1)

    ax1.scatter(t_m1, y_m1, marker='.')
    ax1.scatter(t_m1, v_m1, marker='.')
    ax1.set_title('Velocity and Position of Sphere With Mass 100 kg')


    ax2.scatter(t_m2, y_m2, marker='.')
    ax2.scatter(t_m2, v_m2, marker='.')
    ax2.set_title('Velocity and Position of Sphere With Mass 1 kg')
    ax2.set_xlabel('Time')

    plt.show()
