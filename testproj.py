import tkinter
import time
import person
import roads
import cars

# width of the animation window
animation_window_width=1200
# height of the animation window
animation_window_height=720
# initial x position of the ball
animation_ball_start_xpos = 50
# initial y position of the ball
animation_ball_start_ypos = 50
# radius of the ball
animation_ball_radius = 10
# the pixel movement of ball for each iteration
animation_ball_min_movement = 5
# delay between successive frames in seconds
animation_refresh_seconds = 0.01

# Set test car size
animation_car_size_x = 10
animation_car_size_y = 15
#set test car position
animation_car_position_x = 3
animation_car_position_y = 10

#NUMBER OF PIXELS ROADS MOVE EACH TICK:
#also should be the camera speed
road_move_x=0
road_move_y=5


# The main window of the animation
def create_animation_window():
  window = tkinter.Tk()
  window.title("Tkinter Animation Demo")
  # Uses python 3.6+ string interpolation
  window.geometry(f'{animation_window_width}x{animation_window_height}')
  return window

# Create a canvas for animation and add it to main window
def create_animation_canvas(window):
  canvas = tkinter.Canvas(window)
  canvas.configure(bg="white")
  canvas.pack(fill="both", expand=True)
  return canvas

# Create and animate ball in an infinite loop
def animate_ball(window, canvas,xinc,yinc, object_dict):
  ball = canvas.create_oval(animation_ball_start_xpos-animation_ball_radius,
            animation_ball_start_ypos-animation_ball_radius,
            animation_ball_start_xpos+animation_ball_radius,
            animation_ball_start_ypos+animation_ball_radius,
            fill="blue", outline="white", width=4)
  #test_car(animation_canvas)

  
  window_bottom=window.winfo_height()
  window_top=0
  window_left=0
  window_right=window.winfo_width()
  
  PAUSE=False
  until_pause_counter=0
  TIME_TO_NEXT_PAUSE=(1.5*window_bottom)/road_move_y
  PAUSE_DURATION=200
  pause_timer=0  
  
  #main loop
  while True:
    canvas.move(ball,xinc,yinc)
    
    for key in object_dict:
        if key == 'road':
            if not PAUSE:
                roads.move_roads(canvas,object_dict[key],road_move_x,road_move_y)
                #Ballshit
                xinc, yinc = ballshit(canvas,ball,animation_window_width,animation_window_height,xinc,yinc)
                
                until_pause_counter+=1
                if until_pause_counter >= TIME_TO_NEXT_PAUSE:
                    until_pause_counter=0
                    PAUSE=True
            else:
                pause_timer+=1
                if pause_timer >= PAUSE_DURATION:
                    pause_timer=0
                    PAUSE=False

    window.update()
    time.sleep(animation_refresh_seconds)


"""
    ball_pos = canvas.coords(ball)
    # unpack array to variables
    xl,yl,xr,yr = ball_pos
    if xl < abs(xinc) or xr > animation_window_width-abs(xinc):
      xinc = -xinc
    if yl < abs(yinc) or yr > animation_window_height-abs(yinc):
      yinc = -yinc
"""
# Create test car
def test_car(canvas):
    car = canvas.create_rectangle(30, 50, 60, 70,
        outline="#fb0", fill="#fb0")
def ballshit(canvas,ball,animation_window_width,animation_window_height,xinc,yinc):
    ball_pos = canvas.coords(ball)
    # unpack array to variables
    xl,yl,xr,yr = ball_pos
    if xl < abs(xinc) or xr > animation_window_width-abs(xinc):
      xinc = -xinc
    if yl < abs(yinc) or yr > animation_window_height-abs(yinc):
      yinc = -yinc
    return xinc,yinc
# The actual execution starts here
animation_window = create_animation_window()
animation_canvas = create_animation_canvas(animation_window)

#Store references to all objects created here. Each function should return a list, which will be in this dictionary
# with an appropriate key

all_objects={}

test_car(animation_canvas)
person.create_group(animation_canvas)
animation_window.update()
road_segs=roads.create_roads(animation_canvas, animation_window, 1)
car_brigade=cars.create_cars(animation_canvas, animation_window, 1)

all_objects['road']=road_segs
animate_ball(animation_window,animation_canvas, animation_ball_min_movement, animation_ball_min_movement, all_objects)
#test_car(animation_canvas)
