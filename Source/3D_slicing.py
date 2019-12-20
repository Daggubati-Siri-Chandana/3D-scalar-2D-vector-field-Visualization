import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

class IndexTracker(object):
    def __init__(self, ax, X, c):
        self.ax = ax


        self.X = X
        self.choice=c
        rows, cols, self.slices = X.shape
        self.ind = self.slices//2
        if choice=="x":
            self.im = ax.imshow(self.X[self.ind, :, :], cmap=plt.cm.ocean)
        elif choice=="y":
            self.im = ax.imshow(self.X[:, self.ind, :], cmap=plt.cm.ocean)
        elif choice=="z":
            self.im = ax.imshow(self.X[:, :, self.ind], cmap=plt.cm.ocean)
        self.update()

    def onscroll(self, event):
        print("%s %s" % (event.button, event.step))
        if event.button == 'up':
            self.ind = (self.ind + 1) % self.slices
        else:
            self.ind = (self.ind - 1) % self.slices
        self.update()

    def update(self):
        if choice=="x":
            self.im.set_data(self.X[self.ind, :, :])
            ax.set_ylabel('Z axis')
            ax.set_xlabel('Y axis')
        elif choice=="y":
            self.im.set_data(self.X[:, self.ind, :])
            ax.set_ylabel('Z axis')
            ax.set_xlabel('X axis')
        elif choice=="z":
            self.im.set_data(self.X[:, :, self.ind])
            ax.set_ylabel('Y axis')
            ax.set_xlabel('X axis')
        ax.set_title('use scroll wheel to navigate images\nslice %s' % self.ind)
        self.im.axes.figure.canvas.draw()

fname="/Users/daggubatisirichandana/PycharmProjects/MLTechniques/Datavis/Data/Pf01.bin"
file = open(fname, "rb")
# >f collects data in bigIndian float format
print("collecting data ..!")
data = np.fromfile(file, dtype='>f')
grid = np.zeros((500, 500, 100), dtype=np.float32)

for x in range(500):
    for y in range(500):
        for z in range(100):
            grid[x, y, z] = data[x + (y * 500) + (z * 250000)]

#m1 = np.rot90(grid, axes=(0,1))#rotation about x axes
#m2 = np.rot90(grid, axes=(1,2))#rotation about y axes
m3 = ndimage.rotate(grid, angle=0, axes=(0,2))#rotation about z axes

print("Enter dimension you want to traverse: ")
print("\nx - X axis\ny - Y axis \nz - Z axis")
choice = input(">>> ").lower().rstrip()
d = int(input("Enter angle you want to traverse (in deg): "))
if choice=="x":
    m = ndimage.rotate(grid, angle=d, axes=(0,1))
elif choice=="y":
    m = ndimage.rotate(grid, angle=d, axes=(1,2))
elif choice=="z":
    m = ndimage.rotate(grid, angle=d, axes=(0,2))

fig, ax = plt.subplots(1, 1)
tracker = IndexTracker(ax, m, choice)


fig.canvas.mpl_connect('scroll_event', tracker.onscroll)
plt.show()
