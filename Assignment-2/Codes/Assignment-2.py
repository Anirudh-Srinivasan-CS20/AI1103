#SIMULATION OF ASSIGNMENT-2 QUESTION - GATE 2021 CSE Q18
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon 

no_of_samples = 100000  
R = expon.rvs(scale = 0.5,  size = no_of_samples )
ctr = 0

for x in range(no_of_samples):
  if R[x]>0.5:
   ctr = ctr + 1
simu_prob = ctr/no_of_samples
theo_prob = 1/math.exp(1)
print("Pr(X>0.5) through simulation is ",simu_prob)
print("Pr(X>0.5) through theory is ",theo_prob)

#plotting

cases = ['']
x = np.arange(len(cases))
plt.bar(x + 0.00, theo_prob, color = 'b', width = 0.05, label = 'Theoretical')
plt.bar(x + 0.05, simu_prob, color = 'g', width = 0.05, label = 'Simulated')
plt.xlabel('Theoretical v/s Simulated')
plt.ylabel('Probability')
plt.xticks(x  + 0.05/2,[''])


a = np.arange(0,0.38,0.001)
plt.yticks(a)
plt.ylim([0.35,0.38])
plt.margins(0.01)
plt.grid(b = True, color ='black',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)

plt.legend()
plt.show()