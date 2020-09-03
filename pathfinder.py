import itertools
import math
def create_pathfinder(canvas, window):
    window_bottom=window.winfo_height()
    window_top=0
    window_left=0
    window_right=window.winfo_width()
    
    print("creating pathfinder", window_right, window_bottom)
    
    x1=125
    x2=170
    y1=600
    y2=660
    
    #PF=canvas.create_rectangle(x1,y1,x2,y2,
     #   fill="green", outline="black", width=1)
    xy = [(x1, y1), (x2, y1), (x2, y2), (x1, y2), (x1,y1)]
    
    print(xy)
    PF = canvas.create_polygon(xy,fill="green", outline="black", width=1)     
        
    pfo=PathFinder((x1+x2)/2,(y1+y2)/2, x2-x1, y2-y1)
    pfo.rotate_on=True
    
    pfo.way_points=[(150,150),(550,150),(550,440)]
    pfo.wayx=0
    pfo.wayy=0
    
    return([PF,pfo])

def create_cars(canvas, window):
    window_bottom=window.winfo_height()
    window_top=0
    window_left=0
    window_right=window.winfo_width()
    
    cars=[]
    
    CAR_WIDTH=25
    CAR_HEIGHT=30
    
    
    
    #routes
    routes=[]
    #First two straights
    c1=[(112,480),(-99,100),(112,362),(-99,100),(112,200),(-99,100)]
    c2=[(139,480),(-99,100),(139,362),(-99,100),(139,200),(-99,100)]
    c3=[(166,480),(-99,100),(166,362),(-99,100),(166,200),(-99,100)]
    c4=[(193,480),(-99,100),(193,362),(-99,100),(193,200),(-99,100)]
    routes.append(c1)
    routes.append(c2)
    routes.append(c3)
    routes.append(c4)
    
    #first right turn
    target_x=200
    #extens=math.sqrt((target_x-ix)**2+ (math.tan(math.radians(theta)))**2)
    for route in routes:
        ix=route[-2][0]
        iy=route[-2][1]
        
        for theta in (10,20,30,40,50,60,70,80):
            extens=target_x-ix
            route+=[(target_x-math.cos(math.radians(theta))*(extens),iy-math.sin(math.radians(theta))*(extens))]

    

    
    
    #car1
    x1=100
    x2=x1+CAR_WIDTH
    y1=525
    y2=y1+CAR_HEIGHT    
    xy = [(x1, y1), (x2, y1), (x2, y2), (x1, y2), (x1,y1)]    
    PF = canvas.create_polygon(xy,fill="yellow", outline="black", width=1)             
    pfo=PathFinder((x1+x2)/2,(y1+y2)/2, x2-x1, y2-y1)
    
    number=canvas.create_text((x1+x2)/2,(y1+y2)/2, font=("Arial",8), text=str(1))
    
    pfo.text_obj=number
    pfo.way_points=routes[0]
    pfo.wayx=0
    pfo.wayy=0    
    cars.append([PF,pfo])
    
    #car2
    x1=127
    x2=x1+CAR_WIDTH
    y1=525
    y2=y1+CAR_HEIGHT    
    xy = [(x1, y1), (x2, y1), (x2, y2), (x1, y2), (x1,y1)]    
    PF = canvas.create_polygon(xy,fill="yellow", outline="black", width=1)             
    pfo=PathFinder((x1+x2)/2,(y1+y2)/2, x2-x1, y2-y1)
    
    number=canvas.create_text((x1+x2)/2,(y1+y2)/2, font=("Arial",8), text=str(2))
    
    pfo.text_obj=number
    pfo.way_points=routes[1]
    pfo.wayx=0
    pfo.wayy=0    
    cars.append([PF,pfo])    

    #car3
    x1=154
    x2=x1+CAR_WIDTH
    y1=525
    y2=y1+CAR_HEIGHT    
    xy = [(x1, y1), (x2, y1), (x2, y2), (x1, y2), (x1,y1)]    
    PF = canvas.create_polygon(xy,fill="yellow", outline="black", width=1)             
    pfo=PathFinder((x1+x2)/2,(y1+y2)/2, x2-x1, y2-y1)
    
    number=canvas.create_text((x1+x2)/2,(y1+y2)/2, font=("Arial",8), text=str(3))
    
    pfo.way_points=routes[2]
    pfo.wayx=0
    pfo.wayy=0     
    
    pfo.text_obj=number    
    cars.append([PF,pfo])    
    
    #car4
    x1=181
    x2=x1+CAR_WIDTH
    y1=525
    y2=y1+CAR_HEIGHT    
    xy = [(x1, y1), (x2, y1), (x2, y2), (x1, y2), (x1,y1)]    
    PF = canvas.create_polygon(xy,fill="yellow", outline="black", width=1)             
    pfo=PathFinder((x1+x2)/2,(y1+y2)/2, x2-x1, y2-y1)
    
    number=canvas.create_text((x1+x2)/2,(y1+y2)/2, font=("Arial",8), text=str(4))
    pfo.way_points=routes[3]
    pfo.wayx=0
    pfo.wayy=0     
    pfo.text_obj=number    
    cars.append([PF,pfo])     
    return(cars)


