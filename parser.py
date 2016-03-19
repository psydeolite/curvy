from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform, screen, color ):
    f=open(fname)
    r=f.read()
    byline=r.split("\n")
    transmat=new_matrix()
    for i in range(len(byline)):
        #NO ARGUMENTS FAM
        if byline[i]=='display':
            draw_lines(points, screen, color) 
            display(screen)
        elif byline[i]=='apply':
            matrix_mult(transmat,points)
        elif byline[i]=='ident':
            ident(transmat)
        elif byline[i]=='quit':
            print 'quit!!!'
            break
        else:
            #LET'S ARGUE FAM
            command=byline[i]
            i+=1
            args=byline[i].split(' ')
            if command=='line':
                draw_line(screen,args[0],args[1],args[3],args[4],color)
            elif command=='scale':
                #scale
                scale(transmat,args[0],args[1],args[2])
            elif command=='xrotate':
                #xrot
                xrotate(transmat,args[0])
            elif command=='yrotate':
                #yrot
                yrotate(transmat,args[0])
            elif command=='zrotate':
                #zrot
                zrotate(transmat,args[0])
            elif command=='circle':
                #circle
                add_circle(transmat, args[0],args[1],0,args[2],0.1)
            elif command=='hermite':
                #herm
                add_curve(transmat, args[0],args[1],args[2],args[3],args[4],args[5],args[6],args[7],0.1,'H')
            elif command=='bezier':
                #bez
                add_curve(transmat, args[0],args[1],args[2],args[3],args[4],args[5],args[6],args[7],0.1,'B')
            elif command=='save':
                #save
                save_ppm(screen,args[0])
                save_extension(screen,args[0])
    print byline

parse_file("script_nocurves",0,0,0,0)

