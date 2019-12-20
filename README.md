# Data Visualization Assignment 2


### Introduction

This is a Python implementation of [3D scalar/2D vector field visualization]

### Requriments

- Make sure you have python 3 version installed in your system

- Using pip Install OpenCV - is a library of programming functions mainly aimed at real-time computer vision. The library is cross-platform and free for use under the open-source BSD license. OpenCV supports the deep learning frameworks TensorFlow, Torch/PyTorch, and Caffe.

- Install numpy - is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

- Install matplotlib - is a plotting library for the Python programming language and its numerical mathematics extension NumPy. It provides an object-oriented API for embedding plots into applications.

- Install scipy : is a free and open-source Python library used for scientific computing and technical computing. SciPy contains modules for optimization, interpolation, matrix rotation functions, signal and image 

- Install skimage : Image Processing SciKit (Toolbox for SciPy)

- when you install these a virtual environment will be created and whenever we import few functions from packages the executables get stored in _pycache_ folder

### Datasets

The data set used is a simulation of a hurricane from the National Center for Atmospheric Research in the United States. The data is in ”Brick-of-Floats” format within binary file provided with the variable name. It consists of a volume of data values at each position in space. The three- dimensional array of data consists of planes of x-y values in ascending z-order; in the data, the x values vary fastest. Assuming the data was stored as a one-dimensional array, the index into that array for the point x, y, z would be:
index=x+dimx*(y+dimy*z) 

dataset link - http://sciviscontest-staging.ieeevis.org/2004/data.html

### NOTE:

Download pf01.bin, pf06, pf16, pf30, pf42, uf01.bin, uf06, uf16, uf30, uf42, vf01, vf06, vf16, vf30, and vf42, .bin files from https://www.earthsystemgrid.org/dataset/isabeldata/file.html  extract them in data folder

### To run code

- The code for different plots is present in the source directory. To get a specific plot on a data variable in data directory you can run the file named after the plot to get results 

- You can also see examples of output plots in the images folder

