import numpy as np
import matplotlib.pyplot as plt

def euler_oscilator(x_0, v_0, omega, periods=5, tau=0.1, cromer=False):
    '''
    x_0: Initial state of oscilator.
    v_0: Initial velocity (time derivative) of oscilator
    omega: angular frequency
    periods: number of periods to return
    tau: time step
    cromer: use euler-cromer method (True) or just normal euler (False )
    '''

    T = 2*np.pi/omega
    t_max = T*periods

    t = 0
    x = x_0
    v = v_0

    t_array = np.array([t])
    x_array = np.array([x])
    v_array = np.array([v])

    while t < t_max:
        if cromer == True:
            #Update velocity, then use velocity to update position
            a = -omega**2*x
            v = v + a*tau
            x = x + v*tau

        else:
            #update position, then use position to update velocity
            x = x + v*tau
            a = -omega**2*x
            v = v + a*tau

        t = t+tau

        t_array = np.append(t_array, t)
        x_array = np.append(x_array, x)
        v_array = np.append(v_array, v)


    return (t_array, x_array, v_array)

if __name__ == '__main__':
    #If the approximation is consistent with conservation of energy, the peak of position should always be the minimum of velocity, and vice versa
    #This is because the maximum position is the maximal potential energy, which should correspond to the minimum kinetic energy
    #Surprisingly, this seems to work actually. I have done it out to 200 periods and both seems to be conserving energy with a time step of 0.1



    periods = 200
    tau = 0.1

    euler = euler_oscilator(10, 0, 2, periods=periods, tau=tau, cromer=False)
    euler_cromer = euler_oscilator(10, 0, 2, periods=periods, tau=tau, cromer=True)

    x_axis = np.zeros(len(euler[0]))

    fig, (ax1, ax2) = plt.subplots(2, 1)
    ax1.plot(euler[0], euler[1], label='Position')
    ax1.plot(euler[0], euler[2], label='Velocity')
    ax1.plot(euler[0], x_axis, color='black')
    ax1.set_title('Euler Method')
    ax1.legend()

    ax2.plot(euler_cromer[0], euler_cromer[1], label='Position')
    ax2.plot(euler_cromer[0], euler_cromer[2], label='Velocity')
    ax2.plot(euler_cromer[0], x_axis, color='black')
    ax2.set_title('Euler Cromer Method')
    ax2.set_xlabel('Time')
    ax2.legend()




    plt.show()
