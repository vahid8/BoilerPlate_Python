#!/usr/bin/env python
""" Estimate Plane using 3Dpoints
"""

import open3d as o3d
import numpy as np

__author__ = "vahid jani"
__copyright__ = "Copyright 2021, The Boilerplates"
__credits__ = ["Vahid jani"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Vahid jani"
__email__ = "aghajanivahid1@gmail.com"
__status__ = "Production"



def estimate_plane(points_np:np.array):

    mass_center = np.mean(points_np, axis=0)
    reduced_points = points_np - mass_center
    # check_sums = reduced_points.sum(axis = 0)

    x_h = reduced_points[:,0]
    y_h =  reduced_points[:,1]
    z_h = reduced_points[:,2]
    xx_h = np.dot(x_h,np.transpose(x_h)) # sum of x2
    yy_h = np.dot(y_h,np.transpose(y_h)) # sum of y2
    zz_h = np.dot(z_h,np.transpose(z_h)) # sum of z2
    xy_h = np.dot(x_h,np.transpose(y_h)) # sum of xy
    xz_h = np.dot(x_h,np.transpose(z_h)) # sum of xz
    yz_h = np.dot(y_h,np.transpose(z_h)) # sum of yz

    design_matrix = np.array([[xx_h,xy_h,xz_h],
                              [xy_h,yy_h,yz_h],
                              [xz_h,yz_h,zz_h]])
    # USe PCA to find the minimum (minimum lambda, the corresponding vector is the normal vector)
    u, sigma, v = np.linalg.svd(design_matrix)
    landa = sigma[-1]
    normal_vector = u[:,-1]
    std = np.sqrt(landa/(len(x_h)-3))

    return normal_vector,std

if __name__ == '__main__':
    points_o3d = o3d.io.read_point_cloud("plane_riegl1.ply")
    points_np = np.asarray(points_o3d.points)
    normal_vector, std = estimate_plane(points_np)
