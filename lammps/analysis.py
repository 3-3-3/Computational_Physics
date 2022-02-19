import numpy as np
import matplotlib.pyplot as plt
import os


def parse(dump):
    #Take path to laamps dump file, return structured data to plot
    data_one = [] #for type one atoms
    data_two = [] #for type two atoms
    time_steps = np.array([])
    with open(dump) as f:
        out = f.readlines()
        i = 0
        step_one = np.array([])
        step_two = np.array([])
        while i < len(out):

            if 'TIMESTEP' in out[i]:
                if step_one.any():
                    data_one.append(step_one)
                    data_two.append(step_two)
                time_steps = np.append(time_steps, int(out[i+1]))

                step_one = np.array([])
                step_two = np.array([])
                i += 9
            else:
                row = out[i].split()
                xy = [[float(row[2]), float(row[3])]]
                #print(xy)
                if row[1] == '1':
                    if step_one.any():
                        step_one = np.append(step_one, xy, axis=0) #xs, ys
                    else:
                        step_one = np.array(xy)
                elif row[1] == '2':
                    if step_one.any():
                        step_two = np.append(step_two, xy, axis=0) #xs, ys
                    else:
                        step_two = np.array(xy)

                else:
                    pass

                i += 1

    return (time_steps, np.array(data_one), np.array(data_two))

if __name__ == '__main__':
    data = parse('dump.lammpstrj')
    print(data[0])
    try:
        os.mkdir('visualization')
    except:
        pass


    for i in range(len(data[0])-1):
        plt.title(f'Timestep: {data[0][i]}')
        plt.scatter(data[1][i].transpose()[0], data[1][i].transpose()[1])
        plt.scatter(data[2][i].transpose()[0], data[2][i].transpose()[1],color='r')
        plt.xlabel('Relative X Position')
        plt.ylabel('Relative Y Position')
        plt.savefig(os.path.join('visualization', f'{data[0][i]}.jpg'))
        plt.show()
