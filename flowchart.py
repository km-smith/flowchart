from tkinter import *

#width x height of all objects
DIAMOND_SIZE = [300,200]

CIRCLE_SIZE = [300,200]

RECTANGLE_SIZE = [300,200]

PARALLELOGRAM_SIZE = [300,200]

ARROW_SIZE = 300

DOT_SIZE = 10

COLOR = "#000044"

#instating the window
window = Tk()
window.title("Flowchart Maker")
#instating the canvas that fills the whole window even when expanded
canvas = Canvas(window,bg="#000000")
canvas.pack(fill="both", expand=True)


#CREATION OF CLASSES

#click function: this basically just finds the place that the user clicked inside the object
#without this the program wouldn't be able to find the distance between point A and B

#drag function: this finds where the cursor is now and subtracts the distance between where the cursor is to where it was
#Then the program uses canvas.move() to move the object however many units and then sets the last click position to where the cursor is now for future calls

#__init__ function: each time an object is created, it gets the width x height constants and is created at a specific location
#it looks like a lot of math, but in reality it is the size of every object above itself + 20 for spacing between each object

#show: This is going to just show the dots for each object that is clicked

#hide: the opposite of show.
#It is a little tricky to get it to work though. I need to make it so that the dots show when the object is clicked, but stop showing when the object is clicked off of



class Circle:
    def click(self, event):
        #coordinates of the place we click the label at (Point A)
        self.click_x = event.x
        self.click_y = event.y
        print("Click:",self.click_x,self.click_y)
        
        canvas.itemconfigure("dot",state="normal")
    
    def drag(self, event):
        #coordinates of the place we are dragging the widget to (Point B)
        pointer_x=event.x
        pointer_y=event.y
        print("Pointer:",pointer_x,pointer_y)
        
        #distance between Point A and Point B for x and y
        x = pointer_x - self.click_x
        print("X: {}-{} = {}".format(pointer_x,self.click_x,x))
        y = pointer_y - self.click_y
        print("Y: {}-{} = {}".format(pointer_y,self.click_y,y))
        
        canvas.move(self.circle, x, y)
        canvas.move(self.dot1, x, y)
        canvas.move(self.dot2, x, y)
        canvas.move(self.dot3, x, y)
        canvas.move(self.dot4, x, y)
        
        self.click_x = pointer_x
        self.click_y = pointer_y
    
    def __init__(self, color):
        self.circle = canvas.create_oval(10,10,10+CIRCLE_SIZE[0],10+CIRCLE_SIZE[1], fill=color,width=4,outline="black")
        self.coords = canvas.coords(self.circle)
        print(self.coords)
        
        self.dot1 = canvas.create_oval(((self.coords[2]/2)-DOT_SIZE,self.coords[1]-DOT_SIZE),
                                              ((self.coords[2]/2)+DOT_SIZE,self.coords[1]+DOT_SIZE),
                                              fill="white", outline="black", width=3, state="hidden", tag="dot")
        self.dot2 = canvas.create_oval((self.coords[0]-DOT_SIZE,(self.coords[3]/2)-DOT_SIZE),
                                              (self.coords[0]+DOT_SIZE,(self.coords[3]/2)+DOT_SIZE),
                                              fill="white", outline="black", width=3, state="hidden", tag="dot")
        self.dot3 = canvas.create_oval((self.coords[2]-DOT_SIZE,(self.coords[3]/2)-DOT_SIZE),
                                              (self.coords[2]+DOT_SIZE,(self.coords[3]/2)+DOT_SIZE),
                                              fill="white", outline="black", width=3, state="hidden", tag="dot")
        self.dot4 = canvas.create_oval(((self.coords[2]/2)-DOT_SIZE,self.coords[3]-DOT_SIZE),
                                              ((self.coords[2]/2)+DOT_SIZE,self.coords[3]+DOT_SIZE),
                                              fill="white", outline="black", width=3, state="hidden", tag="dot")
        
        
        canvas.tag_bind(self.circle,"<Button-1>",self.click)
        canvas.tag_bind(self.circle,"<B1-Motion>",self.drag)

