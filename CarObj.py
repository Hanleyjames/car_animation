CAR_SPEED = 1.5
SMOOTH=2
DRAW_ROUTES=False

class Car:
    def __init__(self, sprite, sprite2, canvas, x, y, w, h, route, car_number, wait_instr=[]):
        self.sprite=sprite
        self.sprite2=sprite2
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.route=route.points
        self.car_number=car_number
        
        #velocities
        self.xv=0
        self.yv=0
        
        #waypoints
        self.wayx=self.route[0][0]
        self.wayy=self.route[0][1]
        
        self.way_point=0

        self.canvas=canvas
        self.wait_instructions=wait_instr
        self.wait_number=0
        
        # if HOLD is true, the car will continue to it's current waypoint and then stop
        self.HOLD=True
    
    def check_status(self):
        
        return (abs(self.x - self.wayx)<=(SMOOTH+1) and abs(self.y - self.wayy)<=(SMOOTH+1))
    
    def incr_way_point(self):
        if self.way_point<(len(self.route)-1):
            self.way_point+=1
            self.wayx=self.route[self.way_point][0]
            self.wayy=self.route[self.way_point][1]
        
        print(self.car_number, 'incremented to', self.way_point, self.wayx, self.wayy)
    def update(self, objects):
        
        #self.check_waypoint()
        self.set_velocities()
        #self.check_wait(objects)
        
        self.x += self.xv
        self.y += self.yv

        self.canvas.move(self.sprite, self.xv, self.yv)
        self.canvas.move(self.sprite2, self.xv, self.yv)
    
    #Obsolete
    def check_waypoint(self):
        if abs(self.x-self.wayx)<4 and abs(self.y-self.wayy)<4:
            if not self.HOLD:
                #self.way_point+=1
            
                #only go to next waypoint while there are still way points remaining
                if self.way_point < len(self.route):
                    #print('car#',self.car_number,'changing way_point', self.way_point)
                    self.wayx=self.route[self.way_point][0]
                    self.wayy=self.route[self.way_point][1]
                    
                    #print('new waypoint coord', self.wayx, self.wayy )
    
    def set_velocities(self):
        
        if self.x < self.wayx  and abs(self.x - self.wayx)>SMOOTH:
            self.xv=CAR_SPEED
        elif self.x > self.wayx and abs(self.x - self.wayx)>SMOOTH:
            self.xv=-1*CAR_SPEED
        else:
            self.xv=0
        
        
        if self.y  < self.wayy and abs(self.y - self.wayy)>SMOOTH:
            self.yv = CAR_SPEED
        elif self.y > self.wayy and abs(self.y - self.wayy)>SMOOTH:
            self.yv = -1*CAR_SPEED
        else:
            self.yv=0
    
    def check_wait(self, cars):
        if self.wait_number == len(self.wait_instructions):
            return
        else:
            #print(self.car_number, "waiting on", self.wait_instructions)
            instructions=self.wait_instructions[self.wait_number]
            
            for car in cars:
                if car.car_number==instructions[0]:
                    if car.way_point==instructions[1]:
                        self.xv=0
                        self.yv=0
class Route:
    def __init__(self, points, canvas, car_color, offset=0):
        self.points=points
        self.canvas=canvas
        self.car_color=car_color
        self.offset=offset
    def draw_points(self):
        if DRAW_ROUTES:
            for i in range (0,len(self.points)):
                point_A=self.points[i]
                if i < (len(self.points)-1):
                    point_B=self.points[i+1]
                else:
                    point_B=(-1,-1)
                
                if point_B[0]!=-1:
                    self.canvas.create_line(point_A[0], point_A[1]+self.offset, point_B[0], point_B[1]+self.offset, fill=self.car_color )
                    self.canvas.create_text(point_A[0],point_A[1]+self.offset, font=("Arial",10), text=str(i),fill=self.car_color)

        
