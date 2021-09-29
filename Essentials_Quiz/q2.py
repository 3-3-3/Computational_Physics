import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sc

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

def converge_to_golden(tolerance, f_n1=1, f_n2=1, term=1):
    """
    Determine how many terms are necessary to converge to the golden ratio given a certain tolerance
    Returns which term is the first to approximate the golden ratio to the  correct term
    """
    f_n = f_n1 + f_n2
    golden_approx = f_n/f_n1
    print(golden_approx - sc.golden)

    if np.abs(golden_approx - sc.golden) <= tolerance:
        return term+1
    else:
        return converge_to_golden(tolerance, f_n1=f_n, f_n2=f_n1, term=term+1)


if __name__ == '__main__':
    R_1 = (golden_ratio(30),1,1)
    R_2 = (golden_ratio(30, a_1=1, a_2=3),1,3) #Lucas Numbers
    R_3 = (golden_ratio(30, a_1=11,a_2=19),11,19)
    R_4 = (golden_ratio(30, a_1=513, a_2=2011),513,2011)

    x = np.arange(10)


    for i in [R_1, R_2, R_3, R_4]:
        plt.plot(x,i[0],label=f'$a_1 = {i[1]}$, $a_2 = {i[2]}$')
        plt.scatter(x,i[0])
    plt.plot(x,np.ones(10)*((1+np.sqrt(5))/2))
    plt.title('Convergence to $\phi$ For $\\frac{F_{n+1}}{F_n}$')
    plt.ylabel('$\\frac{F_{n+1}}{F_n}$')
    plt.xlabel('$n$')
    plt.legend()
    plt.savefig('Golden_Ratio.png')
    plt.show()
