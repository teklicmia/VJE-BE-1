import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, v0, angle_deg, m, k, g=9.81):
        self.v0 = v0
        self.angle = np.radians(angle_deg)
        self.m = m
        self.k = k
        self.g = g

        self.vx0 = v0 * np.cos(self.angle)
        self.vy0 = v0 * np.sin(self.angle)

    def simulate_euler(self, dt, T):
        N = int(T / dt)
        t = np.linspace(0, T, N)
        x = np.zeros(N)
        y = np.zeros(N)
        vx = np.zeros(N)
        vy = np.zeros(N)

        x[0], y[0] = 0, 0
        vx[0], vy[0] = self.vx0, self.vy0

        for i in range(1, N):
            v = np.sqrt(vx[i-1]**2 + vy[i-1]**2)
            ax = -self.k / self.m * v * vx[i-1]
            ay = -self.g - self.k / self.m * v * vy[i-1]

            vx[i] = vx[i-1] + ax * dt
            vy[i] = vy[i-1] + ay * dt
            x[i] = x[i-1] + vx[i-1] * dt
            y[i] = y[i-1] + vy[i-1] * dt

            if y[i] < 0:
                x = x[:i+1]
                y = y[:i+1]
                break

        return x, y
    

    def simulate_rk4(self, dt, T):
        N = int(T / dt)
        x = np.zeros(N)
        y = np.zeros(N)
        vx = np.zeros(N)
        vy = np.zeros(N)

        x[0], y[0] = 0, 0
        vx[0], vy[0] = self.vx0, self.vy0

        for i in range(1, N):
            v = lambda vx, vy: np.sqrt(vx**2 + vy**2)

            def derivatives(vx, vy):
                v_mod = v(vx, vy)
                ax = -self.k / self.m * v_mod * vx
                ay = -self.g - self.k / self.m * v_mod * vy
                return ax, ay

            # k1
            ax1, ay1 = derivatives(vx[i-1], vy[i-1])
            k1_vx = ax1 * dt
            k1_vy = ay1 * dt
            k1_x = vx[i-1] * dt
            k1_y = vy[i-1] * dt

            # k2
            ax2, ay2 = derivatives(vx[i-1] + 0.5*k1_vx, vy[i-1] + 0.5*k1_vy)
            k2_vx = ax2 * dt
            k2_vy = ay2 * dt
            k2_x = (vx[i-1] + 0.5*k1_vx) * dt
            k2_y = (vy[i-1] + 0.5*k1_vy) * dt

            # k3
            ax3, ay3 = derivatives(vx[i-1] + 0.5*k2_vx, vy[i-1] + 0.5*k2_vy)
            k3_vx = ax3 * dt
            k3_vy = ay3 * dt
            k3_x = (vx[i-1] + 0.5*k2_vx) * dt
            k3_y = (vy[i-1] + 0.5*k2_vy) * dt

            # k4
            ax4, ay4 = derivatives(vx[i-1] + k3_vx, vy[i-1] + k3_vy)
            k4_vx = ax4 * dt
            k4_vy = ay4 * dt
            k4_x = (vx[i-1] + k3_vx) * dt
            k4_y = (vy[i-1] + k3_vy) * dt

            # update
            vx[i] = vx[i-1] + (k1_vx + 2*k2_vx + 2*k3_vx + k4_vx)/6
            vy[i] = vy[i-1] + (k1_vy + 2*k2_vy + 2*k3_vy + k4_vy)/6
            x[i] = x[i-1] + (k1_x + 2*k2_x + 2*k3_x + k4_x)/6
            y[i] = y[i-1] + (k1_y + 2*k2_y + 2*k3_y + k4_y)/6

            if y[i] < 0:
                return x[:i+1], y[:i+1]

        return x, y
    
if __name__ == "__main__":
    v0 = 50       
    angle = 45     
    m = 1.0       
    k = 0.1        
    T = 10         

    dt_values = [0.5, 0.1, 0.01, 0.001]

    for dt in dt_values:
        proj = Projectile(v0, angle, m, k)
        x, y = proj.simulate_euler(dt, T)

        plt.plot(x, y, label=f"Δt = {dt}")

    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.title("Kosi hitac s otporom zraka (Eulerova metoda)")
    plt.legend()
    plt.grid(True)
    plt.show()

    v0 = 50        
    angle = 45     
    m = 1.0
    k = 0.1
    T = 10
    dt = 0.01

    proj = Projectile(v0, angle, m, k)
    x_e, y_e = proj.simulate_euler(dt, T)
    x_rk, y_rk = proj.simulate_rk4(dt, T)

    plt.figure(figsize=(10, 6))
    plt.plot(x_e, y_e, label="Eulerova metoda", linestyle='--')
    plt.plot(x_rk, y_rk, label="Runge-Kutta 4. reda", linestyle='-')
    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.title("Usporedba Euler i RK4 metoda za kosi hitac s otporom zraka")
    plt.legend()
    plt.grid(True)
    plt.show()