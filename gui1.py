import tkinter
from functools import partial

def window_config():
	window.geometry("400x400") #size of interface
	window.title("Login!")
	window.configure(background="pink")

def color_config(widget, color, event):	#for the buttons(when the cursor hovers)
    widget.configure(foreground=color)	#http://stackoverflow.com/questions/10239292/changing-text-color-when-hovering-over-text-with-tkinter

def login_click():	
	uname = unameTbox.get()
	pw = pwTbox.get()
	fileHandle = open("info.txt", "r")			#opens the file where the username and password are stored in a line and splitting them into two
	for line in fileHandle:
		official = line.split("^")
	username = official[0]
	password = official[1]
	print("Function call", uname, pw)
	if uname == "" or pw == "":
		pwOut.configure(text="Please fill up the boxes.", bg="white")	
	else:
		if uname == username and pw == password:
			pwOut.configure(text="Login succesful", bg="pink")
			window.destroy()
			import diary1
		else:
			pwOut.configure(text="incorrect input")



window = tkinter.Tk()
window_config()
background_image = tkinter.PhotoImage(file="back.png")				#defining the image and adding a label for the placement of the background image
background_label = tkinter.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

unameLbl = tkinter.Label(window, text="Username", bg="pink")
unameTbox = tkinter.Entry(window)
pwLbl = tkinter.Label(window, text="Password", bg="pink")
pwTbox = tkinter.Entry(window, show="*")
btn = tkinter.Button(window, text="LOG IN", bg="#ff009b", command = login_click)
btn.bind("<Enter>", partial(color_config, btn, "#e6e6fa"))
btn.bind("<Leave>", partial(color_config, btn, "blue"))
unameLbl.pack()
unameTbox.pack()
pwLbl.pack()
pwTbox.pack()
btn.pack()

pwOut = tkinter.Label(window, text="")
pwOut.pack()
'''
PROJECT: CIARA'S DIARY
CIARA MAE GOTIS
2015-10323
This diary has different features such as adding new entries, viewing entries, deleting entries, changing username and password and exit button.
'''
window.mainloop()