class Rectangle:
    def click(self, event):
        #coordinates of the place we click the label at (Point A)
        self.click_x = event.x
        self.click_y = event.y
        print("Click:",self.click_x,self.click_y)
        
        canvas.itemconfig(self.dot1, state="normal")
        canvas.itemconfig(self.dot2, state="normal")
        canvas.itemconfig(self.dot3, state="normal")
        canvas.itemconfig(self.dot4, state="normal")

    def drag(self, event):
        #coordinates of the place we are dragging the widget to (Point B)
        pointer_x=event.x
        pointer_y=event.y
        print("Pointer:",pointer_x,pointer_y)
        
        #distance between Point A and Point B for x and y
        x = pointer_x - self.click_x
        print("X: {}-{} = {}".format(pointer_x,self.click_x,x))
        y = pointer_y - self.click_y
        print("Y: {}-{} = {}".format(pointer_y,self.click_y,y))
        
        canvas.move(self.rectangle, x, y)
        canvas.move(self.dot1, x, y)
        canvas.move(self.dot2, x, y)
        canvas.move(self.dot3, x, y)
        canvas.move(self.dot4, x, y)
        
        self.click_x = pointer_x
        self.click_y = pointer_y
    
    def __init__(self, color):
        self.rectangle = canvas.create_rectangle(10,(CIRCLE_SIZE[1]+20),
                                                 10+RECTANGLE_SIZE[0],(CIRCLE_SIZE[1]+20)+RECTANGLE_SIZE[1],
                                                 fill=color,width=4,outline="black")
        self.coords = canvas.coords(self.rectangle)
        
        self.dot1 = canvas.create_oval((self.coords[0]-DOT_SIZE,self.coords[1]-DOT_SIZE),
                                              (self.coords[0]+DOT_SIZE,self.coords[1]+DOT_SIZE),
                                              fill="white", outline="black", width=3, state="hidden")
        self.dot2 = canvas.create_oval((self.coords[0]-DOT_SIZE,self.coords[3]-DOT_SIZE),
                                              (self.coords[0]+DOT_SIZE,self.coords[3]+DOT_SIZE),
                                              fill="white", outline="black", width=3, state="hidden")
        self.dot3 = canvas.create_oval((self.coords[2]-DOT_SIZE,self.coords[1]-DOT_SIZE),
                                              (self.coords[2]+DOT_SIZE,self.coords[1]+DOT_SIZE),
                                              fill="white", outline="black", width=3, state="hidden")
        self.dot4 = canvas.create_oval((self.coords[2]-DOT_SIZE,self.coords[3]-DOT_SIZE),
                                              (self.coords[2]+DOT_SIZE,self.coords[3]+DOT_SIZE),
                                              fill="white", outline="black", width=3, state="hidden")
        
        canvas.tag_bind(self.rectangle,"<Button-1>",self.click)
        canvas.tag_bind(self.rectangle,"<B1-Motion>",self.drag)

