import math
import matplotlib.pyplot as plt
import numpy as np


class oсtagon: 
    def __init__(self,side):  
        self.side=side  
        self.angle=135 
        self.k=1+math.sqrt(2)


    def opis_circle(self):
        radius_opis = self.side * math.sqrt(( 4 + 2 * math.sqrt(2) ) / 4)
        square_opis = math.pi * radius_opis**2
        return radius_opis, square_opis


    def vpis_circle(self):
        radius_vpis = (( 1 + math.sqrt(2) ) / 2) * self.side
        square_vpis = radius_vpis**2 * math.pi
        return radius_vpis, square_vpis


    def Octagon_data(self):
        perimeter = self.side * 8
        square_oktagon = 2 * (1 + math.sqrt(2)) * self.side**2
        return perimeter, square_oktagon


    def draw(self):
        radius_opis, _ = self.opis_circle()
        radius_vpis, _ = self.vpis_circle()
        figure, ax = plt.subplots(figsize=(10, 10))
        circle_opis = plt.Circle((0, 0), radius_opis, color="red", fill=False, label="Описанная окр.")
        ax.add_patch(circle_opis)
        circle_vpis = plt.Circle((0, 0), radius_vpis, color="blue", fill=False, label="Вписанная окр.")
        ax.add_patch(circle_vpis)
        angles = np.linspace(0, 2 * np.pi, 8, endpoint=False) + np.pi / 8
        x = radius_opis * np.cos(angles)
        y = radius_opis * np.sin(angles)
        x = np.append(x, x[0])
        y = np.append(y, y[0])
        ax.plot(x, y, color="black", linewidth=2, label="Октагон")
        ax.set_aspect("equal")

        plt.show()