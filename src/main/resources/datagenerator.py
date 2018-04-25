import random

datafile = open('randominput.dat', 'w')
print('n = 100', file=datafile)

for i in range(100):
    print(random.uniform(0, 10), random.uniform(0, 1), random.uniform(0, 1), 
          random.uniform(0, 1), random.uniform(0, 1), file=datafile)

datafile.close()
