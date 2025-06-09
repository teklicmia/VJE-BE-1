import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class ChargedParticle:
    def __init__(self, q, m, E, B, r0, v0):
        self.q = q
        self.m = m
        self.E = np.array(E)
        self.B = np.array(B)
        self.r0 = np.array(r0)
        self.v0 = np.array(v0)

    def simulate(self, dt, T):
        N = int(T / dt)
        r = np.zeros((N, 3))
        v = np.zeros((N, 3))
        t = np.linspace(0, T, N)

        r[0] = self.r0
        v[0] = self.v0

        for i in range(1, N):
            F = self.q * (self.E + np.cross(v[i-1], self.B))
            a = F / self.m
            v[i] = v[i-1] + a * dt
            r[i] = r[i-1] + v[i] * dt

        return r, v, t

if __name__ == "__main__":
    q_e = -1.6e-19    
    q_p = +1.6e-19    
    m = 9.11e-31      
    B = [0, 0, 1e-3]  
    E = [0, 0, 0]     

    r0 = [0, 0, 0]                      
    v0 = [1e5, 1e5, 1e5]                

    dt = 1e-9
    T = 5e-6

    e_particle = ChargedParticle(q_e, m, E, B, r0, v0)
    r_e, _, _ = e_particle.simulate(dt, T)

    p_particle = ChargedParticle(q_p, m, E, B, r0, v0)
    r_p, _, _ = p_particle.simulate(dt, T)

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(r_e[:, 0], r_e[:, 1], r_e[:, 2], label='Elektron', color='blue')
    ax.plot(r_p[:, 0], r_p[:, 1], r_p[:, 2], label='Pozitron', color='red')

    ax.set_xlabel('x [m]')
    ax.set_ylabel('y [m]')
    ax.set_zlabel('z [m]')
    ax.set_title('Gibanje elektrona i pozitrona u konstantnom B polju')
    ax.legend()
    plt.show()

#Elektron se giba po lijevoj (negativnoj) spirali u smjeru uz ili niz z-os, ovisno o smjeru 𝑣𝑧,
# a pozitron po desnoj (pozitivnoj) spirali duž 𝑧-osi u suprotnom smjeru u x-y ravnini u odnosu na elektron.