from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

raindrops=[[200,500,200,200],[250,500,250,200],[300,500,300,200],[350,500,350,200],
           [400,500,400,200],[450,500,450,200],[500,500,500,200]]



rain_speed = 0.050
reset=500
r_r=1
r_g=1
r_b=1
bg_r=0.4
bg_g=0.4
bg_b=1
bg_a=1
rooftop_color=(1,0.6,0)
roofmiddle_color=(0.5, 0.8, 0.9)
body_color=(0.1,0.5,0.7)
border_color=(0.5, 0.8, 0.9)
door_color=(1,0.6,0)
window_color=(1,0.6,0)
doorknob_color=(0,0,0)
window_bar_color=(0.1,0.5,0.7)



def draw_dashed_line(x1, y1, x2, y2, thickness=1.5):
    glColor3f(r_r,r_r,r_b)
    glLineWidth(thickness)
    glEnable(GL_LINE_STIPPLE)
    glLineStipple(20, 0xAAAA)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()
    glDisable(GL_LINE_STIPPLE)



def draw_rains(raindrops):
    for index in raindrops:
        draw_dashed_line(index[0],index[1],index[2],index[3])



def make_it_rain():
    global raindrops
    global reset
    for index in raindrops:
        index[1]-=rain_speed
        index[3]-=rain_speed
        if  index[1]<450:
            index[1]=reset
            index[3]=200


def draw_roof():
    global rooftop_color
    global roofmiddle_color
    draw_triangle(150,200,550,200,350,350,5,rooftop_color)
    draw_triangle(230, 225, 470, 225, 350, 310, 5, roofmiddle_color)

def draw_body():
    global body_color
    draw_triangle(175,200,175,35,350,130, 5, body_color)
    draw_triangle(525,200,525,35,345,130,5, body_color) 
    draw_triangle(175,35,525,35,345,130,5, body_color) 
    draw_triangle(175,200,525,200,345,130,5, body_color)

def draw_window():
    global window_color
    global window_bar_color
    draw_line(450,180,450,130,10,window_color)
    draw_line(455,180,455,130,10,window_color)
    draw_line(455,180,455,130,10,window_color)
    draw_line(460,180,460,130,10,window_color)
    draw_line(465,180,465,130,10,window_color)
    draw_line(470,180,470,130,10,window_color)
    draw_line(475,180,475,130,10,window_color)
    draw_line(480,180,480,130,10,window_bar_color)
    draw_line(485,180,485,130,10,window_color)
    draw_line(490,180,490,130,10,window_color)
    draw_line(495,180,495,130,10,window_color)
    draw_line(500,180,500,130,10,window_color)
    draw_line(505,180,505,130,10,window_color)
    draw_line(445,155,510,155,5,window_bar_color)

def draw_door():
    global door_color
    draw_line(245,35,245,135,10,door_color)
    draw_line(250,35,250,135,10,door_color)
    draw_line(255,35,255,135,10,door_color)
    draw_line(260,35,260,135,10,door_color)
    draw_line(265,35,265,135,10,door_color)
    draw_line(270,35,270,135,10,door_color)
    draw_line(275,35,275,135,10,door_color)
    draw_line(280,35,280,135,10,door_color)
    draw_line(285,35,285,135,10,door_color)
    draw_points(280,80,(0,0,0))

def draw_borders():
    draw_line(175,200,175,30,5,border_color)
    draw_line(170,200,170,30,10,border_color)
    draw_line(525,200,525,30,5,border_color)
    draw_line(530,200,530,30,10,border_color)
    draw_line(165,30,535,30,10,border_color)

def color_darken(object):
    r=object[0]
    g=object[1]
    b=object[2]
    n_r=r-0.1
    n_g=g-0.1
    n_b=b-0.1
    new_color=(n_r,n_g,n_b)
    return new_color

def color_lighten(object):
    r=object[0]
    g=object[1]
    b=object[2]
    n_r=r+0.1
    n_g=g+0.1
    n_b=b+0.1
    new_color=(n_r,n_g,n_b)
    return new_color
    
def keyboardListener(key, x, y):
    global rooftop_color
    global roofmiddle_color
    global body_color
    global border_color
    global door_color
    global window_color
    global window_bar_color
    global r_r
    global r_g
    global r_b
    global bg_a
    global bg_b
    global bg_g
    global bg_r

    if key==b'w':
        a=color_lighten(rooftop_color)
        b=color_lighten(roofmiddle_color)
        c=color_lighten(body_color)
        d=color_lighten(border_color)
        e=color_lighten(door_color)
        f=color_lighten(window_color)
        g=color_lighten(window_bar_color)
        rooftop_color=a
        roofmiddle_color=b
        body_color=c
        border_color=d
        door_color=e
        window_color=f
        window_bar_color=g
        r_r+=0.1
        r_g+=0.1
        r_b+=0.1
        bg_r+=0.1
        bg_g+=0.1
        bg_b+=0.1

    elif key==b's':
        a=color_darken(rooftop_color)
        b=color_darken(roofmiddle_color)
        c=color_darken(body_color)
        d=color_darken(border_color)
        e=color_darken(door_color)
        f=color_darken(window_color)
        g=color_darken(window_bar_color)
        rooftop_color=a
        roofmiddle_color=b
        body_color=c
        border_color=d
        door_color=e
        window_color=f
        window_bar_color=g
        r_r-=0.1
        r_g-=0.1
        r_b-=0.1
        bg_r-=0.1
        bg_g-=0.1
        bg_b-=0.1


def animate():
    make_it_rain()
    glutPostRedisplay()



def specialKeyListener(key, x, y):
    global raindrops

    raindrops2=[[200,500,150,200],[250,500,200,200],[300,500,250,200],[350,500,300,200],
           [400,500,350,200],[450,500,400,200],[500,500,450,200]]

    raindrops3=[[200,500,250,200],[250,500,300,200],[300,500,350,200],[350,500,400,200],
           [400,500,450,200],[450,500,500,200],[500,500,550,200]]
    
    if key==GLUT_KEY_LEFT:
        raindrops=raindrops2

    elif key==GLUT_KEY_RIGHT:
        raindrops=raindrops3
    


def draw_points(x, y,color):
    glColor3f(*color)
    glPointSize(5) 
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def draw_line(x1, y1, x2, y2,width,color):
    glColor3f(*color)
    glLineWidth(width)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()



def draw_triangle(x1,y1,x2,y2,x3,y3,thickness,color):
    glColor3f(*color)
    glLineWidth(thickness)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3) 
    glEnd()


def iterate():
    glViewport(0, 0, 700, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 700, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClearColor(bg_r,bg_g,bg_b,bg_a)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0)
    
    draw_rains(raindrops)
    draw_roof()
    draw_borders()
    draw_body()
    draw_door()
    draw_window()

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(700,500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Tiny-2D-House-In-Rain")
glutDisplayFunc(showScreen)
glutIdleFunc(animate)
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboardListener)
glutMainLoop()
