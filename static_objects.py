def create_roads(canvas, window):
    
    window_bottom=window.winfo_height()
    window_top=0
    window_left=0
    window_right=window.winfo_width()
    
    print("creating roads", window_right, window_bottom)
    
    ROAD_WIDTH=window_right/12
    LINE_WIDTH=1
    OFFSET=100
    
    
    road_segs=[]
    #vertical streets
    num_vert=3
    for i in range (0,num_vert+1):
        x1=i*(window_right/num_vert)+OFFSET
        print(x1)
        x2=x1+LINE_WIDTH
        
        y1=window_top
        y2=window_bottom
        
        seg = canvas.create_rectangle(x1,
            y1,
            x2,
            y2,
            fill="black", outline="black", width=1)
        coord=canvas.create_text(x1,y1+20, font="Arial",
        text=str(x1))
        
        x1=x1+ROAD_WIDTH
        x2=x2+ROAD_WIDTH
        
        y1=window_top
        y2=window_bottom
        
        seg = canvas.create_rectangle(x1,
            y1,
            x2,
            y2,
            fill="black", outline="black", width=1)    
        coord=canvas.create_text(x1,y1+20, font="Arial",
        text=str(x1))    
        road_segs.append(seg)
    
    #Horizontal Streets
    
    num_horz=2
    OFFSET=100
    for i in range (0,num_horz+1):
        x1=window_left
        x2=window_right
        y1=OFFSET+(i*window_bottom/num_horz*.75)
        y2=y1+LINE_WIDTH
        seg = canvas.create_rectangle(x1,
            y1,
            x2,
            y2,
            fill="black", outline="black", width=1)    
        
        coord=canvas.create_text(x1+50,y1, font="Arial",
        text=str(y1))    
        
        road_segs.append(seg)    

        x1=window_left
        x2=window_right
        y1=y1+ROAD_WIDTH
        y2=y1+LINE_WIDTH
        seg = canvas.create_rectangle(x1,
            y1,
            x2,
            y2,
            fill="black", outline="black", width=1)    
        
        coord=canvas.create_text(x1+50,y1, font="Arial",
        text=str(y1))    
        road_segs.append(seg)

    return road_segs
        
def draw_grids(canvas, window):
    window_bottom=window.winfo_height()
    window_top=0
    window_left=0
    window_right=window.winfo_width()
    
    GRID_SPACE=25
    
    i=0
    while i<window_bottom:
        canvas.create_line(window_left, i, window_right, i, dash=(4, 2))
        canvas.create_text(window_left+25,i, font=("Arial",8),
            text=str(i))
        i+=GRID_SPACE
    
    i=0
    while i<window_right:
        canvas.create_line(i, window_top, i, window_bottom, dash=(4, 2))
        canvas.create_text(i, window_top+25, font=("Arial",8),
            text=str(i))
        i+=GRID_SPACE    
            