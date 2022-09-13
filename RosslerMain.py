import numpy as np
import matplotlib.pyplot as plt
a = 0.2
b = 0.2
c = 5
t = 0
T = 200
h = 0.01
def derivative(r,t):
    x = r[0]
    y = r[1]
    z = r[2]
    return np.array([- y - z, x + a * y, b + z * (x - c)])
time = np.array([])
x = np.array([])
y = np.array([])
z = np.array([])
r = np.array([1.000, 1.000, 1.000])
while t <= T :
    
        time = np.append(time, t)
        z = np.append(z, r[2])
        y = np.append(y, r[1])
        x = np.append(x, r[0])
        
        k1 = h*derivative(r,t)
        k2 = h*derivative(r+k1/2,t+h/2)
        k3 = h*derivative(r+k2/2,t+h/2)
        k4 = h*derivative(r+k3,t+h)
        r += (k1+2*k2+2*k3+k4)/6
        
        t = t + h
fig = plt.figure(figsize = (8,8),dpi=100)
ax = plt.axes(projection='3d')
ax.grid()

ax.plot3D(x, y, z)
ax.set_title(r' $r_{o} = (1,1,1)$, $a=0.2, b=0.2, c=5$')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
fig.tight_layout()
plt.show()
fig.savefig('Rossler_13d.png',layout='tight')

plt.rcParams.update({'font.size': 10})  
fig, (ax1, ax2,ax3) = plt.subplots(3, 1,figsize=(8,8))
ax1.plot(np.arange(0,200.01,0.01),x)
ax1.set_title(r'Time Series for x coordinate')
ax1.set_xlabel(r'$t$')
ax1.set_ylabel('x')


ax2.plot(np.arange(0,200.01,0.01),y)
ax2.set_title(r'Time Series for y coordinate')
ax2.set_xlabel(r'$t$')
ax2.set_ylabel('x')
fig.tight_layout()

ax3.plot(np.arange(0,200.01,0.01),z)
ax3.set_title(r'Time Series for z coordinate')
ax3.set_xlabel(r'$t$')
ax3.set_ylabel('z')
fig.tight_layout()
fig.savefig('Rossler_1dt.png')
plt.show()