import CarObj

def create_cars(canvas, window):
    
    all_cars=[]
    
    # Front Cars ------------------------------------------------------------------------
    #1
    car_color="yellow"
    car_number=1
    points=[(287.5,112.5),(412.4,112.5),(787.5,112.5),(787.5,512.5),(1200,512.5)]
    route_one = Route(points, canvas, car_color)
    route_one.draw_points()
    
    xy = [(275,100),(300,100),(300,125),(275,125),(275,125)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    sprite2=canvas.create_text(points[0][0],points[0][1], font=("Arial",8), text=str(car_number))
    
    car_one = Car(sprite, sprite2, canvas, 287.5,112.5,25,25, route_one, car_number)
    
    all_cars.append(car_one)
    
    #2
    car_number=2
    car_color="green"
    
    points=[(287.5,137.5),(412.4,137.5),(762.5,137.5),(762.5,537.5),(1200,537.5)]
    route_one = Route(points, canvas, car_color)
    route_one.draw_points()
    
    xy = [(275,125),(300,125),(300,150),(275,150),(275,150)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    sprite2=canvas.create_text(points[0][0],points[0][1], font=("Arial",8), text=str(car_number))
    car_one = Car(sprite,sprite2, canvas, 287.5,137.5,25,25, route_one, car_number)
    
    all_cars.append(car_one)    
 
    #3
    car_number=3
    car_color="blue"
    
    points=[(287.5,162.5),(412.4,162.5),(737.5,162.5),(737.5,562.5),(1200,562.5)]
    route_one = Route(points, canvas, car_color)
    route_one.draw_points()
    
    xy = [(275,150),(300,150),(300,175),(275,175),(275,150)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    sprite2=canvas.create_text(points[0][0],points[0][1], font=("Arial",8), text=str(car_number))
    car_one = Car(sprite,sprite2, canvas, 287.5,162.5,25,25, route_one, car_number)
    
    all_cars.append(car_one)   
    
    #4
    car_number=4
    car_color="red"
    
    points=[(287.5,187.5),(412.4,187.5),(712.5,187.5),(712.5,587.5),(1200,587.5)]
    route_one = Route(points, canvas, car_color)
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
    
    points=[(262.5,112.5),(387.5,112.5),(787.5,112.5),(787.5,512.5),(1200,512.5)]
    route_one = Route(points, canvas, car_color)
    route_one.draw_points()
    
    xy = [(points[0][0]-12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]-12.5)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    sprite2=canvas.create_text(points[0][0],points[0][1], font=("Arial",8), text=str(car_number))
    car_one = Car(sprite,sprite2, canvas, points[0][0], points[0][1],25,25, route_one, car_number)
    
    all_cars.append(car_one)    
    
    #6
    car_number=6
    car_color="pink"
    
    points=[(262.5,137.5),(262.5,112.5),(387.5,112.5),(787.5,112.5),(787.5,512.5),(1200,512.5)]
    route_one = Route(points, canvas, car_color)
    route_one.draw_points()
    
    xy = [(points[0][0]-12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]-12.5)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    sprite2=canvas.create_text(points[0][0],points[0][1], font=("Arial",8), text=str(car_number))
    car_one = Car(sprite, sprite2, canvas, points[0][0], points[0][1],25,25, route_one, car_number)
    
    all_cars.append(car_one)    
    
    #7
    car_number=7
    car_color="purple"
    
    points=[(262.5,162.5),(262.5,187.5),(387.5,187.5),(787.5,187.5),(787.5,512.5),(1200,512.5)]
    route_one = Route(points, canvas, car_color)
    route_one.draw_points()
    
    xy = [(points[0][0]-12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]-12.5)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    sprite2=canvas.create_text(points[0][0],points[0][1], font=("Arial",8), text=str(car_number))
    car_one = Car(sprite, sprite2, canvas, points[0][0], points[0][1],25,25, route_one, car_number)
    
    all_cars.append(car_one)    
    
    #8
    car_number=8
    car_color="orange"
    
    points=[(262.5,187.5),(262.5,187.5),(387.5,187.5),(787.5,187.5),(787.5,512.5),(1200,512.5)]
    route_one = Route(points, canvas, car_color)
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
    car_color="cyan"
    
    points=[(237.5,112.5)]
    route_one = Route(points, canvas, car_color)
    route_one.draw_points()
    
    xy = [(points[0][0]-12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]-12.5)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    sprite2=canvas.create_text(points[0][0],points[0][1], font=("Arial",8), text=str(car_number))
    
    wait=[(9,0)]
    
    car_one = Car(sprite,sprite2, canvas, points[0][0], points[0][1],25,25, route_one, car_number, wait_instr=wait)
    
    all_cars.append(car_one)    
    
    #10
    car_number=10
    car_color="pink"
    
    points=[(237.5,137.5)]
    route_one = Route(points, canvas, car_color)
    route_one.draw_points()
    
    xy = [(points[0][0]-12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]-12.5)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    sprite2=canvas.create_text(points[0][0],points[0][1], font=("Arial",8), text=str(car_number))
    car_one = Car(sprite, sprite2, canvas, points[0][0], points[0][1],25,25, route_one, car_number)
    
    all_cars.append(car_one)    
    
    #11
    car_number=11
    car_color="purple"
    
    points=[(237.5,162.5)]
    route_one = Route(points, canvas, car_color)
    route_one.draw_points()
    
    xy = [(points[0][0]-12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]-12.5)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    sprite2=canvas.create_text(points[0][0],points[0][1], font=("Arial",8), text=str(car_number))
    car_one = Car(sprite, sprite2, canvas, points[0][0], points[0][1],25,25, route_one, car_number)
    
    all_cars.append(car_one)    
    
    #12
    car_number=12
    car_color="orange"
    
    points=[(237.5,187.5)]
    route_one = Route(points, canvas, car_color)
    route_one.draw_points()
    
    xy = [(points[0][0]-12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]-12.5),(points[0][0]+12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]+12.5),(points[0][0]-12.5,points[0][1]-12.5)]
    sprite = canvas.create_polygon(xy, fill=car_color, outline="black", width=1)
    sprite2=canvas.create_text(points[0][0],points[0][1], font=("Arial",8), text=str(car_number))
    car_one = Car(sprite, sprite2, canvas, points[0][0], points[0][1],25,25, route_one, car_number)
    
    all_cars.append(car_one)    
    return all_cars