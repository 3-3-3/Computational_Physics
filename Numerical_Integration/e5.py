import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    t_array = np.loadtxt('acceleration_data.txt', usecols=0)
    a_array = np.loadtxt('acceleration_data.txt', usecols=1)

    v_array = np.array([np.trapz(a_array[0:i], t_array[0:i]) for i in range(len(a_array))]) + 1.28
    #If this were a huge dataset it would be more efficient to add each change instead of computing the entire integral each optimize
    x_array = np.array([np.trapz(v_array[0:i], t_array[0:i]) for i in range(len(v_array))])


    print(f'Final approximate position: {x_array[-1]}')
    plt.scatter(t_array, a_array, label='Acceleration')
    plt.scatter(t_array, v_array, label='Velocity')
    plt.scatter(t_array, x_array, label='Position')
    plt.legend()
    plt.title('Acceleration, Velocity, and Position of Racecar')
    plt.xlabel('Time (Seconds)')
    plt.show()
