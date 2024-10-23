import numpy as np
import matplotlib.pyplot as plt

areas = np.array([1200, 1450, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600, 3800, 4000, 4200, 4400, 4600, 4800, 5000, 5200, 5400, 5600, 5800, 6000])
prices =np.array([850, 980, 1100, 1250, 1400, 1550, 1700, 1850, 2000, 2150, 2300, 2450, 2600, 2750, 2900, 3050, 3200, 3350, 3500, 3650, 3800, 3950, 4100, 4250, 4400])
areas_normalized = (areas - np.min(areas)) / (np.max(areas) - np.min(areas))

w_ini=b_ini=0
p=1
n=len(areas)
for i in range(1000):
    y_pred=w_ini*(areas_normalized)+b_ini
    cost=(1/(2*n))*sum(((prices)-y_pred)**2)
    dw=-(1/n)*sum((areas_normalized)*((prices)-y_pred))
    db=-(1/n)*sum((prices)-y_pred)
    w_ini=w_ini-p*dw
    b_ini=b_ini-p*db
    print(f"w:{w_ini} b:{b_ini} cost:{cost} iterations no:{i}")
print(f"the value suitable for w is w:{w_ini} adn b is b:{b_ini}")
x=float(input("what is the area of the house you would like to buy? "))
x_normalized = (x - np.min(areas)) / (np.max(areas) - np.min(areas))
y=w_ini*x_normalized+b_ini
print(f"the house would cost around {y} $")