def create_cars(canvas, window):
    
    all_cars=[]
    
    # Front Cars ------------------------------------------------------------------------
    #1
    car_color="yellow"
    car_number=1
    
    # first intersection 0-10
    points=[(287.5,112.5),(312.5,112.5),(337.5,112.5),(362.5,112.5),(387.5,112.5),(412.4,112.5),(687.4,112.5),(687.4,112.5),(687.4,112.5),(687.4,112.5),(687.4,112.5)]
    # holding while cars get into position for next intersection
    points+=[(687.5,112.5),(687.5,112.5),(687.5,112.5)]
    # Right Turn
    points+=[(787.5,112.5),(787.5,137.5),(787.5,162.5),(787.5,187.5),(787.5,212.5),(787.5,487.5)]
    
    #17 holds
    points+=[(787.5,487.5),(787.5,487.5),(787.5,487.5),(787.5,487.5),(787.5,487.5),(787.5,487.5),(787.5,487.5),(787.5,487.5),(787.5,487.5),(787.5,487.5),(787.5,487.5),(787.5,487.5),(787.5,487.5),(787.5,487.5),(787.5,487.5),(787.5,487.5),(787.5,487.5),]
    # 2 holds
    points+=[(787.5,487.5),(787.5,487.5)]
    #WP 39 Start Left Turn
    points+=[(787.5,512.5)]
    
    route_one = Route(points, canvas, car_color, offset=car_number)
    route_one.draw_points()
    
    xy = [(275,100),(300,100),(300,125),(275,125),(275,125)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    sprite2=canvas.create_text(points[0][0],points[0][1], font=("Arial",8), text=str(car_number))
    
    car_one = Car(sprite, sprite2, canvas, 287.5,112.5,25,25, route_one, car_number)
    
    all_cars.append(car_one)
    
    #2
    car_number=2
    car_color="green"
    
    points=[(287.5,137.5),(312.5,137.5),(337.5,137.5),(362.5,137.5),(387.5,137.5),(412.4,137.5),(687.4,137.5),(687.4,137.5),(687.4,137.5),(687.4,137.5),(687.4,137.5)]
        # holding while cars get into position for next intersection
    points+=[(687.5,137.5),(687.5,137.5),(687.5,137.5)]
    # Right Turn
    points+=[(762.5,137.5),(762.5,137.5),(762.5,162.5),(762.5,187.5),(762.5,212.5),(762.5,487.5)]
        #17 holds
    points+=[(762.5,487.5),(762.5,487.5),(762.5,487.5),(762.5,487.5),(762.5,487.5),(762.5,487.5),(762.5,487.5),(762.5,487.5),(762.5,487.5),(762.5,487.5),(762.5,487.5),(762.5,487.5),(762.5,487.5),(762.5,487.5),(762.5,487.5),(762.5,487.5),(762.5,487.5),]
    # 2 holds
    points+=[(762.5,487.5),(762.5,487.5)]
    #Start Left Turn wp #39
    points+=[(762.5,512.5)]
    
    route_one = Route(points, canvas, car_color, offset=car_number)
    route_one.draw_points()
    
    xy = [(275,125),(300,125),(300,150),(275,150),(275,150)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    sprite2=canvas.create_text(points[0][0],points[0][1], font=("Arial",8), text=str(car_number))
    car_one = Car(sprite,sprite2, canvas, 287.5,137.5,25,25, route_one, car_number)
    
    all_cars.append(car_one)    
 
    #3
    car_number=3
    car_color="blue"
    
    points=[(287.5,162.5),(312.5,162.5),(337.5,162.5),(362.5,162.5),(387.5,162.5),(412.4,162.5),(687.4,162.5),(687.4,162.5),(687.4,162.5),(687.4,162.5),(687.4,162.5)]
    points+=[(687.5,162.5),(687.5,162.5),(687.5,162.5)]
        # Right Turn
    points+=[(737.5,162.5),(737.5,162.5),(737.5,162.5),(737.5,187.5),(737.5,212.5),(737.5,487.5)]
        #17 holds
    points+=[(737.5,487.5),(737.5,487.5),(737.5,487.5),(737.5,487.5),(737.5,487.5),(737.5,487.5),(737.5,487.5),(737.5,487.5),(737.5,487.5),(737.5,487.5),(737.5,487.5),(737.5,487.5),(737.5,487.5),(737.5,487.5),(737.5,487.5),(737.5,487.5),(737.5,487.5),]
    #2 holds
    points+=[(737.5,487.5),(737.5,487.5)]
    
    #Start Left Turn wp #39
    points+=[(737.5,512.5)]
    route_one = Route(points, canvas, car_color, offset=car_number)
    route_one.draw_points()
    
    xy = [(275,150),(300,150),(300,175),(275,175),(275,150)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    sprite2=canvas.create_text(points[0][0],points[0][1], font=("Arial",8), text=str(car_number))
    car_one = Car(sprite,sprite2, canvas, 287.5,162.5,25,25, route_one, car_number)
    
    all_cars.append(car_one)   
    
    #4
    car_number=4
    car_color="red"
    
    points=[(287.5,187.5),(312.5,187.5),(337.5,187.5),(362.5,187.5),(387.5,187.5),(412.4,187.5),(687.4,187.5),(687.4,187.5),(687.4,187.5),(687.4,187.5),(687.4,187.5)]
    points+=[(687.5,187.5),(687.5,187.5),(687.5,187.5)]
        # Right Turn
    points+=[(712.5,187.5),(712.5,187.5),(712.5,187.5),(712.5,187.5),(712.5,212.5),(712.5,487.5)]
    #17 holds
    points+=[(712.5,487.5),(712.5,487.5),(712.5,487.5),(712.5,487.5),(712.5,487.5),(712.5,487.5),(712.5,487.5),(712.5,487.5),(712.5,487.5),(712.5,487.5),(712.5,487.5),(712.5,487.5),(712.5,487.5),(712.5,487.5),(712.5,487.5),(712.5,487.5),(712.5,487.5),]
        #2 holds
    points+=[(712.5,487.5),(712.5,487.5)]    
    #Start Left Turn #39
    points+=[(712.5,512.5)]
    route_one = Route(points, canvas, car_color, offset=car_number)
    route_one.draw_points()
    
    xy = [(275,175),(300,175),(300,200),(275,200),(275,175)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    sprite2=canvas.create_text(points[0][0],points[0][1], font=("Arial",8), text=str(car_number))
    car_one = Car(sprite,sprite2, canvas, 287.5,187.5,25,25, route_one, car_number)
    
    all_cars.append(car_one)    
    
    
    # Intersection (middle) Cars first 4 --------------------------------------------------------------------------------
    car_color="red"
    
    #5
    car_number=5
    car_color="cyan"
    
    points=[(262.5,112.5),(287.5,112.5),(312.5,87.5),(337.5,87.5),(362.5,87.5),(387.5,87.5),(387.5,87.5),(412.5,112.5),(437.5,112.5),(462.5,112.5),(487.5,112.5)]
    points+=[(562.5,112.5),(612.5,112.5),(662.5,112.5)]
    points+=[(762.5,112.5),(787.5,112.5),(787.5,137.5),(787.5,162.5),(787.5,187.5),(787.5,187.5),(787.5,187.5),(787.5,187.5)]
    
    #extra hold time
    points+=[(787.5,187.5),(787.5,187.5),(787.5,187.5),(787.5,187.5)]
    
    #finish turn
    points+=[(787.5,212.5),(787.5, 237.5), (787.5, 262.5),(787.5, 287.5),(787.5, 312.5),(787.5, 337.5),(787.5, 362.5),(712.5,437.5)]
    
    # hold to prepare for left turn (X5)
    points+=[(712.5,437.5),(712.5,437.5),(712.5,437.5),(712.5,437.5),(712.5,437.5)]
    
    #begin left on wp 39?
    points+=[(712.5,462.5)]
    
    route_one = Route(points, canvas, car_color, offset=car_number)
    route_one.draw_points()
    
    xy = [(points[0][0]-12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]-12.5)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    sprite2=canvas.create_text(points[0][0],points[0][1], font=("Arial",8), text=str(car_number))
    car_one = Car(sprite,sprite2, canvas, points[0][0], points[0][1],25,25, route_one, car_number)
    
    all_cars.append(car_one)    
    
    #6
    car_number=6
    car_color="pink"
    
    points=[(262.5,137.5),(262.5,112.5),(287.5,112.5),(312.5,87.5),(337.5,87.5),(362.5,87.5),(362.5,87.5),(387.5,87.5),(412.5,112.5),(437.5,112.5),(462.5,112.5)]
    points+=[(487.5,112.5),(562.5,112.5),(612.5,112.5)]
    points+=[(712.5,112.5),(737.5,112.5),(762.5,112.5),(787.5,112.5),(787.5,137.5),(787.5,137.5),(787.5,137.5),(787.5,137.5)]
        #extra hold time
    points+=[(787.5,137.5),(787.5,137.5),(787.5,137.5),(787.5,137.5)]
    points+=[(787.5,162.5),(787.5,187.5),(787.5,212.5),(787.5,237.5),(787.5, 262.5),(787.5, 287.5),(787.5, 312.5),(787.5, 337.5),(787.5, 362.5),(712.5,387.5)]
            # hold to prepare for left turn (X3)
    points+=[(712.5,387.5),(712.5,387.5),(712.5,387.5)]
    points+=[(712.5,412.5)]
    route_one = Route(points, canvas, car_color, offset=car_number)
    route_one.draw_points()
    
    xy = [(points[0][0]-12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]-12.5)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    sprite2=canvas.create_text(points[0][0],points[0][1], font=("Arial",8), text=str(car_number))
    car_one = Car(sprite, sprite2, canvas, points[0][0], points[0][1],25,25, route_one, car_number)
    
    all_cars.append(car_one)    
    
    #7
    car_number=7
    car_color="purple"
    
    points=[(262.5,162.5),(262.5,187.5),(287.5,187.5),(312.5,212.5),(337.5,212.5),(362.5,212.5),(362.5,212.5),(387.5,212.5),(412.5,187.5),(437.5,187.5),(462.5,187.5)]
    points+=[(487.5,187.5),(537.5,112.5),(587.5,112.5)]
    points+=[(687.5,112.5),(712.5,112.5),(737.5,112.5),(762.5,112.5),(787.5,112.5),(787.5,112.5),(787.5,112.5),(787.5,112.5)]
        #extra hold time
    points+=[(787.5,112.5),(787.5,112.5),(787.5,112.5),(787.5,112.5)]
    points+=[(787.5,137.5),(787.5,162.5),(787.5,187.5),(787.5,212.5),(787.5,237.5),(787.5, 262.5),(787.5, 287.5),(787.5, 312.5),(787.5, 337.5),(787.5, 362.5),(712.5,362.5)]
                # hold to prepare for left turn (X2)
    points+=[(712.5,362.5),(712.5,362.5)]
    points+=[(712.5,387.5)]
    route_one = Route(points, canvas, car_color, offset=car_number)
    route_one.draw_points()
    
    xy = [(points[0][0]-12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]-12.5)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    sprite2=canvas.create_text(points[0][0],points[0][1], font=("Arial",8), text=str(car_number))
    car_one = Car(sprite, sprite2, canvas, points[0][0], points[0][1],25,25, route_one, car_number)
    
    all_cars.append(car_one)    
    
    #8
    car_number=8
    car_color="orange"
    
    points=[(262.5,187.5),(287.5,187.5),(312.5,212.5),(337.5,212.5),(362.5,212.5),(387.5,212.5),(387.5,212.5),(412.5,187.5),(437.5,187.5),(462.5,187.5),(487.5,187.5)]
    points+=[(537.5,112.5),(587.5,112.5),(637.5,112.5)]
    points+=[(737.5,112.5),(762.5,112.5),(787.5,112.5),(787.5,137.5),(787.5,162.5),(787.5,162.5),(787.5,162.5),(787.5,162.5)]
        #extra hold time
    points+=[(787.5,162.5),(787.5,162.5),(787.5,162.5),(787.5,162.5)]
    points+=[(787.5,187.5),(787.5,212.5),(787.5,237.5),(787.5, 262.5),(787.5, 287.5),(787.5, 312.5),(787.5, 337.5),(787.5, 362.5),(712.5,412.5)]
        # hold to prepare for left turn (X4)
    points+=[(712.5,412.5),(712.5,412.5),(712.5,412.5),(712.5,412.5)]
    points+=[(712.5,437.5)]
    
    route_one = Route(points, canvas, car_color, offset=car_number)
    route_one.draw_points()
    
    xy = [(points[0][0]-12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]-12.5)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    sprite2=canvas.create_text(points[0][0],points[0][1], font=("Arial",8), text=str(car_number))
    car_one = Car(sprite, sprite2, canvas, points[0][0], points[0][1],25,25, route_one, car_number)
    
    all_cars.append(car_one)

    car_color="red"
    
    # Intersection (middle) Cars 2nd 4 --------------------------------------------------------------------------------    
    #9
    car_number=9
    car_color="light cyan"
    
    points=[(237.5,112.5),(237.5,112.5),(262.5,112.5),(287.5,112.5),(312.5,87.5),(337.5,87.5),(337.5,87.5),(362.5,87.5),(387.5,87.5),(412.5,112.5),(437.5,112.5)]
    points+=[(462.5,112.5),(487.5,112.5),(562.5,112.5)]
    points+=[(662.5,112.5),(687.5,112.5),(712.5,112.5),(737.5,112.5),(762.5,112.5),(762.5,112.5),(762.5,112.5),(762.5,112.5)]
        #extra hold time
    points+=[(762.5,112.5),(762.5,112.5),(762.5,112.5),(762.5,112.5)]
    points+=[(787.5,112.5),(787.5,137.5),(787.5,162.5),(787.5,187.5),(787.5,212.5),(787.5,237.5),(787.5, 262.5),(787.5, 287.5),(787.5, 312.5),(787.5, 337.5),(787.5, 362.5),(737.5, 362.5)]
    
    # hold to prepare for left turn (X1)
    points+=[(737.5, 362.5)]
    points+=[(712.5,362.5)]
    
    route_one = Route(points, canvas, car_color, offset=car_number)
    route_one.draw_points()
    
    xy = [(points[0][0]-12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]-12.5)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    sprite2=canvas.create_text(points[0][0],points[0][1], font=("Arial",8), text=str(car_number))
    
    wait=[(6,1)]
    
    car_one = Car(sprite,sprite2, canvas, points[0][0], points[0][1],25,25, route_one, car_number, wait)
    
    all_cars.append(car_one)    
    
    #10
    car_number=10
    car_color="khaki1"
    
    points=[(237.5,137.5),(237.5,137.5),(237.5,112.5),(262.5,112.5),(287.5,112.5),(312.5,87.5),(312.5,87.5),(337.5,87.5),(362.5,87.5),(387.5,87.5),(412.5,112.5)]
    points+=[(437.5,112.5),(462.5,112.5),(512.5,112.5)]
    points+=[(612.5,112.5),(637.5,112.5),(662.5,112.5),(687.5,112.5),(712.5,112.5),(712.5,112.5),(712.5,112.5),(712.5,112.5)]
        #extra hold time
    points+=[(712.5,112.5),(712.5,112.5),(712.5,112.5),(712.5,112.5)]
    points+=[(737.5,112.5),(762.5,112.5),(787.5,112.5),(787.5,137.5),(787.5,162.5),(787.5,187.5),(787.5,212.5),(787.5,237.5),(787.5, 262.5),(787.5, 287.5),(787.5, 312.5),(787.5, 337.5),(787.5, 362.5)]
    #no hold needed
    points+=[(762.5, 362.5)]
    route_one = Route(points, canvas, car_color, offset=car_number)
    route_one.draw_points()
    
    xy = [(points[0][0]-12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]-12.5)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    sprite2=canvas.create_text(points[0][0],points[0][1], font=("Arial",8), text=str(car_number))
    
    wait=[(6,1)]
    
    car_one = Car(sprite, sprite2, canvas, points[0][0], points[0][1],25,25, route_one, car_number, wait)
    
    all_cars.append(car_one)    
    
    #11
    car_number=11
    car_color="salmon1"
    
    points=[(237.5,162.5),(237.5,162.5),(237.5,187.5),(262.5,187.5),(287.5,187.5),(312.5,212.5),(312.5,212.5),(337.5,212.5),(362.5,212.5),(387.5,212.5),(412.5,187.5)]
    points+=[(437.5,187.5),(462.5,187.5),(487.5,112.5)]
    points+=[(587.5,112.5),(612.5,112.5),(637.5,112.5),(662.5,112.5),(687.5,112.5),(712.5, 212.5),(712.5,462.5),(712.5,462.5)]
    
    # hold 17? times before start left turn
    points+=[(712.5,462.5),(712.5,462.5),(712.5,462.5),(712.5,462.5),(712.5,462.5),(712.5,462.5),(712.5,462.5),(712.5,462.5),(712.5,462.5),(712.5,462.5),(712.5,462.5),(712.5,462.5),(712.5,462.5),(712.5,462.5),(712.5,462.5),(712.5,462.5),(712.5,462.5)]
    
    # WP 39 start left turn
    points+=[(712.5, 487.5)]
    
    route_one = Route(points, canvas, car_color, offset=car_number)
    route_one.draw_points()
    
    xy = [(points[0][0]-12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]-12.5)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    sprite2=canvas.create_text(points[0][0],points[0][1], font=("Arial",8), text=str(car_number))
    
    wait=[(7,1)]
    
    car_one = Car(sprite, sprite2, canvas, points[0][0], points[0][1],25,25, route_one, car_number, wait)
    
    all_cars.append(car_one)    
    
    #12
    car_number=12
    car_color="OliveDrab1"
    
    points=[(237.5,187.5),(237.5,187.5),(262.5,187.5),(287.5,187.5),(312.5,212.5),(337.5,212.5),(337.5,212.5),(362.5,212.5),(387.5,212.5),(412.5,187.5),(437.5,187.5)]
    points+=[(462.5,187.5),(487.5,187.5),(537.5,112.5)]
    points+=[(637.5,112.5),(662.5,112.5),(687.5,112.5),(712.5,112.5),(737.5,112.5),(737.5,112.5),(737.5,112.5),(737.5,112.5)]
        #extra hold time
    points+=[(737.5,112.5),(737.5,112.5),(737.5,112.5),(737.5,112.5)]
    points+=[(762.5,112.5),(787.5,112.5),(787.5,137.5),(787.5,162.5),(787.5,187.5),(787.5,212.5),(787.5,237.5),(787.5, 262.5),(787.5, 287.5),(787.5, 312.5),(787.5, 337.5),(787.5, 362.5),(762.5, 362.5)]
    
    # no hold needed
    points+=[(737.5, 362.5)]
    
    route_one = Route(points, canvas, car_color, offset=car_number)
    route_one.draw_points()
    
    xy = [(points[0][0]-12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]-12.5)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    sprite2=canvas.create_text(points[0][0],points[0][1], font=("Arial",8), text=str(car_number))
    
    wait=[(7,1)]
    
    car_one = Car(sprite, sprite2, canvas, points[0][0], points[0][1],25,25, route_one, car_number, wait)
    
    all_cars.append(car_one)    
    
    # ------------------------BACK CARS--------------------
     #13
    car_number=13
    car_color="steel blue"
    
    points=[(62.5,112.5),(62.5,112.5),(87.5,112.5),(137.5,112.5),(162.5,112.5),(187.5,112.5),(375,112.5),(375,112.5),(375,112.5),(375,112.5),(375,112.5)]
    points+=[(412.5,112.5),(437.5,112.5),(437.5,112.5)]
    points+=[(537.5,112.5),(537.5,112.5),(537.5,112.5),(537.5,112.5),(537.5,112.5),(537.5,112.5),(662.5,112.5),(662.5,112.5),(687.5,137.5)]
        #execute wheel
    points+=[(737.5,137.5),(762.5,137.5),(762.5,162.5)]
    #hold and fill in
    points+=[(762.5,162.5),(762.5,162.5),(762.5,162.5),(762.5,162.5),(762.5,162.5),(762.5,162.5),(787.5,187.5),(787.5,187.5)]
    # two extra holds to bring to 10
    points+=[(787.5,187.5),(787.5,187.5)]
        #WP 36 move up
    points+=[(787.5,237.5)]
    route_one = Route(points, canvas, car_color, offset=car_number)
    route_one.draw_points()
    
    xy = [(points[0][0]-12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]-12.5)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    sprite2=canvas.create_text(points[0][0],points[0][1], font=("Arial",8), text=str(car_number))
    
    wait=[(7,1)]
    
    car_one = Car(sprite, sprite2, canvas, points[0][0], points[0][1],25,25, route_one, car_number, wait)
    
    all_cars.append(car_one)    
   
   #14
    car_number=14
    car_color="gold"
    
    points=[(62.5,137.5),(62.5,137.5),(87.5,137.5),(137.5,137.5),(162.5,137.5),(187.5,137.5),(375,137.5),(375,137.5),(375,137.5),(375,137.5),(375,137.5)]
    points+=[(412.5,137.5),(437.5,137.5),(437.5,137.5)]
    points+=[(537.5,137.5),(537.5,137.5),(537.5,137.5),(537.5,137.5),(537.5,137.5),(537.5,137.5),(687.5,137.5),(687.5,137.5),(712.5,137.5)]
    #execute wheel
    points+=[(762.5,137.5),(762.5,162.5),(762.5,187.5)]
    
    #Hold and catch up to marchers
    #WP 26
    # 10 holds
    points+=[(762.5,187.5),(762.5,187.5),(762.5,187.5),(762.5,187.5),(762.5,187.5),(762.5,187.5),(762.5,187.5),(762.5,187.5),(762.5,187.5),(762.5,187.5)]
    
    #WP 36 move up
    points+=[(762.5,237.5)]
    
    route_one = Route(points, canvas, car_color, offset=car_number)
    route_one.draw_points()
    
    xy = [(points[0][0]-12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]-12.5)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    sprite2=canvas.create_text(points[0][0],points[0][1], font=("Arial",8), text=str(car_number))
    
    wait=[(7,1)]
    
    car_one = Car(sprite, sprite2, canvas, points[0][0], points[0][1],25,25, route_one, car_number, wait)
    
    all_cars.append(car_one)    
   
   #15
    car_number=15
    car_color="sea green"
    
    points=[(62.5,162.5),(62.5,162.5),(87.5,162.5),(137.5,162.5),(162.5,162.5),(187.5,162.5),(375,162.5),(375,162.5),(375,162.5),(375,162.5),(375,162.5)]
    points+=[(412.5,162.5),(437.5,162.5),(437.5,162.5)]
    points+=[(537.5,162.5),(537.5,162.5),(537.5,162.5),(537.5,162.5),(537.5,162.5),(537.5,162.5),(687.5,162.5),(687.5,162.5),(712.5,162.5)]
        #execute wheel
    points+=[(737.5,162.5),(737.5,162.5),(737.5,187.5)]
        #Hold and catch up to marchers
    #WP 26
    # 10 holds
    points+=[(737.5,187.5),(737.5,187.5),(737.5,187.5),(737.5,187.5),(737.5,187.5),(737.5,187.5),(737.5,187.5),(737.5,187.5),(737.5,187.5),(737.5,187.5)]
        #WP 36 move up
    points+=[(737.5,237.5)]
    
    route_one = Route(points, canvas, car_color, offset=car_number)
    route_one.draw_points()
    
    xy = [(points[0][0]-12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]-12.5)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    sprite2=canvas.create_text(points[0][0],points[0][1], font=("Arial",8), text=str(car_number))
    
    wait=[(7,1)]
    
    car_one = Car(sprite, sprite2, canvas, points[0][0], points[0][1],25,25, route_one, car_number, wait)
    
    all_cars.append(car_one)    
    
    #16
    car_number=16
    car_color="firebrick4"
    
    points=[(62.5,187.5),(62.5,187.5),(87.5,187.5),(137.5,187.5),(162.5,187.5),(187.5,187.5),(375,187.5),(375,187.5),(375,187.5),(375,187.5),(375,187.5)]
    points+=[(412.5,187.5),(437.5,187.5),(437.5,187.5)]
    points+=[(537.5,187.5),(537.5,187.5),(537.5,187.5),(537.5,187.5),(537.5,187.5),(537.5,187.5),(687.5,187.5),(687.5,187.5),(712.5,187.5)]
        #execute wheel
    points+=[(712.5,187.5),(712.5,187.5),(712.5,187.5)]
        #Hold and catch up to marchers
    #WP 26
    # 10 holds
    points+=[(712.5,187.5),(712.5,187.5),(712.5,187.5),(712.5,187.5),(712.5,187.5),(712.5,187.5),(712.5,187.5),(712.5,187.5),(712.5,187.5),(712.5,187.5)]    
        #WP 36 move up
    points+=[(712.5,237.5)]
    route_one = Route(points, canvas, car_color, offset=car_number)
    route_one.draw_points()
    
    xy = [(points[0][0]-12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]-12.5)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    sprite2=canvas.create_text(points[0][0],points[0][1], font=("Arial",8), text=str(car_number))
    
    wait=[(7,1)]
    
    car_one = Car(sprite, sprite2, canvas, points[0][0], points[0][1],25,25, route_one, car_number, wait)
    
    all_cars.append(car_one)    
    
    # MARCHERS
    car_number=99
    car_color="orchid3"
    
    points=[(150,150),(150,150),(175,150),(200,150),(225,150),(250,150),(600,150),(600,150),(600,150),(600,150),(600,150)]
    points+=[(600,162.5),(600,162.5),(600,162.5)]
    points+=[(600,162.5),(600,162.5),(600,162.5),(600,162.5),(600,162.5),(600,162.5),(737.5,162.5),(737.5,300)]
    points+=[]
    route_one = Route(points, canvas, car_color, offset=car_number)
    route_one.draw_points()
    
    xy = [(points[0][0]-37.5,points[0][1]-37.5),(points[0][0]+37.5,points[0][1]-37.5),(points[0][0]+37.5,points[0][1]+37.5),(points[0][0]-37.5,points[0][1]+37.5),(points[0][0]-37.5,points[0][1]-37.5)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    sprite2=canvas.create_text(points[0][0],points[0][1], font=("Arial",8), text='MARCHERS')
    
    wait=[(7,1)]
    
    car_one = Car(sprite, sprite2, canvas, points[0][0], points[0][1],25,25, route_one, car_number, wait)
    
    all_cars.append(car_one) 
    
    return all_cars
    


        
        