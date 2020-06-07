import os
from svgpathtools import Path, Line, QuadraticBezier, CubicBezier, Arc
from svgpathtools import svg2paths, wsvg
import numpy as np

HOME = "G28\n"
UNITS_MILLIMETRES = "G21\n"
FEEDRATE = 3000
Z_OFFSET = 27.6
START_X = 123
START_Y = 32
WIDTH = 140 #mm

paths,attributes=svg2paths("in.svg")
gcode = open("out.gcode","w")

#Add boilerplate code
gcode.write(HOME)
gcode.write(UNITS_MILLIMETRES)
gcode.write("G1 F"+str(FEEDRATE)+"\n")
gcode.write("G1 Z"+str(Z_OFFSET+5)+"\n")

X = np.linspace(0,1,100)
X_coords = []
Y_coords = []

for path in paths:
    for curve in path:
        p = curve.poly()
        X_coords.extend(p(X).real)
        Y_coords.extend(-p(X).imag)
        
SCALE = WIDTH/(max(X_coords)-min(X_coords))
Y_OFFSET = START_Y - min(np.array(Y_coords)*SCALE)
X_OFFSET = START_X - min(np.array(X_coords)*SCALE)

for path in paths:
    for subpath in path.continuous_subpaths():
        X_coords=[]
        Y_coords=[]
        if subpath:
            for curve in subpath:
                p = curve.poly()
                if(p.order==1):
                    x = [p(0).real, p(1).real]
                    y = [-p(0).imag,-p(1).imag]
                else:
                    x = p(X).real
                    y = -p(X).imag
                x = np.array(x)*SCALE+X_OFFSET
                y = np.array(y)*SCALE+Y_OFFSET
                X_coords.extend(x)
                Y_coords.extend(y)
            gcode.write("G1 X"+str(X_coords[0])+" Y"+str(Y_coords[0])+"\n")
            gcode.write("G1 Z"+str(Z_OFFSET)+"\n")
            for x_coord, y_coord in zip(X_coords,Y_coords):
                gcode.write("G1 X"+str(x_coord)+" Y"+str(y_coord)+"\n")
            gcode.write("G1 Z"+str(Z_OFFSET+5)+"\n")     
