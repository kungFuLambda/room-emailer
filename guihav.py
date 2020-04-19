#gui to get all the room numnbers that have received mail
import tkinter as tk




rooms = []


def get_rooms():

    
    root = tk.Tk()

    canvas = tk.Canvas(root,height = 400,width = 160,bg = "white",confine = True,relief = "ridge")
    canvas.pack()

    frame = tk.Frame(root)
    frame.pack()

#################printer#########################

    def redraw():
        canvas.delete("all")
        p1 = 20
        p2 = 20
        for r in rooms:
            canvas.create_text(p1,p2,text= str(r))
            p2 += 20
#################################################
    
    
    insertroom = tk.Entry(frame)
    insertroom.pack(side = "top")
    insertroom.insert(0,"room number: ")

    def add_rooms_list(e=1):
        r = insertroom.get().split(": ")
        if r[1] != "":
            rooms.append(r[1])
            insertroom.delete(13,17)
            redraw()

    def remove_rooms_list():
        r = insertroom.get().split(": ")
        if r[1] != "":
            rooms.remove(r[1])
            insertroom.delete(13,17)
            redraw()

    addroom = tk.Button(frame,text="add to email list",command = add_rooms_list)
    addroom.pack()

    removeroom = tk.Button(frame,text="remove", command = remove_rooms_list)
    removeroom.pack()

    #addroom.bind("<Enter>",add_rooms_list)
    


    doneg = tk.Button(root,text = "finished",command = root.destroy)
    doneg.pack()
    









    root.mainloop()
    return rooms


