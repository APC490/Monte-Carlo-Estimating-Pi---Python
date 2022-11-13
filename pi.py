import random
import math
import matplotlib.pyplot as plt
import numpy as np
import time

c = 0
t = 0
a = 0
px = np.array([])
py = np.array([])
repititions = 10000

fig, axs = plt.subplots()
axs.set_xscale('log')
axs.set_title('Pi Estimate')
axs.set_xlabel('Runs')
axs.set_ylabel('Pi Estimate')
axs.grid(True)

def main():
    for i in range(0, repititions):
        global axs
        global px
        global py
        global c
        global t
        global x
        global y
        global a
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        x2 = x**2
        y2 = y**2
        pt = math.sqrt(x2 + y2)
        t += 1
        if  pt < 1:
            global c
            c += 1
        a = c/t * 4
        py = np.append(py, a)
        px = np.append(px, t)
        axs.set_title(f"Pi Estimate : {a}")
    pi4 = c/t
    pi = pi4 * 4
    print(pi)
    plt.scatter(px, py)
    plt.show()

main()

