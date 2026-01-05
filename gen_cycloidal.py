from math import *;
import ezdxf;

doc = ezdxf.new(setup=True)
msp = doc.modelspace()

N = 8 # number of poles
Rr = 5.5 # radius of pole
R = 35 # radius of disc
E = 1 # escentric offset

for i in range(0, 1024):
    t = 2*pi*i/1024
    x = (R*cos(t))-(Rr*cos(t+atan(sin((1-N)*t)/((R/(E*N))-cos((1-N)*t)))))-(E*cos(N*t))
    y = (-R*sin(t))+(Rr*sin(t+atan(sin((1-N)*t)/((R/(E*N))-cos((1-N)*t)))))+(E*sin(N*t))
    t = 2*pi*(i+1)/1024
    x1 = (R*cos(t))-(Rr*cos(t+atan(sin((1-N)*t)/((R/(E*N))-cos((1-N)*t)))))-(E*cos(N*t))
    y1 = (-R*sin(t))+(Rr*sin(t+atan(sin((1-N)*t)/((R/(E*N))-cos((1-N)*t)))))+(E*sin(N*t))

    msp.add_line((x/1000, y/1000), (x1/1000, y1/1000), dxfattribs={"layer": "MyLayer"})

doc.saveas("disk.dxf")