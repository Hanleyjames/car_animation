#define the radius of the person
person_head_radius = 10
#create groups of people
def create_group(canvas):
    person_one_x_start = 20
    person_one_y_start = 20
    for i in range(0,5):
        crowd = canvas.create_oval(person_one_x_start - person_head_radius,
                person_one_y_start - person_head_radius,
                person_one_x_start + person_head_radius,
                person_one_y_start + person_head_radius,
                fill="blue", outline="black", width=1)
        person_one_x_start += 20
