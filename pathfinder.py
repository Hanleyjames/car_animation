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
    
    return([PF,pfo])

class PathFinder:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.wi=w
        self.he=h
        self.wayx=0
        self.wayy=0
        self.xv=1
        self.yv=1
        self.way_point=0
        self.MAX_SPEED=1
        
        self.tick=0
    
    def update(self,canvas, pf):
        self.check_state()
        self.set_waypoints(canvas,pf)
        self.set_velocities()
        canvas.move(pf,self.xv, self.yv)
        
        self.x+=self.xv
        self.y+=self.yv
        
        pf=self.rotate(canvas,pf)
        self.tick+=.1
        return pf
    
    def set_waypoints(self,canvas,pf):
        if self.way_point==0:
            self.wayx=150
            self.wayy=150
        elif self.way_point==1:
            self.wayx=550
            self.wayy=150
            #pf=self.rotate(canvas,pf)            
        elif self.way_point==2:
            self.wayx=550
            self.wayy=430    
        elif self.way_point==3:
            self.wayx=950
            self.wayy=430
        elif self.way_point==4:
            self.wayx=950
            self.wayy=150            
    def check_state(self):
        if abs(self.x-self.wayx)<3 and abs(self.y-self.wayy)<3 :
            self.way_point+=1
    
    def set_velocities(self):
        if self.x<self.wayx:
            self.xv=self.MAX_SPEED
        else:
            self.xv=-1*self.MAX_SPEED
        
        if abs(self.x-self.wayx)<2:
            self.xv=0
            
        if self.y<self.wayy:
            self.yv=self.MAX_SPEED
        else:
            self.yv=-1*self.MAX_SPEED
        
        if abs(self.y-self.wayy)<2:
            self.yv=0

    def flatten(self, list_of_lists):
        """Flatten one level of nesting"""
        return itertools.chain.from_iterable(list_of_lists)

    def rotate(self,canvas,pf):
        
        oldcoords=canvas.coords(pf)
        print(oldcoords)
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
        
