#SIMULATION OF ASSIGNMENT-3 GATE 2006 MA Q16
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

no_of_samples = 5000000
data_x = poisson.rvs(1,size = no_of_samples )
data_y = poisson.rvs(2, size = no_of_samples )
ctr_x = 0
ctr_y = 0
ctr_z = 0

for i in range(no_of_samples):
  if data_x[i] == 1:
   ctr_x = ctr_x + 1

for i in range(no_of_samples):
  if data_y[i] == 3:
   ctr_y = ctr_y + 1

for i in range(no_of_samples):
  if data_x[i] + data_y[i] == 4:
   ctr_z = ctr_z + 1

   prob_x1 = ctr_x/no_of_samples
   prob_y3 = ctr_y/no_of_samples
   prob_z4 = ctr_z/no_of_samples

   simu_prob = prob_x1*prob_y3/prob_z4
   theo_prob = 32/81
print("Pr(X=1|X+Y=4) through simulation is ",simu_prob)
print("Pr(X=1|X+Y=4) through theory is ",theo_prob) 

#plotting

cases = ['']
x = np.arange(len(cases))
plt.bar(x + 0.00, theo_prob, color = 'b', width = 0.05, label = 'Theoretical')
plt.bar(x + 0.05, simu_prob, color = 'g', width = 0.05, label = 'Simulated')
plt.xlabel('Theoretical v/s Simulated')
plt.ylabel('Probability')
plt.xticks(x  + 0.05/2,[''])


a = np.arange(0,0.40,0.001)
plt.yticks(a)
plt.ylim([0.38,0.40])
plt.margins(0.01)
plt.grid(b = True, color ='black',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)

plt.legend()
plt.show()