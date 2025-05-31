from particle import Particle
import math

v0 = 20  # m/s
theta = 45  # stupnjeva

p = Particle(v0, theta)

num_domet = p.range()
print(f"Numerički domet: {num_domet:.2f} m")

theta_rad = math.radians(theta)
analit_domet = (v0 ** 2) * math.sin(2 * theta_rad) / 9.81
print(f"Analitički domet: {analit_domet:.2f} m")

odstupanje = abs(num_domet - analit_domet)
print(f"Odstupanje: {odstupanje:.4f} m")

p.plot_trajectory()

# Numeričko rješenje se malo razlikuje od analitičkog.
# Odstupanje je 0.0454 m, što je prihvatljivo.


