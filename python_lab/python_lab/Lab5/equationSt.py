# Enter the coordinates of two points on the cartesian plane. Find the equation of the straight line passing through these points.
# Hint: Eqn is (x-x1) = ((x1-x2)/(y1-y2)) (y-y1)
t1=(3,4)
t2=(4,5)
m =(t2[1]-t1[1])/(t2[0]-t1[0])
print(f"Equation of straight line  is : y-{t1[1]}={m} (x-{t1[0]})")
