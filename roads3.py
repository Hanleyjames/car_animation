def create_roads(canvas, window):
    
    window_bottom=window.winfo_height()
    window_top=0
    window_left=0
    window_right=window.winfo_width()
    
    #Road 1 
    canvas.create_line(0, 100, 300, 100)
    canvas.create_line(0, 200, 300, 200)
    canvas.create_line(400, 100, 700, 100)
    canvas.create_line(400, 200, 700, 200)
    canvas.create_line(800, 100, window_right, 100)
    canvas.create_line(800, 200, window_right, 200)    
    
    #road 2 (not taken)
    canvas.create_line(300, 0, 300, 100)
    canvas.create_line(400, 0, 400, 100)
    canvas.create_line(300, 200, 300, 500)
    canvas.create_line(400, 200, 400, 500)  
    canvas.create_line(300, 600, 300, window_bottom)
    canvas.create_line(400, 600, 400, window_bottom)
    # road 3    (first right turn)
    canvas.create_line(700, 0, 700, 100)
    canvas.create_line(800, 0, 800, 100)
    canvas.create_line(700, 200, 700, 500)
    canvas.create_line(800, 200, 800, 500)
    canvas.create_line(700, 600, 700, window_bottom)
    canvas.create_line(800, 600, 800, window_bottom) 

    #road 4 (first left turn)
    canvas.create_line(0, 500, 300, 500)
    canvas.create_line(0, 600, 300, 600)
    canvas.create_line(400, 500, 700, 500)
    canvas.create_line(400, 600, 700, 600)
    canvas.create_line(800, 500, window_right, 500)
    canvas.create_line(800, 600, window_right, 600)      