class Diamond:
    def click(self, event):
        #coordinates of the place we click the label at (Point A)
        self.click_x = event.x
        self.click_y = event.y
        print("Click:",self.click_x,self.click_y)
        
        canvas.itemconfig(self.dot1, state="normal")
        canvas.itemconfig(self.dot2, state="normal")
        canvas.itemconfig(self.dot3, state="normal")
        canvas.itemconfig(self.dot4, state="normal")

    def drag(self, event):
        #coordinates of the place we are dragging the widget to (Point B)
        pointer_x=event.x
        pointer_y=event.y
        print("Pointer:",pointer_x,pointer_y)
        
        #distance between Point A and Point B for x and y
        x = pointer_x - self.click_x
        print("X: {}-{} = {}".format(pointer_x,self.click_x,x))
        y = pointer_y - self.click_y
        print("Y: {}-{} = {}".format(pointer_y,self.click_y,y))
        
        canvas.move(self.diamond, x, y)
        canvas.move(self.dot1, x, y)
        canvas.move(self.dot2, x, y)
        canvas.move(self.dot3, x, y)
        canvas.move(self.dot4, x, y)
        
        self.click_x = pointer_x
        self.click_y = pointer_y
        
    def drag(self, event):
        #coordinates of the place we are dragging the widget to (Point B)
        pointer_x=event.x
        pointer_y=event.y
        print("Pointer:",pointer_x,pointer_y)
        
        #distance between Point A and Point B for x and y
        x = pointer_x - self.click_x
        print("X: {}-{} = {}".format(pointer_x,self.click_x,x))
        y = pointer_y - self.click_y
        print("Y: {}-{} = {}".format(pointer_y,self.click_y,y))
        
        canvas.move(self.arrow, x, y)
        canvas.move(self.dot1, x, y)
        canvas.move(self.dot2, x, y)
        
        self.click_x = pointer_x
        self.click_y = pointer_y
    
    def __init__(self, color):
        self.diamond = canvas.create_polygon((10+ (DIAMOND_SIZE[0] / 2), (RECTANGLE_SIZE[1]+20+CIRCLE_SIZE[1]+20)),
                                             (10, (RECTANGLE_SIZE[1]+20+CIRCLE_SIZE[1]+20) + (DIAMOND_SIZE[1] / 2)),
                                             (10+ (DIAMOND_SIZE[0] / 2), (RECTANGLE_SIZE[1]+20+CIRCLE_SIZE[1]+20)  + DIAMOND_SIZE[1]),
                                             (10+ DIAMOND_SIZE[0], (RECTANGLE_SIZE[1]+20+CIRCLE_SIZE[1]+20) + (DIAMOND_SIZE[1] / 2)),
                                             fill=color,width=4,outline="black")
        self.coords = canvas.coords(self.diamond)
        
        self.dot1 = canvas.create_oval((self.coords[0]-DOT_SIZE,self.coords[1]-DOT_SIZE),
                                              (self.coords[0]+DOT_SIZE,self.coords[1]+DOT_SIZE),
                                              fill="white", outline="black", width=3, state="hidden")
        self.dot2 = canvas.create_oval((self.coords[2]-DOT_SIZE,self.coords[3]-DOT_SIZE),
                                              (self.coords[2]+DOT_SIZE,self.coords[3]+DOT_SIZE),
                                              fill="white", outline="black", width=3, state="hidden")
        self.dot3 = canvas.create_oval((self.coords[4]-DOT_SIZE,self.coords[5]-DOT_SIZE),
                                              (self.coords[4]+DOT_SIZE,self.coords[5]+DOT_SIZE),
                                              fill="white", outline="black", width=3, state="hidden")
        self.dot4 = canvas.create_oval((self.coords[6]-DOT_SIZE,self.coords[7]-DOT_SIZE),
                                              (self.coords[6]+DOT_SIZE,self.coords[7]+DOT_SIZE),
                                              fill="white", outline="black", width=3, state="hidden")
        
        canvas.tag_bind(self.diamond,"<Button-1>",self.click)
        canvas.tag_bind(self.diamond,"<B1-Motion>",self.drag)

