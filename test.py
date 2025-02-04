import fmm_gpu
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def direct_compute(shot, weight):
    potentials = []
    print(shot.shape)
    for i in np.arange(shot.shape[0]):
        print(str(i/shot.shape[0]))
        current_point = shot[i]
        pot = 0
        for j in np.arange(shot.shape[0]):
            if i==j:
                continue
            else:
                R = np.linalg.norm(current_point - shot[j])
                pot += weight[j] / R
        potentials.append(pot)
    return np.asarray(potentials)


num_points = 1633000
num_iter = 1
num_terms = 10
bin_size = 200
theta = 0.001
dodebug = False
for i in np.arange(num_iter):
    print("Run " + str(i+1))
    A = np.random.uniform(0, 1, 3 * num_points)
    A_shot = np.reshape(A,(num_points,3), order='F')
    B = np.random.uniform(0, 1, num_points)
    C = fmm_gpu.bonsai(num_points, A, B, 0.00005, dodebug)
    C = -C

if(dodebug):
    plt.plot(C)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(A_shot[:,0], A_shot[:, 1], A_shot[:,2])
    plt.show()
print("Output " + str(C))