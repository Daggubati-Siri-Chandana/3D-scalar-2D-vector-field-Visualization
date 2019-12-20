import matplotlib.pyplot as plt
from skimage import measure
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import plotly.graph_objects as go
import numpy as np

fname="/Users/daggubatisirichandana/PycharmProjects/MLTechniques/Datavis/Data/A2_Data/Pf42.bin"
limit=3225.42578

file = open(fname, "rb")
# >f collects data in bigIndian float format
print("collecting data ..!")
data = np.fromfile(file, dtype='>f')

max=np.max(data)
min=np.min(data)
for i in range(25000000):
    if(data[i]>=limit):
        data[i]= (data[i]-limit)/(max-limit)
    else:
        data[i]= ((min-data[i])/(limit-min))

grid = np.zeros((500, 500, 100), dtype=np.float32)

# to arrange the data to grid
for x in range(500):
    for y in range(500):
        for z in range(100):
            grid[x, y, z] = data[x + (y * 500) + (z * 250000)]

print("Preforming Marching Cubes")

iv=-0.25 # normalized isovalue
verts,faces,normals,values = measure.marching_cubes_lewiner(grid, iv , spacing=(1, 1, 1))
#vert1,face1,normals,values = measure.marching_cubes_lewiner(grid, -0.25, spacing=(0.1, 0.1, 0.1))

# # skimage.measure.marching_cubes_lewiner(volume, level=None, spacing=(1.0, 1.0, 1.0))
# # volume(M, N, P) array
# # Input data volume to find isosurfaces. Will internally be converted to float32 if necessary.
# #
# # levelfloat
# # Contour value to search for isosurfaces in volume. If not given or None, the average of the min and max of vol is used.
# #
# # spacinglength-3 tuple of floats
# # Voxel spacing in spatial dimensions corresponding to numpy array indexing dimensions (M, N, P) as in volume.
#
#
#
if(iv<0):
     iv=min-iv*(limit-min)
else:
     iv=limit+iv*(max-limit)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
cax=ax.plot_trisurf(verts[:, 0], verts[:,1], faces, verts[:, 2], cmap=plt.cm.PiYG, lw=1)#,vmax=1, vmin=-1)
#ax.plot_trisurf(vert1[:, 0], vert1[:,1], face1, vert1[:, 2], cmap=plt.cm.Reds, lw=1)#,vmax=1, vmin=-1)
fig.colorbar(cax)
ax.set_xticks([0, 100, 200, 300, 400, 500])
ax.set_yticks([0, 100, 200, 300, 400, 500])
ax.set_zticks([0, 20, 40, 60, 80, 100])
ax.set_title( "For pressure isoval : "+str(iv))
plt.tight_layout()
plt.show()
