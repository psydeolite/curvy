from display import *
from matrix import *
from math import cos, sin

def add_circle( points, cx, cy, cz, r, step ):
    s=step
    x0=cx+r
    y0=cy
    x=0
    y=0
    while (s<1):
        #print x
        #print y
        t=2*math.pi*s
        x=r*cos(t)+cx
        y=r*sin(t)+cy
        add_edge(points,x0,y0,0,x,y,0)
        x0=x
        y0=y
        s+=step

#curve_type: either 'H' or 'B', interpreted in matrix.py
def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    s=step
    x=x0
    y=y0
    cox=generate_curve_coefs(x0,x1,x2,x3,curve_type)
    coy=generate_curve_coefs(y0,y1,y2,y3,curve_type)
    i=0
    fx=0
    fy=0
    while (s<1):
        #evaluate x part of polynomial
        #print 'x: '+str(x)
        #print 'y: '+str(y)
        #print 'fx: '+str(fx)
        #print 'fy: '+str(fy)
        i=3
        fx=0
        fy=0
        while (i>=0):
            fx+=pow(s,i)*cox[0][3-i]
            fy+=pow(s,i)*coy[0][3-i]
            i-=1
            #print 'in'
        add_edge(points,x,y,0,fx,fy,0)
        x=fx
        y=fy
        s+=step
        #print 'out'
    #print 'AY'

def draw_lines( matrix, screen, color ):
    #print matrix
    #print 'draw_lines'
    if len( matrix ) < 2:
        print "Need at least 2 points to draw a line"
        
    p = 0
    while p < len( matrix ) - 1:
        #print 'while'
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
    #print 'draw'
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
            #print 'a'
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

