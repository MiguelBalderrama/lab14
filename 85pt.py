#########################################
#
#         85pt - Boundary detection
#
#########################################

# Add a button to move to the right and make them work as you'd expect (repeating lab12)
# This time - make sure that pressing left or right does nothing if you are going
# to hit a "boundary" - i.e. the edge of the screen.

from Tkinter import *
root = Tk()
# Create our drawpad and oval - use variables for our width and height so
# we can access them later on
drawpadwidth = 500
drawpadheight = 500
drawpad = Canvas(root, width=drawpadwidth, height=drawpadheight, background='white')
player = drawpad.create_oval(160,160,320,320, fill="red")

class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="Left", background= "green")
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
		# Make the oval move to the left!
                # "global" makes sure that we can access our oval and our drawpad
                # Add in boundary detection
		global oval
		global drawpad
		global drawpadwidth
		global drawpadheight
		x1,y1,x2,y2 = drawpad.coords(player)
                global player
                x1, y1, x2, y2 = drawpad.coords(player)
                if (x1 > 0 and x2 < 500):
                 	drawpad.move(player, -20, 0)
                else:
                    print ""
                    
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

root.mainloop()