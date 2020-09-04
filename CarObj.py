class Car:
    def __init__(self, sprite, canvas, x, y, w, h, route):
        self.sprite=sprite
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.route=route.points
        
        #velocities
        self.xv=0
        self.yv=0
        
        #waypoints
        self.wayx=self.route[0][0]
        self.wayy=self.route[0][1]
        
        self.way_point=0

        self.canvas=canvas
    
    def update(self, objects):
        
        self.check_waypoint()
        self.set_velocities()
        
        self.x += self.xv
        self.y += self.yv

        self.canvas.move(self.sprite, self.xv, self.yv)
        
    def check_waypoint(self):
        if abs(self.x-self.wayx)<4 and abs(self.y-self.wayy)<4:
            self.way_point+=1
            print('changing way_point', self.way_point)
            
            if self.way_point < len(self.route):
                self.wayx=self.route[self.way_point][0]
                self.wayy=self.route[self.way_point][1]
                
                print('new waypoint coord', self.wayx, self.wayy )
    
    def set_velocities(self):
        
        if self.x < self.wayx:
            self.xv=1
        elif self.x > self.wayx:
            self.xv=-1
        else:
            self.xv=0
        
        
        if self.y  < self.wayy:
            self.yv = 1
        elif self.y > self.wayy:
            self.yv = -1
        else:
            self.yv=0
class Route:
    def __init__(self, points, canvas, car_color):
        self.points=points
        self.canvas=canvas
        self.car_color=car_color
    def draw_points(self):
        
        for i in range (0,len(self.points)):
            point_A=self.points[i]
            if i < (len(self.points)-1):
                point_B=self.points[i+1]
            else:
                point_B=(-1,-1)
            
            if point_B[0]!=-1:
                self.canvas.create_line(point_A[0], point_A[1], point_B[0], point_B[1], fill=self.car_color )

        
def create_cars(canvas, window):
    
    all_cars=[]
    
    #1
    car_color="yellow"
    
    points=[(287.5,112.5),(787.5,112.5),(787.5,512.5),(1200,512.5)]
    route_one = Route(points, canvas, car_color)
    route_one.draw_points()
    
    xy = [(275,100),(300,100),(300,125),(275,125),(275,125)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    car_one = Car(sprite, canvas, 287.5,112.5,25,25, route_one)
    
    all_cars.append(car_one)
    
    #2
    car_color="green"
    
    points=[(287.5,137.5),(762.5,137.5),(762.5,537.5),(1200,537.5)]
    route_one = Route(points, canvas, car_color)
    route_one.draw_points()
    
    xy = [(275,125),(300,125),(300,150),(275,150),(275,150)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    car_one = Car(sprite, canvas, 287.5,137.5,25,25, route_one)
    
    all_cars.append(car_one)    
 
    #3
    car_color="blue"
    
    points=[(287.5,162.5),(737.5,162.5),(737.5,562.5),(1200,562.5)]
    route_one = Route(points, canvas, car_color)
    route_one.draw_points()
    
    xy = [(275,150),(300,150),(300,175),(275,175),(275,150)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    car_one = Car(sprite, canvas, 287.5,162.5,25,25, route_one)
    
    all_cars.append(car_one)   
    
    #4
    car_color="red"
    
    points=[(287.5,187.5),(712.5,187.5),(712.5,587.5),(1200,587.5)]
    route_one = Route(points, canvas, car_color)
    route_one.draw_points()
    
    xy = [(275,175),(300,175),(300,200),(275,200),(275,175)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    car_one = Car(sprite, canvas, 287.5,187.5,25,25, route_one)
    
    all_cars.append(car_one)    
    
    return all_cars
    


        
        