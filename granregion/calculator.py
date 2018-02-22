import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter

def main():
    calculate_c();

def calculate_c():
    r = 0.5;
    n_p = 1.135;
    g = 9.8;

    d1 = 3;
    d2 = 4;
    d3 = 6;

    q1_7 = 17;
    q2_7 = 36;
    q3_7 = 101;

    q1_14 = 18;
    q2_14 = 37;
    q3_14 = 114;

    c = np.arange(0,d1/r,0.05);

    diff1_7 = np.absolute(n_p*np.sqrt(g)*np.power((d1-c*r),2.5)-q1_7);
    diff2_7 = np.absolute(n_p*np.sqrt(g)*np.power((d2-c*r),2.5)-q2_7);
    diff3_7 = np.absolute(n_p*np.sqrt(g)*np.power((d3-c*r),2.5)-q3_7);
    diff1_14 = np.absolute(n_p*np.sqrt(g)*np.power((d1-c*r),2.5)-q1_14);
    diff2_14 = np.absolute(n_p*np.sqrt(g)*np.power((d2-c*r),2.5)-q2_14);
    diff3_14 = np.absolute(n_p*np.sqrt(g)*np.power((d3-c*r),2.5)-q3_14);

    error = diff1_7 + diff2_7 + diff3_7 + diff1_14 + diff2_14 + diff3_14;

    min_index = min(enumerate(error), key=itemgetter(1))[0];

    print(diff1_7[min_index])
    print(diff2_7[min_index])
    print(diff3_7[min_index])
    print(diff1_14[min_index])
    print(diff2_14[min_index])
    print(diff3_14[min_index])
    print(c[min_index])

    plt.plot(c, error, 'ro')
    plt.xlabel('c')
    plt.ylabel('Error')
    plt.show()


if __name__ == "__main__":
    main()
