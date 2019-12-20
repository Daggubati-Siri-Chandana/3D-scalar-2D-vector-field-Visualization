import plotly.graph_objects as go
import numpy as np


fname="/Users/daggubatisirichandana/PycharmProjects/MLTechniques/Datavis/Data/A2_Data/Pf42.bin"
limit=3225.42578

file = open(fname, "rb")
# >f collects data in bigIndian float format
print("collecting data ..!")
data = np.fromfile(file, dtype='>f')

grid = np.zeros((500, 500, 100), dtype=np.float32)

# to arrange the data to grid
for x in range(500):
    for y in range(500):
        for z in range(100):
            grid[x, y, z] = data[x + (y * 500) + (z * 250000)]
print("collected data ..!")
X, Y, Z = np.meshgrid(np.array(range(500)), np.array(range(500)), np.array(range(100)))

fig = go.Figure(data=go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=grid.flatten(),
    surface_count=3, # number of isosurfaces, 2 by default: only min and max
    colorbar_nticks=3, # colorbar ticks correspond to isosurface values
    caps=dict(x_show=False, y_show=False)
    ))
fig.show()
