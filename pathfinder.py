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
    pfo.way_points=[(112,175),(212,112),(550,440)]
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
    pfo.way_points=[(137,150),(212,137),(550,440)]
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
        self.tick=0
        
        self.way_points=[]
    
    def update(self,canvas, pf):
        self.check_state()
        self.set_waypoints(canvas,pf)
        self.set_velocities()
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
           
    def check_state(self):
        if self.wayx != "stop" and self.wayy != "stop":
            if abs(self.x-self.wayx)<3 and abs(self.y-self.wayy)<3 :
                self.way_point+=1
                print('arrived at waypoint, coords:',self.wayx,self.wayy)
                print('going to waypoint:',self.way_point)
    
    def set_velocities(self):

        if self.wayx == "stop":
            self.xv=0
        else:        
            if self.x<self.wayx:
                self.xv=self.MAX_SPEED
            else:
                self.xv=-1*self.MAX_SPEED
            
            if abs(self.x-self.wayx)<2:
                self.xv=0
        if self.wayy == "stop":
            self.yv=0
        else:
            if self.y<self.wayy:
                self.yv=self.MAX_SPEED
            else:
                self.yv=-1*self.MAX_SPEED
            
            if abs(self.y-self.wayy)<2:
                self.yv=0

    def flatten(self, list_of_lists):
        """Flatten one level of nesting"""
        return itertools.chain.from_iterable(list_of_lists)
    
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
        
