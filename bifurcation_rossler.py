
import math
import numpy as np
import matplotlib.pyplot as plt


a = 0.2
b = 0.2
c = 4.05
x_max = []
x_min= []
y_max = []
y_min = []
z_max = []
z_min = []
r = []

def rk4(x,y):
    k1,l1,m1 = derivative(x,y,z)

    k2,l2,m2 = derivative(x + k1*h/2, y + l1*h/2, z + m1*h/2)

    k3,l3,m3 = derivative(x + k2*h/2, y + l2*h/2, z + m2*h/2)

    k4,l4,m4 = derivative(x + k3*h, y + l3*h, z+l3*h)

    k = (h/6)*(k1 + 2*k2 + 2*k3 + k4)
    l = (h/6)*(l1 + 2*l2 + 2*l3 + l4)
    m = (h/6)*(m1 + 2*m2 + 2*m3 + m4)

    return k,l,m

def derivative(x,y,z):
  dxdt = -y - z
  dydt = x + a*y
  dzdt = b + z*(x - c)
  return dxdt,dydt,dzdt
while c<4.5:

  x = 1.0
  y = 1.0  
  z = 1.0
  t = 0.0
  h = 0.01

  X,Y,Z,T = [],[],[],[]

  dxdt,dydt,dzdt = derivative(x,y,z)

  while t < 400.0:
    
    t = t+h
    k,l,m = rk4(x,y)
    x = x+k
    y = y+l
    z = z+m

    X.append(x),Y.append(y),Z.append(z),T.append(t)
  
  min_x, max_x = [],[]
  min_y, max_y = [],[]
  min_z, max_z = [],[]

  for i in range(20000,(len(X)-1)):
    if(X[i-1] > X[i] < X[i + 1]):
      min_x.append(X[i])
    if(X[i-1] < X[i] > X[i + 1]):
      max_x.append(X[i])
  
  x_max.append(list(set(max_x)))
  x_min.append(list(set(min_x)))

  for i in range(20000,(len(Y)-1)):
    if(Y[i-1] > Y[i] < Y[i + 1]):
      min_y.append(Y[i])
    if(Y[i-1] < Y[i] > Y[i + 1]):
      max_y.append(Y[i])
  
  y_max.append(list(set(max_y)))
  y_min.append(list(set(min_y)))

  for i in range(20000,(len(Z)-1)):
    if(Z[i-1] > Z[i] < Z[i + 1]):
      min_z.append(Z[i])
    if(Z[i-1] < Z[i] > Z[i + 1]):
      max_z.append(Z[i])
  
  z_max.append(list(set(max_z)))
  z_min.append(list(set(min_z)))
  
  r.append(c)
  c = c+0.0002

fig = plt.figure(dpi=100)

for i in range(len(x_max)):
  plt.scatter([r[i] for j in range(len(x_max[i]))],x_max[i],s=0.05,c='black', marker = '.')
plt.title('Rossler System for a=0.2, b=0.2')
plt.xlabel('c')
plt.ylabel('x')
fig.tight_layout()
plt.show()
fig.savefig('bif2.png')
