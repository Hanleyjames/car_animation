print('hello') 

def create_cars(canvas, window, scale):
    
    cars=[]
    window_bottom=window.winfo_height()
    window_top=0
    window_left=0
    window_right=window.winfo_width()
    road_center=window_right/2
    road_width=window_right/6

    
    NUM_WIDE=4
    NUM_TALL=3
    
    car_w=road_width/NUM_WIDE
    car_h=road_width/NUM_TALL
    
    
    
    FRONT_SPACE=200
    CAR_SPACER=2
    
    CAR_NUMBER=0
    
    #Initiate Front Cars
    
    #Front position  
    FRONT_START=window_bottom - (NUM_TALL*car_h + FRONT_SPACE)
    
    for i in range (0,NUM_WIDE):
        x1=road_center-(.5*road_width)+i*CAR_SPACER+i*car_w - (NUM_WIDE/2 * CAR_SPACER)
        x2=x1+car_w
        y1=FRONT_START
        y2=y1+car_h
        
        seg = canvas.create_rectangle(x1,
        y1,
        x2,
        y2,
        fill="green", outline="black", width=1)
        cars.append(seg)        
    
    #Init Side Cars
    for i in range (0,NUM_WIDE):
        x1=road_center-(.5*road_width)+i*CAR_SPACER+i*car_w - (NUM_WIDE/2 * CAR_SPACER)
        x2=x1+car_w
        y1=FRONT_START+ car_h+CAR_SPACER
        y2=y1+car_h
        
        seg = canvas.create_rectangle(x1,
        y1,
        x2,
        y2,
        fill="yellow", outline="black", width=1)
        cars.append(seg) 
    #Init Side Cars #2
    for i in range (0,NUM_WIDE):
        x1=road_center-(.5*road_width)+i*CAR_SPACER+i*car_w - (NUM_WIDE/2 * CAR_SPACER)
        x2=x1+car_w
        y1=FRONT_START+ 2*(car_h+CAR_SPACER)
        y2=y1+car_h
        
        seg = canvas.create_rectangle(x1,
        y1,
        x2,
        y2,
        fill="yellow", outline="black", width=1)
        cars.append(seg) 

 
    #Init Back Cars
    for i in range (0,NUM_WIDE):
        x1=road_center-(.5*road_width)+i*CAR_SPACER+i*car_w - (NUM_WIDE/2 * CAR_SPACER)
        x2=x1+car_w
        y1=window_bottom
        y2=y1-car_h
        
        seg = canvas.create_rectangle(x1,
        y1,
        x2,
        y2,
        fill="red", outline="black", width=1)
        cars.append(seg)     
    
    return cars
            