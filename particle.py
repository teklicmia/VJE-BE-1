import math
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, v0, theta, x0=0, y0=0):
        self.v0 = v0
        self.theta = math.radians(theta)
        self.x0 = x0
        self.y0 = y0
        self.g = 9.81
        self.reset()

    def reset(self):
        self.x = self.x0
        self.y = self.y0
        self.vx = self.v0 * math.cos(self.theta)
        self.vy = self.v0 * math.sin(self.theta)
        self.t = 0
        self.x_vals = [self.x]
        self.y_vals = [self.y]

    def __move(self, dt):
        self.t += dt
        self.x += self.vx * dt
        self.vy -= self.g * dt
        self.y += self.vy * dt
        self.x_vals.append(self.x)
        self.y_vals.append(self.y)

    def range(self, dt=0.01):
        self.reset()
        while self.y >= 0:
            self.__move(dt)
        return self.x_vals[-1]

    def plot_trajectory(self, dt=0.01):
        self.reset()
        while self.y >= 0:
            self.__move(dt)
        plt.plot(self.x_vals, self.y_vals)
        plt.xlabel('x (m)')
        plt.ylabel('y (m)')
        plt.title('Putanja čestice')
        plt.grid()
        plt.show()
