import tkinter
import time
import roads3
import static_objects
import CarObj


# width of the animation window
animation_window_width=1200
# height of the animation window
animation_window_height=800

# the pixel movement of ball for each iteration
animation_ball_min_movement = 5
# delay between successive frames in seconds
animation_refresh_seconds = 0.01

# The main window of the animation
def create_animation_window():
  window = tkinter.Tk()
  window.title("Car Brigade")
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
def start_animation(window, canvas, objects): 
  #main loop
  while True:

    for obj in objects:
        obj.update(objects)
    window.update()
    time.sleep(animation_refresh_seconds)
def create_static_objects(window, canvas):
    pass

# The actual execution starts here
animation_window = create_animation_window()
animation_canvas = create_animation_canvas(animation_window)

#Store references to all objects created here. Each function should return a list, which will be in this dictionary
# with an appropriate key

#CRITICAL!!!
animation_window.update()

animation_objects=[]

static_objects.draw_grids(animation_canvas, animation_window)
roads3.create_roads(animation_canvas, animation_window)
animation_objects+=CarObj.create_cars(animation_canvas, animation_window)


start_animation(animation_window,animation_canvas,animation_objects)
#test_car(animation_canvas)