class Parallelogram:
    def click(self, event):
        #coordinates of the place we click the label at (Point A)
        self.click_x = event.x
        self.click_y = event.y
        print("Click:",self.click_x,self.click_y)
        
        canvas.itemconfig(self.dot1, state="normal")
        canvas.itemconfig(self.dot2, state="normal")
        canvas.itemconfig(self.dot3, state="normal")
        canvas.itemconfig(self.dot4, state="normal")

    def resize(self, event):
        pointer_x = event.x
        pointer_y = event.y
        print("Pointer:", pointer_x, pointer_y)

        # Here you would compute the new size based on the pointer position
        # relative to the original dot position. Hopefully there is some easy
        # way to do that using the canvas. If not I would probably try and save
        # some values in each shape class you have to make it easier.

        # Once you know how much to scale the shape you can use canvas.scale
        # to change the size. I wasn't too sure on the args you would want to
        # use here so you might play with that a bit since you are more familiar.
        # canvas.scale(self.parallelogram, 0, 0, r, r)

    def drag(self, event):
        #coordinates of the place we are dragging the widget to (Point B)
        pointer_x=event.x
        pointer_y=event.y
        print("Pointer:",pointer_x,pointer_y)

        #distance between Point A and Point B for x and y
        x = pointer_x - self.click_x
        print("X: {}-{} = {}".format(pointer_x,self.click_x,x))
        y = pointer_y - self.click_y
        print("Y: {}-{} = {}".format(pointer_y,self.click_y,y))
        
        canvas.move(self.parallelogram, x, y)
        canvas.move(self.dot1, x, y)
        canvas.move(self.dot2, x, y)
        canvas.move(self.dot3, x, y)
        canvas.move(self.dot4, x, y)
        
        self.click_x = pointer_x
        self.click_y = pointer_y
    
    def __init__(self, color):
        self.parallelogram = canvas.create_polygon(
            (10 + 45, (RECTANGLE_SIZE[1] + 20 + CIRCLE_SIZE[1] + 20 + DIAMOND_SIZE[1] + 20)),
            (10, (RECTANGLE_SIZE[1] + 20 + CIRCLE_SIZE[1] + 20 + DIAMOND_SIZE[1] + 20) + PARALLELOGRAM_SIZE[1]),
            (10 + PARALLELOGRAM_SIZE[0] - 45,
             (RECTANGLE_SIZE[1] + 20 + CIRCLE_SIZE[1] + 20 + DIAMOND_SIZE[1] + 20) + PARALLELOGRAM_SIZE[1]),
            (10 + PARALLELOGRAM_SIZE[0], (RECTANGLE_SIZE[1] + 20 + CIRCLE_SIZE[1] + 20 + DIAMOND_SIZE[1] + 20)),
            fill=color, width=4, outline="black")
        self.coords = canvas.coords(self.parallelogram)
        
        self.dot1 = canvas.create_oval((self.coords[0]-DOT_SIZE,self.coords[1]-DOT_SIZE),
                                              (self.coords[0]+DOT_SIZE,self.coords[1]+DOT_SIZE),
                                              fill="white", outline="black", width=3, state="hidden")
        self.dot2 = canvas.create_oval((self.coords[2]-DOT_SIZE,self.coords[3]-DOT_SIZE),
                                              (self.coords[2]+DOT_SIZE,self.coords[3]+DOT_SIZE),
                                              fill="white", outline="black", width=3, state="hidden")
        self.dot3 = canvas.create_oval((self.coords[4]-DOT_SIZE,self.coords[5]-DOT_SIZE),
                                              (self.coords[4]+DOT_SIZE,self.coords[5]+DOT_SIZE),
                                              fill="white", outline="black", width=3, state="hidden")
        self.dot4 = canvas.create_oval((self.coords[6]-DOT_SIZE,self.coords[7]-DOT_SIZE),
                                              (self.coords[6]+DOT_SIZE,self.coords[7]+DOT_SIZE),
                                              fill="white", outline="black", width=3, state="hidden")
        
        canvas.tag_bind(self.parallelogram,"<Button-1>",self.click)
        canvas.tag_bind(self.parallelogram,"<B1-Motion>",self.drag)

        # Bind events to the dots... I used motion, but you might use something else.
        # I assumed it would be similar to "drag" above
        canvas.tag_bind(self.dot1, '<B1-Motion>', self.resize)
        canvas.tag_bind(self.dot2, '<B1-Motion>', self.resize)
        canvas.tag_bind(self.dot3, '<B1-Motion>', self.resize)
        canvas.tag_bind(self.dot4, '<B1-Motion>', self.resize)

class Arrow:
    def click(self, event):
        #coordinates of the place we click the label at (Point A)
        self.click_x = event.x
        self.click_y = event.y
        print("Click:",self.click_x,self.click_y)
        
        canvas.itemconfig(self.dot1, state="normal")
        canvas.itemconfig(self.dot2, state="normal")

    def drag(self, event):
        #coordinates of the place we are dragging the widget to (Point B)
        pointer_x=event.x
        pointer_y=event.y
        print("Pointer:",pointer_x,pointer_y)
        
        #distance between Point A and Point B for x and y
        x = pointer_x - self.click_x
        print("X: {}-{} = {}".format(pointer_x,self.click_x,x))
        y = pointer_y - self.click_y
        print("Y: {}-{} = {}".format(pointer_y,self.click_y,y))
        
        canvas.move(self.arrow, x, y)
        canvas.move(self.dot1, x, y)
        canvas.move(self.dot2, x, y)
        
        self.click_x = pointer_x
        self.click_y = pointer_y
    
    def __init__(self, color):
        self.arrow = canvas.create_line((10, (RECTANGLE_SIZE[1]+20+CIRCLE_SIZE[1]+20+DIAMOND_SIZE[1]+20+(PARALLELOGRAM_SIZE[1]*1.5))),
                                             (ARROW_SIZE+10, (RECTANGLE_SIZE[1]+20+CIRCLE_SIZE[1]+20+DIAMOND_SIZE[1]+20+(PARALLELOGRAM_SIZE[1]*1.5))),
                                             fill=color, width=20, arrow="last", arrowshape=(30,24,9))
        self.coords = canvas.coords(self.arrow)
        
        self.dot1 = canvas.create_oval((self.coords[0]-DOT_SIZE,self.coords[1]-DOT_SIZE),
                                              (self.coords[0]+DOT_SIZE,self.coords[1]+DOT_SIZE),
                                              fill="white", outline="black", width=3,state="hidden")
        self.dot2 = canvas.create_oval((self.coords[2]-DOT_SIZE,self.coords[3]-DOT_SIZE),
                                              (self.coords[2]+DOT_SIZE,self.coords[3]+DOT_SIZE),
                                              fill="white", outline="black", width=3, state="hidden")
         
        canvas.tag_bind(self.arrow,"<Button-1>",self.click)
        canvas.tag_bind(self.arrow,"<B1-Motion>",self.drag)
        
        
        

