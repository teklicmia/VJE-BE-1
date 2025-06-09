import numpy as np
import matplotlib.pyplot as plt

class HarmonicOscillator:
    def __init__(self, m, k, x0, v0):
        self.m = m
        self.k = k
        self.x0 = x0
        self.v0 = v0
        self.omega = np.sqrt(k / m)

    def analytical_solution(self, t):
        A = self.x0
        B = self.v0 / self.omega
        x = A * np.cos(self.omega * t) + B * np.sin(self.omega * t)
        v = -A * self.omega * np.sin(self.omega * t) + B * self.omega * np.cos(self.omega * t)
        a = -self.omega**2 * x
        return x, v, a

    def numerical_solution(self, T, dt):
        N = int(T / dt)
        t = np.linspace(0, T, N)
        x = np.zeros(N)
        v = np.zeros(N)
        a = np.zeros(N)

        x[0] = self.x0
        v[0] = self.v0
        a[0] = -self.k / self.m * x[0]

        for i in range(1, N):
            a[i-1] = -self.k / self.m * x[i-1]
            v[i] = v[i-1] + a[i-1] * dt
            x[i] = x[i-1] + v[i-1] * dt
            a[i] = -self.k / self.m * x[i]

        return t, x, v, a
    
#2 zadatak    
    def calculate_numerical_period(self, T, dt):
        t, x, _, _ = self.numerical_solution(T, dt)
        zero_crossings = []

        for i in range(1, len(x)):
            if x[i-1] <= 0 < x[i] or x[i-1] >= 0 > x[i]:
                t_zero = t[i-1] + (0 - x[i-1]) * (t[i] - t[i-1]) / (x[i] - x[i-1])
                zero_crossings.append(t_zero)

        if len(zero_crossings) < 2:
            return None  

        periods = [zero_crossings[i+2] - zero_crossings[i] for i in range(len(zero_crossings) - 2)]
        return np.mean(periods)


if __name__ == "__main__":

    m = 1.0
    k = 1.0
    x0 = 1.0
    v0 = 0.0
    T = 20
    dt_values = [0.5, 0.1, 0.01]

    osc = HarmonicOscillator(m, k, x0, v0)

    for dt in dt_values:
        t, x, v, a = osc.numerical_solution(T, dt)
        x_exact, v_exact, a_exact = osc.analytical_solution(t)

        plt.figure(figsize=(12, 8))
        plt.suptitle(f'Rezultati za ∆t = {dt}')

        plt.subplot(3, 1, 1)
        plt.plot(t, x, label='Numerički', linestyle='--')
        plt.plot(t, x_exact, label='Analitički', alpha=0.7)
        plt.ylabel('Položaj x(t)')
        plt.legend()

        plt.subplot(3, 1, 2)
        plt.plot(t, v, label='Numerički', linestyle='--')
        plt.plot(t, v_exact, label='Analitički', alpha=0.7)
        plt.ylabel('Brzina v(t)')
        plt.legend()

        plt.subplot(3, 1, 3)
        plt.plot(t, a, label='Numerički', linestyle='--')
        plt.plot(t, a_exact, label='Analitički', alpha=0.7)
        plt.xlabel('Vrijeme t')
        plt.ylabel('Ubrzanje a(t)')
        plt.legend()

        plt.tight_layout()
        plt.show()

#2 zadatak
        print("Ispitivanje preciznosti perioda za različite ∆t:\n")
    T_exact = 2 * np.pi * np.sqrt(m / k)

    for dt in dt_values:
        T_num = osc.calculate_numerical_period(T=20, dt=dt)
        if T_num is not None:
            greska = abs(T_num - T_exact)
            print(f"∆t = {dt:.3f} → T_num = {T_num:.5f}, T_exact = {T_exact:.5f}, greška = {greska:.5e}")
        else:
            print(f"∆t = {dt:.3f} → Nije moguće izračunati period.")

