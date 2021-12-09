import matplotlib.pylab as plot
import math

x = float(input("Enter starting x-coordinate: "))
y = float(input("Enter starting y-coordinate: "))
u = float(input("Enter starting velocity in meters per second: "))
angle = float(input("Enter starting angle from 0 to 90 degrees: "))

print("Running projectile motion. Will stop when projectile reaches y=0")

# process odd angles
while angle >= 360:
    angle -= 360
if angle > 180 and angle < 360:
    angle -= 180

ux = u * math.cos(math.radians(angle))
uy = u * math.cos(math.radians(angle))
t = 0

while y > 0 and uy >= 0:
    t += 0.1
    t = round(t, 3)
    x = x + (ux * t)
    y = y + (uy * t) + (0.5 * -9.81 * t**2)

    vX = ux
    vY = uy - (9.81 * t)

    print("t = "+str(t)+" seconds: x = "+str(x)+", y = "+str(y)+", vX = "+str(vX)+", vY = "+str(vY))
    plot.scatter(x, y, color='red', marker='o')

   



plot.show() 

