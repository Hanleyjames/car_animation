print('hello') 

def create_cars(canvas, window, scale):
    
    cars=[]
    window_bottom=window.winfo_height()
    window_top=0
    window_left=0
    window_right=window.winfo_width()
    road_center=window_right/2
    
    car_w=25
    car_h=25
    
    NUM_WIDE=4
    NUM_TALL=3
    
    #Initiate Front Cars
    
    #Init Side Cars
    
    #Init Back Cars
    
    
    for i in range (0,5):
        for j in range (0,5):
        
            x1=road_center-3*car_w + (i%5) * car_w 
            x2=x1+car_w
            y1=window_bottom - car_h*j - 50
            y2=y1-car_h
            
            seg = canvas.create_rectangle(x1,
            y1,
            x2,
            y2,
            fill="yellow", outline="black", width=1)
            cars.append(seg)
    return cars
            