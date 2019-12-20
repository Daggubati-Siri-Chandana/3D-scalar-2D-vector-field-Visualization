import numpy as np
import matplotlib.pyplot as plt

u = open("/Users/daggubatisirichandana/PycharmProjects/MLTechniques/Datavis/Data/A2_Data/Uf42.bin", "rb")
v = open("/Users/daggubatisirichandana/PycharmProjects/MLTechniques/Datavis/Data/A2_Data/Vf42.bin", "rb")

print("collecting data ..!")
dataU = np.fromfile(u, dtype='>f')
dataV = np.fromfile(v, dtype='>f')

gridU = np.zeros((500,500,100), dtype=np.float32)
gridV = np.zeros((500,500,100), dtype=np.float32)

# to arrange the data to grid
for x in range(500):
    for y in range(500):
        for z in range(100):
            gridU[x, y, z] = dataU[x + (y * 500) + (z * 250000)]
            gridV[x, y, z] = dataV[x + (y * 500) + (z * 250000)]

print("\ncollected data of dimensions 500*500*100")
print(".........................................................")

fig, ax = plt.subplots(1, 1)
x, y = np.meshgrid(np.array(range(500)), np.array(range(500)))
ax.streamplot(x,y,gridU[:,:,10][::-1], gridV[:,:,10][::-1], color=gridU[:,:,10][::-1] , cmap=plt.cm.ocean)

plt.show()
