#define the radius of the person
person_head_radius = 10
#define person start points
person_one_x_start = 20
person_one_y_start = 20
person_two_x_start = 30
person_two_y_start = 20
person_three_x_start = 40
person_three_y_start = 20
#Not really sure yet why window needs to be created
def create_group(window, canvas, xinc, yinc):
    crowd = canvas.create_oval(person_one_x_start - person_head_radius,
                person_one_y_start - person_head_radius,
                person_one_x_start + person_head_radius,
                person_one_y_start + person_head_radius,
                fill="blue", outline="black", width=1),
            canvas.create_oval(person_two_x_start - person_head_radius,
                person_two_y_start - person_head_radius,
                person_two_x_start + person_head_radius,
                person_two_y_start + person_head_radius,
                fill="blue", outline="black", width=1),
            canvas.create_oval(person_three_x_start - person_head_radius,
                person_three_y_start - person_head_radius,
                person_three_x_start + person_head_radius,
                person_three_y_start + person_head_radius,
                fill="blue", outline="black", width=1)
