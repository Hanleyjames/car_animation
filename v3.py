import tkinter
import time
import pandas as pd
import os


import roads3
import static_objects
import CarObj
import car_func


# width of the animation window
animation_window_width=1200
# height of the animation window
animation_window_height=800

# the pixel movement of ball for each iteration
animation_ball_min_movement = 5
# delay between successive frames in seconds
animation_refresh_seconds = 0.01



#Game level 
CPW=0

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

  global CPW
  
  # these two methods were needed to originally convert my python lists into a csv
  # from here on out, the car objects will read their route in from a csv, making all those lists obsolete
  #df=convert_route_to_csv(objects)
  #df2=splice_df(df)
  
  df2=pd.read_csv("C:\\Users\\V\\car_animation\\real_routes.csv")
  df2=df2.drop(['NOTES'], axis=1)
  df3=desplice(df2)
  load_csv_to_routes(objects, DF=df3)
  
  # fast forward method for testing
  fast_forward(objects, 0, canvas)
  
  def key(event):
    #print ("pressed", repr(event.char))
    #print(event)
    print(event.keycode)
    if event.keycode == 83:
        
        print('pause/unpause called')
        for obj in objects:
            CPW=obj.way_point
            if obj.HOLD:
                obj.HOLD=False
            else:
                obj.HOLD=True
        canvas.create_text(100+12*CPW,50, font=("Arial",12), text=str(CPW))
    elif event.keycode == 8:
        print('rewind')
        for obj in objects:
            obj.way_point-=1
            CPW=obj.way_point
        canvas.create_text(100+12*CPW,60, font=("Arial",12), text=str(CPW))    
    elif event.keycode == 87:
        print('fastforward')
        for obj in objects:
            obj.way_point+=1
            CPW=obj.way_point
        canvas.create_text(100+12*CPW,70, font=("Arial",12), text=str(CPW)) 
  window.bind("<Key>", key)
  
  #main loop
  PLAY=True
  while True:    
    for obj in objects:
        obj.update(objects)
        
    if PLAY:
        increment=True
        for obj in objects:
            if not obj.check_status():
                increment=False
        if increment:
            for obj in objects:
                if not obj.HOLD:
                    obj.incr_way_point()
    window.update()
    time.sleep(animation_refresh_seconds)
def create_static_objects(window, canvas):
    pass

def convert_route_to_csv(objects):
    df=pd.DataFrame()
    maxlen=100
    for object in objects:
        route=object.route
        pad = maxlen-len(route)
        for i in range(0,pad):
            route+=[(0,0)]
        df[object.car_number]=route
    path="C:\\Users\\V\\car_animation\\"
    path=os.getcwd()
    df.to_csv(path+"routes.csv")
    return df

def load_csv_to_routes(objects, DF=1):
    if isinstance(DF, int):
        print('reading from old routes files')
        path="C:\\Users\\V\\car_animation\\"
        path=os.getcwd()
        df=pd.read_csv(path+"routes.csv")
    else:
        print('using passed dataframe')
        df=DF
    print(df.columns)
    
    for object in objects:
        num=object.car_number
        route=df[str(num)].values
        
        #Sanitize values
        new_route=[]
        for item in route:
            item=item.replace('(', '')
            item=item.replace(')', '')
            itemL, itemR = item.split(',')
            
            tup=(float(itemL),float(itemR))
            
            new_route.append(tup)
        
        object.route=new_route
    print(new_route)
    
def fast_forward(objects, waypoint, canvas):
    for object in objects:
        object.way_point=waypoint
               
        
        object.x=object.route[object.way_point][0]
        object.y=object.route[object.way_point][1]
        
        object.wayx=object.x
        object.wayy=object.y        
        
        #original start positions
        ox=object.route[0][0]
        oy=object.route[0][1]
        
        #
        canvas.move(object.sprite, object.x-ox, object.y-oy)
        canvas.move(object.sprite2,object.x-ox, object.y-oy)
        
def splice_df(df):
    path="C:\\Users\\V\\car_animation\\"
    path=os.getcwd()
    df2=pd.DataFrame()
        
    for col in df.columns:
        raw= df[col].values
        
        xs=[]
        ys=[]
        for item in raw:
            #print(item)
            xs.append(item[0])
            ys.append(item[1])
        df2[str(col)+'_x']=xs
        df2[str(col)+'_y']=ys
    df2.to_csv(path+'splicedroutes.csv')
    return df2
    
def desplice(df):
    print('desplicing')
    print(df.columns)
    path="C:\\Users\\V\\car_animation\\"
    path=os.getcwd()    
    i=0
    df2=pd.DataFrame()
    while i < len(df.columns):
        cola=df.columns[i]
        colb=df.columns[i+1]
        
        xs=df[cola].values
        ys=df[colb].values
        
        tuples=[]
        
        for x,y in zip(xs,ys):
            tuples.append("("+str(x)+","+str(y)+")")
        i+=2
        col_name = cola.split('_')[0]
        df2[col_name]=tuples
    df2.to_csv(path+'despliced.csv')
    return df2
# The actual execution starts here
animation_window = create_animation_window()
animation_canvas = create_animation_canvas(animation_window)

#Store references to all objects created here. Each function should return a list, which will be in this dictionary
# with an appropriate key

#CRITICAL!!!
animation_window.update()

animation_objects=[]

#grid lines for testing
#static_objects.draw_grids(animation_canvas, animation_window)

roads3.create_roads(animation_canvas, animation_window)

animation_objects+=CarObj.create_cars(animation_canvas, animation_window)


start_animation(animation_window,animation_canvas,animation_objects)
#test_car(animation_canvas)
