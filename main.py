import csv
import random as rn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

""" def rand_AB(Nmax):
   A_ = []
   B_ = []
   for i in range(0, Nmax):
      A = round(rn.uniform(-D, 0), 3)
      B = round(rn.uniform(-min(A + D, -A), min(A + D, -A)), 3)
      A_.append(A)
      B_.append(B)
   return A_, B_


def strategy(t, A, B):
   x_yng = []
   for i in range(0, Nmax):
      x_yng_ = A[i] + B[i]*np.cos(2*np.pi*t)
      x_yng.append(x_yng_)
   return x_yng

Nmax = 20
D = 120
D0 = 70  
sigma1 = 0.25
sigma2 = 0.0003 """



"""
xy = []
M1 = []
M2 = []
M3 = []
M4 = []
for i in range(0, Nmax):
   A_ = round(rn.uniform(-D, 0), 3)
   B_ = round(rn.uniform(-min(A_ + D, -A_), min(A_ + D, -A_)), 3)
   A.append(A_)
   B.append(B_)

t = np.linspace(0, 1, Nmax)
for i in range(0, len(A)):
   xy_ = A[i] + B[i]*np.cos(2*np.pi*t)
   xy.append(xy_)

d = {'A': A, 'B': B}
data_A_B = pd.DataFrame(data = d)

data_A_B.to_csv("data_A_B.csv", index=False, sep="\t")

for i in range(0, len(A)):
   M1_ = round(sigma1*(A[i] + D), 3)
   M2_ = round(-sigma2*(A[i] + D + B[i]/2), 3)
   M3_ = round(-2*(np.pi*B[i])**2, 3)
   M4_ = round(-((A[i] + D0)**2 + (B[i]**2)/2), 3)
   M1.append(M1_)
   M2.append(M2_)
   M3.append(M3_)
   M4.append(M4_)

e = {'M1': M1, 'M2': M2, 'M3': M3, 'M4': M4}
data_M = pd.DataFrame(data = e)

data_M.to_csv("data_M.csv", index=False, sep="\t")
z = -112.289+ 5.17*np.cos(2*np.pi*t)
plt.plot(t, z)
plt.show()
"""
""" 
AB = rand_AB(Nmax)
t = np.linspace(0, 1, Nmax)
x = strategy(t, AB[0], AB[1]) """

""" 
data_AB = pd.read_csv('data_AB.csv')

Ay = data_AB["A_yng"].tolist()
By = data_AB["B_yng"].tolist()
print(Ay)
print(By) """

alpha_y = 0.0016
alpha_o = 0.006
betta_y = 0.0000007
betta_o = 0.000000075
gamma_y = 0.00008
gamma_o = 0.004
delta_y = 0.000016
delta_o = 0.00006

D = 120
D0 = 70  
sigma1 = 1
sigma2 = 1
Nmax = 100

data_M = pd.read_csv('data_M.csv')
M1 = data_M['M1'].tolist()
M2 = data_M['M2'].tolist()
M3 = data_M['M3'].tolist()
M4 = data_M['M4'].tolist()
M5 = data_M['M5'].tolist()
M6 = data_M['M6'].tolist()
M7 = data_M['M7'].tolist()
M8 = data_M['M8'].tolist()
J = []
for i in range(0, 10):
   r = 0
   s = 0
   p = 0
   q = 0
   r = alpha_o*M5[i] + betta_o*M7[i] + delta_o*M8[i]
   s = gamma_o*M6[i]
   p = alpha_y*M1[i] + betta_y*M3[i] + delta_y*M4[i]
   q = gamma_y*M2[i]
   j_ =  -s - p - q + np.sqrt(4*r*p + (p + q - s)**2)
   J.append(j_)

print(J.sort())