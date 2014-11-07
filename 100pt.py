#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in colision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="blue")
player = drawpad.create_rectangle(240,240,260,260, fill="pink")
def animate():
    global direction
    # Get the x and y co-ordinates of the circle
    x1, y1, x2, y2 = drawpad.coords(target)
    if x2 > drawpad.winfo_width(): 
        direction = - 10
    elif x1 < 0:
        direction = 10
    #Move our oval object by the value of direction
    drawpad.move(target,direction,0)
    # Wait for 1 millisecond, then recursively call our animate function
    drawpad.after(5, animate)



class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="left", background= "green")
		self.button1.grid(row=1,column=0)
					
		# "Bind" an action to the first button												
		self.button1.bind("<Button-1>", self.button1Click)
		self.button2 = Button(self.myContainer1)
	        self.button2.configure(text="down", background= "green")
	        self.button2.grid(row=2,column=1)
	        self.button2.bind("<Button-1>", self.button2Click)
       	        self.button4 = Button(self.myContainer1)
	        self.button4.configure(text="right", background= "green")
	        self.button4.grid(row=1,column=2)
	        self.button4.bind("<Button-1>", self.button4Click)
      	        self.button5 = Button(self.myContainer1)
	        self.button5.configure(text="          ", background= "green")
	        self.button5.grid(row=1,column=1)
	        self.up = Button(self.myContainer1)
       	        self.up.configure(text="  up  ", background= "green")
                self.up.grid(row=0,column=1)
       	    # Bind an event to the first button
       	        self.up.bind("<Button-1>", self.upClicked)
		  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		

		
	def button1Click(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
		global oval
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
		# Get the coords of our target
                drawpad.move(player, -20, 0)

		# Ensure that we are doing our collision detection
		# After we move our object!
                didWeHit = self.collisionDetect()
                if(didWeHit == True):
                    # We made contact! Stop our animation!
                    print "Do something"
	# Use a function to do our collision detection
	# This way we only have to write it once, and call it from
	# every button click function.
	def collisionDetect(self):
                global player
                global target
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
                tx1,ty1,tx2,ty2 = drawpad.coords(target) 
                if (tx1 <= x1 and tx2 >= x2) and (ty1 <= y1 and ty2 >= y2):
                    drawpad.itemconfig(target, fill="pink")
                    return True

                # Do your if statement - remember to return True if successful!
        def button2Click(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,20)
	   
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
	   
	def button4Click(self, event):   
	   global oval
	   global player
	   x1,y1,x2,y2 = drawpad.coords(player)
           global player
           x1, y1, x2, y2 = drawpad.coords(player)
           if (x1 > 0 and x2 < 500):
               drawpad.move(player, 20, 0)
           else:
               print ""
		                
	    
		
myapp = MyApp(root)
animate()
root.mainloop()