class PathFinder:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.wi=w
        self.he=h
        self.wayx="stop"
        self.wayy="stop"
        self.xv=1
        self.yv=1
        self.way_point=0
        self.MAX_SPEED=1
        self.text_obj=0
        
        self.rotate_on=False
        self.HOLD=False
        self.hold_timer=0
        self.tick=0
        
        self.way_points=[]
    
    def update(self,canvas, pf):
        if not self.check_hold(canvas,pf):
            self.check_state()
            self.set_waypoints(canvas,pf)
            self.set_velocities()
            self.apply_brakes()
            canvas.move(pf,self.xv, self.yv)
            canvas.move(self.text_obj,self.xv, self.yv)
            self.x+=self.xv
            self.y+=self.yv
        
        if self.rotate_on:
            pf=self.rotate(canvas,pf)
        self.tick+=.1
        return pf
    
    def set_waypoints(self,canvas,pf):
        if len(self.way_points)>self.way_point:
            self.wayx=self.way_points[self.way_point][0]
            self.wayy=self.way_points[self.way_point][1]
        else:
            self.wayx="stop"
            self.wayy="stop"
    
    def check_hold(self,canvas,pf):
        if self.wayx==-99 and not self.HOLD:
            self.HOLD=True
            self.xv=0
            self.yv=0
        
        elif self.HOLD:
            self.hold_timer+=1
        
        if self.HOLD and self.hold_timer>self.wayy:
            self.HOLD=False
            self.hold_timer=0
            self.way_point+=1
        return self.HOLD
            
    def check_state(self):
        if self.wayx != "stop" and self.wayy != "stop":
            if abs(self.x-self.wayx)<3 and abs(self.y-self.wayy)<3 :
                self.way_point+=1
                print('arrived at waypoint, coords:',self.wayx,self.wayy)
                print('going to waypoint:',self.way_point)
    
    def set_velocities(self):
        #print(self.xv,self.yv)
        if self.wayx == "stop":
            self.xv=0
        else:        
            if self.x<self.wayx:
                self.xv=self.interpolation(self.xv)
            else:
                self.xv=self.interpolation(self.xv,-1)
            
            if abs(self.x-self.wayx)<2:
                self.xv=0
        if self.wayy == "stop":
            self.yv=0
        else:
            if self.y<self.wayy:
                self.yv=self.interpolation(self.yv)
            else:
                self.yv=self.interpolation(self.yv,direction=-1)
            
            if abs(self.y-self.wayy)<2:
                self.yv=0

    def flatten(self, list_of_lists):
        """Flatten one level of nesting"""
        return itertools.chain.from_iterable(list_of_lists)
    
    def apply_brakes(self):
        BRAKE_DISTANCE=50
        BRAKE_CONSTANT=.95
        
        if self.wayx=="stop" or self.wayy=="stop":
            return
        
        if abs(self.x-self.wayx)<BRAKE_DISTANCE:
            brakes=max(BRAKE_CONSTANT,abs(self.x-self.wayx)/BRAKE_DISTANCE)
            self.xv*=brakes
        if abs(self.y-self.wayy)<BRAKE_DISTANCE:
            brakes=max(BRAKE_CONSTANT,abs(self.y-self.wayy)/BRAKE_DISTANCE)
            self.yv*=brakes      
    
    def interpolation(self,velocity,direction=1):
        new_v=0
        if velocity==0:
            new_v=direction*.01
        elif velocity<self.MAX_SPEED:
            new_v=velocity+direction*.01
        return new_v
    #Rotation is just goofy circling
    def rotate(self,canvas,pf):
        
        oldcoords=canvas.coords(pf)
        #print(oldcoords)
        cleanxy=[]
        
        counter=0
        newcoords=[]
        for coord in oldcoords:
            newcoords.append(coord)
        newcoords[0]=newcoords[0]+math.sin(self.tick)
        newcoords[1]=newcoords[1]+math.cos(self.tick)
        
        newcoords[2]=newcoords[2]+math.sin(self.tick)
        newcoords[3]=newcoords[3]+math.cos(self.tick)
        
        newcoords[4]=newcoords[4]+math.sin(self.tick)
        newcoords[5]=newcoords[5]+math.cos(self.tick)
        
        newcoords[6]=newcoords[6]+math.sin(self.tick)
        newcoords[7]=newcoords[7]+math.cos(self.tick)
        
        newcoords[8]=newcoords[8]+math.sin(self.tick)
        newcoords[9]=newcoords[9]+math.cos(self.tick)

        #print(cleanxy)
        #canvas.delete(pf)
        PF = canvas.coords(pf,oldcoords)
        PF = canvas.coords(pf,newcoords)
        #PF = canvas.coords(pf,*self.flatten(cleanxy))
        return PF
        
