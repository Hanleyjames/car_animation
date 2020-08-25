print('test123')

#Roads should be in the center of the window, and take up 1/6 of the window width
def create_roads(canvas, window, scale):
    print('called create roads') 
    print("height:",window.winfo_height())
    print("width:",window.winfo_width())
    #print(window.winfo_reqheight())
    #print(window.winfo_reqwidth())
    #Method constants
    seg_width=2
    
    road_segs=[]
    
    #left road
    #left line
    window_bottom=window.winfo_height()
    window_top=0
    window_left=0
    window_right=window.winfo_width()
    road_center=window_right/2
    x1=int(road_center-window_right/12)
    x2=int(road_center-window_right/12)+seg_width
    y1=-1*window_bottom
    y2=window_bottom
    seg = canvas.create_rectangle(x1,
        y1,
        x2,
        y2,
        fill="black", outline="black", width=1)
    road_segs.append(seg)
    
    #right line
    window_bottom=window.winfo_height()
    window_top=0
    window_left=0
    window_right=window.winfo_width()
    road_center=window_right/2
    x1=int(road_center+window_right/12)
    x2=int(road_center+window_right/12)+seg_width
    y1=-1*window_bottom
    y2=window_bottom
    seg = canvas.create_rectangle(x1,
        y1,
        x2,
        y2,
        fill="black", outline="black", width=1)
    road_segs.append(seg)


    # intersection 1, left road
    #bottom line
    
    x1=0
    x2=int(road_center-window_right/12)
    y1=-1*window_bottom-int(window_right/6) 
    y2=-1*window_bottom-int(window_right/6)-seg_width
    
    seg = canvas.create_rectangle(x1,
        y1,
        x2,
        y2,
        fill="black", outline="black", width=1)
    road_segs.append(seg)

    #top line
    x1=0
    x2=int(road_center-window_right/12)
    y1=-1*window_bottom 
    y2=-1*window_bottom-seg_width
    
    seg = canvas.create_rectangle(x1,
        y1,
        x2,
        y2,
        fill="black", outline="black", width=1)
    road_segs.append(seg)
    
    return road_segs
    
def move_roads(canvas, road_list,rmx,rmy):
    #print('testing move_raods') 
    for road in road_list:
        canvas.move(road,rmx,rmy)
    