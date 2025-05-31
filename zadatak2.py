import matplotlib.pyplot as plt
from particle import Particle
import math


v0 = 10  # m/s
theta = 60  # stupnjeva


theta_rad = math.radians(theta)
analit_domet = (v0 ** 2) * math.sin(2 * theta_rad) / 9.81


dt_values = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.02, 0.05, 0.1]
rel_errors = []


for dt in dt_values:
    p = Particle(v0, theta)
    num_domet = p.range(dt=dt)
    rel_error = abs(num_domet - analit_domet) / analit_domet * 100  # %
    rel_errors.append(rel_error)
    print(f"dt = {dt:.4f} -> pogreška = {rel_error:.4f}%")


plt.figure()
plt.plot(dt_values, rel_errors, marker='o')
plt.xlabel("Vremenski korak Δt (s)")
plt.ylabel("Relativna pogreška (%)")
plt.title("Relativna pogreška dometa u ovisnosti o Δt")
plt.grid(True)
plt.xscale('log')  
plt.yscale('log')
plt.tight_layout()
plt.show()

