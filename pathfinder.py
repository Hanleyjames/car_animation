def create_pathfinder(canvas, window):
    window_bottom=window.winfo_height()
    window_top=0
    window_left=0
    window_right=window.winfo_width()
    
    print("creating pathfinder", window_right, window_bottom)
    
    x1=125
    x2=175
    y1=600
    y2=650
    
    PF=canvas.create_rectangle(x1,y1,x2,y2,
        fill="green", outline="black", width=1)
    pfo=PathFinder(x1,y1)
    
    return([PF,pfo])

class PathFinder:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.wayx=0
        self.wayy=0
        self.xv=1
        self.yv=1
        self.way_point=0
        self.MAX_SPEED=1
    
    def update(self,canvas, pf):
        self.check_state()
        self.set_waypoints()
        self.set_velocities()
        canvas.move(pf,self.xv, self.yv)
        
        self.x+=self.xv
        self.y+=self.yv
    
    def set_waypoints(self):
        if self.way_point==0:
            self.wayx=150
            self.wayy=150
        elif self.way_point==1:
            self.wayx=550
            self.wayy=150            
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
        if abs(self.x-self.wayx)<2 and abs(self.y-self.wayy)<2 :
            self.way_point+=1
    
    def set_velocities(self):
        if self.x<self.wayx:
            self.xv=self.MAX_SPEED
        else:
            self.xv=-1*self.MAX_SPEED
        if self.y<self.wayy:
            self.yv=self.MAX_SPEED
        else:
            self.yv=-1*self.MAX_SPEED
        
        
    