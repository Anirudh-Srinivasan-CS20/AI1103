
#SIMULATION OF ASSIGNMENT-1 QUESTION - 5.10
import random as rd
import numpy as np
import matplotlib.pyplot as plt

sample_data = 500000

list_of_faces = [-1, -1, -1, -1, -1, -1]
i=0
while i<3:
  temp = rd.randint(0, 5)
  if(list_of_faces[temp] == -1):
    list_of_faces[temp] = 0
    i+=1
i=0
while i<2:
  temp = rd.randint(0, 5)
  if(list_of_faces[temp] == -1):
    list_of_faces[temp] = 1
    i+=1
i=0
while i<1:
  temp = rd.randint(0, 5)
  if(list_of_faces[temp] == -1):
    list_of_faces[temp] = 2
    i+=1
count_1 = count_2 = count_5 = 0 

# 0 corresponds to face with 1
# 1 corresponds to face with 2
# 2 corresponds to face with 5

for i in range(sample_data):
  temp = rd.randint(0, 5)
  if(list_of_faces[temp] == 0):
    count_1 += 1
  elif(list_of_faces[temp] == 1):
    count_2 += 1
  else:
    count_5 += 1

prob_1 = count_1 / sample_data
prob_2 = count_2 / sample_data
prob_5 = count_5 / sample_data

mean = prob_1*1 + prob_2*2 + prob_5*5;

print("Following results are obtained from the simulation")
print("(i) Probability that face with 1 is obtained is: {}".format(prob_1))
print("(ii) Probability that face with 2 is obtained is: {}".format(prob_2))
print("(iii) Probability that face with 5 is obtained is: {}".format(prob_5))
print()
print("Following results are obtained theoretically")
print("(i) Probability that face with 1 is obtained is: 0.5000000000")
print("(ii) Probability that face with 2 is obtained is: 0.3333333333")
print("(iii) Probability that face with 5 is obtained is: 0.1666666667")
print()
print("Following are the absolute errors in calculating probabilties")
print("(i) Absolute error in calculating probability that face with 1 is obtained is: {}".format(abs(prob_1 - 0.5000000000)))
print("(ii) Absolute error in calculating probability that face with 2 is obtained is: {}".format(abs(prob_2 - 0.3333333333)))
print("(iii) Absolute error in calculating probability that face with 5 is obtained is: {}".format(abs(prob_5 - 0.1666666667)))
print()
print("The mean of the numbers obtained on throwing this die obtained from simulation is: {}".format(mean))
print("The mean of the numbers obtained on throwing this die obtained theoretically is: 2")
print("Absolute error in calculating the mean of the numbers obtained on throwing this die is: {}".format(abs(mean - 2)))

#plotting

Number_on_die = ["1","2","5"]

probab_theo = [0.5000000000, 0.3333333333, 0.1666666667]
probab_sim = [prob_1,prob_2,prob_5]

x = np.arange(len(Number_on_die))
plt.bar(x + 0.00, probab_theo, color = 'b', width = 0.25, label = 'Theoretical')
plt.bar(x + 0.25, probab_sim, color = 'g', width = 0.25, label = 'Simulated')
plt.xlabel('Number on the face of die')
plt.ylabel('Probabilities')
plt.xticks(x  + 0.25/2,['1', '2', '5'])
plt.legend()
plt.show()

