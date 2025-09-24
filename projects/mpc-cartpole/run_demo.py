#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from src.controllib.lqr import lqr

# simple linearized cart-pole example constants (toy)
A = np.array([[0,1,0,0],
              [0,0,-0.1818,0],
              [0,0,0,1],
              [0,0,2.6727,0]])
B = np.array([[0],
              [1.818],
              [0],
              [-2.727]])
Q = np.eye(4)
R = np.array([[0.01]])
K = lqr(A,B,Q,R)

print("LQR gain K = ", K)

# simulate linear closed-loop on small time horizon
x0 = np.array([0.1,0,0.05,0])
dt = 0.02
t = np.arange(0,5,dt)
x = x0.copy()
X = []
for _ in t:
    u = -K.dot(x)
    x = x + dt*(A.dot(x) + B.dot(u))
    X.append(x.copy())
X = np.array(X)

plt.figure()
plt.plot(t, X[:,0], label='cart pos')
plt.plot(t, X[:,2], label='pole angle')
plt.legend()
plt.xlabel('time (s)')
plt.title('LQR closed-loop (toy)')
plt.savefig('projects/mpc-cartpole/results_demo.png')
print('Saved projects/mpc-cartpole/results_demo.png')
