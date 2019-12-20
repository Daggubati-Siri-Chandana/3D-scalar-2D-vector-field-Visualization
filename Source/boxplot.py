import numpy as np
import matplotlib.pyplot as plt

l=[]
for i in range(1,49):
    name="/Users/daggubatisirichandana/PycharmProjects/MLTechniques/Datavis/Data/pressure/Pf"+str(i)+".bin"

    file = open(name, "rb")
    data = np.fromfile(file, dtype='>f')
    p =[i for i in data if i<=3225.42578 ]
    print(np.std(p))
    ''' l.append(p)
    plt.boxplot(l)
    plt.show()'''


