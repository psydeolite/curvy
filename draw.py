from display import *
from matrix import *
import math

def add_circle( points, cx, cy, cz, r, step ):
    s=step
    x0=cx+r
    y0=cy
    while (s<1):
        t=2*math.pi*step
        x=r*cos(t)+cx
        y=r*sin(t)+cy
        add_edge(points,x0,y0,0,x1,y1,0)
        x0=x
        y0=y
        s+=step

#curve_type: either 'H' or 'B', interpreted in matrix.py
def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    s=step
    x=x0
    y=y0
    cox=generate_curve_coeffs(x0,x1,x2,x3,curve_type)
    coy=generate_curve_coeffs(y0,y1,y2,y3,curve_type)
    while (s<1):
        #evaluate x part of polynomial
        i=3
        while (i>=0):
            fx+=pow(x,i)*fx[3-i]
            fy+=pow(y,i)*fy[3-i]
            i-=1
        add_edge(points,x,y,0,fx,fy,0)
        x=fx
        y=fy
        #evaluate y part of polynomial
        #add edge
        #increment stuff
    #pass

def draw_lines( matrix, screen, color ):
    if len( matrix ) < 2:
        print "Need at least 2 points to draw a line"
        
    p = 0
    while p < len( matrix ) - 1:
        draw_line( screen, matrix[p][0], matrix[p][1],
                   matrix[p+1][0], matrix[p+1][1], color )
        p+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point( matrix, x0, y0, z0 )
    add_point( matrix, x1, y1, z1 )

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )

def xrotate(matrix,theta):
    m=make_rotX(theta)
    matrix_mult(m,matrix)
    return m

def yrotate(matrix, theta):
    m=make_rotY(theta)
    matrix_mult(m,matrix)
    return m

def zrotate(matrix, theta):
    m=make_rotZ(theta)
    matrix_mult(m,matrix)
    return m

def translate(matrix,x,y,z):
    m=make_translate(x,y,z)
    matrix_mult(m,matrix)
    return m

def scale(matrix,x,y,z):
    m=make_scale(x,y,z)
    matrix_mult(m,matrix)
    return m

def draw_line( screen, x0, y0, x1, y1, color ):
    dx = x1 - x0
    dy = y1 - y0
    if dx + dy < 0:
        dx = 0 - dx
        dy = 0 - dy
        tmp = x0
        x0 = x1
        x1 = tmp
        tmp = y0
        y0 = y1
        y1 = tmp
    
    if dx == 0:
        y = y0
        while y <= y1:
            plot(screen, color,  x0, y)
            y = y + 1
    elif dy == 0:
        x = x0
        while x <= x1:
            plot(screen, color, x, y0)
            x = x + 1
    elif dy < 0:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y - 1
                d = d - dx
            x = x + 1
            d = d - dy
    elif dx < 0:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x - 1
                d = d - dy
            y = y + 1
            d = d - dx
    elif dx > dy:
        d = 0
        x = x0
        y = y0
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y = y + 1
                d = d - dx
            x = x + 1
            d = d + dy
    else:
        d = 0
        x = x0
        y = y0
        while y <= y1:
            plot(screen, color, x, y)
            if d > 0:
                x = x + 1
                d = d - dy
            y = y + 1
            d = d + dx

