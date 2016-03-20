from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform, screen, color ):
    f=open(fname)
    r=f.read()
    byline=r.split("\n")
    transmat=new_matrix()
    ident(transmat)
    linelen=len(byline)
    #for i in range(len(byline)):
    i=0
    while i<linelen:
        #NO ARGUMENTS FAM
        if byline[i]=='display':
            draw_lines(points, screen, color) 
            display(screen)
            i+=1
        elif byline[i]=='apply':
            matrix_mult(transmat,points)
            i+=1
        elif byline[i]=='ident':
            ident(transmat)
            i+=1
        elif byline[i]=='quit':
            break
        else:
            #LET'S ARGUE FAM
            command=byline[i]
            i+=1
            args=byline[i].split(' ')
            if command=='line':
                add_edge(points,int(args[0]),int(args[1]),int(args[2]),int(args[3]),int(args[4]),int(args[5]))
                i+=1
            elif command=='translate':
                translate(transmat,int(args[0]),int(args[1]),int(args[2]))
                i+=1
            elif command=='scale':
                #scale
                scale(transmat,float(args[0]),float(args[1]),float(args[2]))
                i+=1
            elif command=='xrotate':
                #xrot
                xrotate(transmat,int(args[0]))
                i+=1
            elif command=='yrotate':
                #yrot
                yrotate(transmat,int(args[0]))
                i+=1
            elif command=='zrotate':
                #zrot
                zrotate(transmat,int(args[0]))
                i+=1
            elif command=='circle':
                #circle
                add_circle(points, int(args[0]),int(args[1]),0,int(args[2]),0.00001)
                i+=1
            elif command=='hermite':
                #herm
                add_curve(points, int(args[0]),int(args[1]),int(args[2]),int(args[3]),int(args[4]),int(args[5]),int(args[6]),int(args[7]),0.00001,'H')
                i+=1
            elif command=='bezier':
                #bez
                add_curve(points, int(args[0]),int(args[1]),int(args[2]),int(args[3]),int(args[4]),int(args[5]),int(args[6]),int(args[7]),0.00001,'B')
                i+=1
            elif command=='save':
                #save
                draw_lines(points, screen, color) 
                save_ppm(screen,args[0])
                save_extension(screen,args[0])
                i+=1
            else:
                print 'Invalid command bro:' +command
                i+=1