#For each object, there is a base object that creates a new canvas item when it is clicked
#The math for where it is placed is the same as the __init__ variables above
#when it is clicked, is creates another circle with the color from the constant at the top

base_oval = canvas.create_oval(10,10,10+CIRCLE_SIZE[0],
                               10+CIRCLE_SIZE[1],
                               fill="#440044", width=4, outline="black")
canvas.tag_bind(base_oval,"<Button-1>",lambda self: Circle(COLOR))

base_rectangle = canvas.create_rectangle(10,(CIRCLE_SIZE[1]+20),
                                        10+RECTANGLE_SIZE[0],(CIRCLE_SIZE[1]+20)+RECTANGLE_SIZE[1],
                                        fill="#440044", width=4, outline="black")
canvas.tag_bind(base_rectangle,"<Button-1>",lambda self: Rectangle(COLOR))

base_diamond = canvas.create_polygon((10+ (DIAMOND_SIZE[0] / 2), (RECTANGLE_SIZE[1]+20+CIRCLE_SIZE[1]+20)),
                                             (10, (RECTANGLE_SIZE[1]+20+CIRCLE_SIZE[1]+20) + (DIAMOND_SIZE[1] / 2)),
                                             (10+ (DIAMOND_SIZE[0] / 2), (RECTANGLE_SIZE[1]+20+CIRCLE_SIZE[1]+20)  + DIAMOND_SIZE[1]),
                                             (10+ DIAMOND_SIZE[0], (RECTANGLE_SIZE[1]+20+CIRCLE_SIZE[1]+20) + (DIAMOND_SIZE[1] / 2)),
                                             fill="#440044", width=4, outline="black")
canvas.tag_bind(base_diamond,"<Button-1>",lambda self: Diamond(COLOR))

base_parallelogram = canvas.create_polygon((10+45, (RECTANGLE_SIZE[1]+20+CIRCLE_SIZE[1]+20+DIAMOND_SIZE[1]+20)),
                                             (10, (RECTANGLE_SIZE[1]+20+CIRCLE_SIZE[1]+20+DIAMOND_SIZE[1]+20)+PARALLELOGRAM_SIZE[1]),
                                             (10+PARALLELOGRAM_SIZE[0]-45, (RECTANGLE_SIZE[1]+20+CIRCLE_SIZE[1]+20+DIAMOND_SIZE[1]+20)+PARALLELOGRAM_SIZE[1]),
                                             (10+PARALLELOGRAM_SIZE[0], (RECTANGLE_SIZE[1]+20+CIRCLE_SIZE[1]+20+DIAMOND_SIZE[1]+20)),
                                             fill="#440044", width=4, outline="black")
canvas.tag_bind(base_parallelogram,"<Button-1>",lambda self: Parallelogram(COLOR))

base_arrow = canvas.create_line((10, (RECTANGLE_SIZE[1]+20+CIRCLE_SIZE[1]+20+DIAMOND_SIZE[1]+20+(PARALLELOGRAM_SIZE[1]*1.5))),
                                             (ARROW_SIZE+10, (RECTANGLE_SIZE[1]+20+CIRCLE_SIZE[1]+20+DIAMOND_SIZE[1]+20+(PARALLELOGRAM_SIZE[1]*1.5))),
                                             fill="#440044", width=20, arrow="last", arrowshape=(30,24,9))
canvas.tag_bind(base_arrow,"<Button-1>",lambda self: Arrow(COLOR))


window.mainloop()


#I have no idea what tagbind i can use to hide them since "<FocusOut>" shows an error as a bad bind
#Maybe i need to use a different method or another library to hide them, but I do not know what it would be
