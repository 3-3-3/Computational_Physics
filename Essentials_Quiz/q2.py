import numpy as np
import matplotlib.pyplot as plt

def fibonacci(n, seq=np.array([1,1])):
    if seq.size == n:
        return seq
    else:
        s = np.append(seq, seq[-1] + seq[-2])
        return fibonacci(n,s)

def golden_ratio(n, a_1=1, a_2=1):
    #The proof of the true value of the golden ratio simply uses the
    #recursive definition of the Fibonacci numbers–the initial numbers
    #should not matter. Therefore, for any a_1, a_2, R_n should
    #converge to the golden ratio
    s = fibonacci(n, seq=np.array([a_1,a_2]))
    return np.array([s[i]/s[i-1] for i in range(1,s.size)])

if __name__ == '__main__':
    R_1 = (golden_ratio(11),1,1)
    R_2 = (golden_ratio(11, a_1=1, a_2=3),1,3) #Lucas Numbers
    R_3 = (golden_ratio(11, a_1=11,a_2=19),11,19)
    R_4 = (golden_ratio(11, a_1=513, a_2=2011),513,2011)

    #This gives the error at each n. The error of the 10th is of the order 10e-4,
    #or four decimal points. This impossible to discern on the graph
    #so it does not make sense to go further.
    #Clearly R_n never reaches the golden ratio because R_n is by
    #Definition rational, while the golden ratio is ironically irrational
    #So determining what counts as "Convergence" depends on the use case
    print(R_4-(1+np.sqrt(5))/2)

    x = np.arange(10)

    for i in [R_1, R_2, R_3, R_4]:
        plt.plot(x,i[0],label=f'$a_1 = {i[1]}$, $a_2 = {i[2]}$')
        plt.scatter(x,i[0])
    plt.plot(x,np.ones(10)*((1+np.sqrt(5))/2))
    plt.title('Convergence to $\phi$ For $\\frac{F_{n+1}}{F_n}$')
    plt.ylabel('$\\frac{F_{n+1}}{F_n}$')
    plt.xlabel('$n$')
    plt.legend()
    plt.show()
