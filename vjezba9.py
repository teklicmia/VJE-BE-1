import numpy as np
import matplotlib.pyplot as plt

G = 6.67408e-11                
M_s = 1.989e30                 
M_z = 5.9742e24                
AU = 1.486e11                  
v0 = 29783                     
T_year = 365.242 * 24 * 3600   

r_s = np.array([0.0, 0.0])         
v_s = np.array([0.0, 0.0])          

r_z = np.array([AU, 0.0])           
v_z = np.array([0.0, v0])           

dt = 60 * 60                         
N = int(T_year / dt)               

r_s_list = []
r_z_list = []

for _ in range(N):
    r = r_z - r_s
    dist = np.linalg.norm(r)
    force = -G * M_s * M_z / dist**3 * r

    a_s = force / M_s
    a_z = -force / M_z

    v_s += a_s * dt
    v_z += a_z * dt
    r_s += v_s * dt
    r_z += v_z * dt

    r_s_list.append(r_s.copy())
    r_z_list.append(r_z.copy())

r_s_arr = np.array(r_s_list)
r_z_arr = np.array(r_z_list)

plt.figure(figsize=(8, 8))
plt.plot(r_s_arr[:, 0], r_s_arr[:, 1], label="Sunce", color='orange')
plt.plot(r_z_arr[:, 0], r_z_arr[:, 1], label="Zemlja", color='blue')
plt.scatter(0, 0, color='orange', marker='o', s=100, label="Početak (Sunce)")
plt.axis('equal')
plt.title("Putanja Zemlje oko Sunca (Eulerova metoda)")
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.grid(True)
plt.legend()
plt.show()
