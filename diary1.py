import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import Text
from functools import partial

def exit():
	window1.destroy()

def window_config():
	window1 = tkinter.Tk()
	window1.geometry("400x400")
	window1.title("MENU")
	window1.configure(bg="pink")
	return window1
	
def main():
	window1 = window_config()
	return window1

def color_config(widget, color, event):	#for the buttons(when the cursor hovers)
    widget.configure(foreground=color)	#http://stackoverflow.com/questions/10239292/changing-text-color-when-hovering-over-text-with-tkinter


def newEntry():
	def menu():
		f2.pack_forget()
		mframe.pack()
	def submit():
		date = dateTbox.get()
		topic = topicTbox.get()
		story = storyTbox.get("1.0", END)	#gets the input from line 1, index 0 'til the end of the box
		fileHandle = open("diary.txt", "r")
		for line in fileHandle:
			if date == line[0:8]:
				messagebox.showinfo("Date already taken", "This will be added to your existing entry")
		fileHandle.close()
		if date == "" or topic == "" or story =="":
			messagebox.showinfo("Try Again", "Please fill up the boxes.")
		else:
			if date != "" and topic != "" and story != "":
				fileHandle = open("diary.txt", "a")
				topic2 = ""
				story2 = ""
				for i in topic:
					if i == "a":
						topic2 += "!"
					elif i == "e":
						topic2 += "@"
					elif i == "i":
						topic2 += "#"
					elif i == "o":
						topic2 += "$"
					elif i == "u":
						topic2 += "%"
					else:
						topic2 += i
				for i in story:
					if i == "a":
						story2 += "!"
					elif i == "e":
						story2 += "@"
					elif i == "i":
						story2 += "#"
					elif i == "o":
						story2 += "$"
					elif i == "u":
						story2 += "%"
					else:
						story2 += i
				value = topic2 + "^" + story2
				fileHandle.write(date + "&")
				fileHandle.write(value)
				fileHandle.close()			
				print("An entry has been added", date, topic)		
				messagebox.showinfo("Success.", "You have added an entry.")
				f2.pack_forget()
				mframe.pack()
	window1.title("New Entry")
	mframe.pack_forget()
	f2 = Frame(window1, bg="pink", padx = 25, pady = 25)
	f2.pack()
	date = tkinter.Label(f2, text="Date", bg="pink")
	ins = tkinter.Label(f2, text="Please follow the format: mm/dd/yy", bg="pink")
	dateTbox = tkinter.Entry(f2)
	topic = tkinter.Label(f2, text="Topic", bg="pink")
	topicTbox = tkinter.Entry(f2)
	story = tkinter.Label(f2, text="Story", bg="pink")
	storyTbox = tkinter.Text(f2, width=40, height=10)
	btn = tkinter.Button(f2, text="SUBMIT", bg="#ff009b", command = submit)
	btn.bind("<Enter>", partial(color_config, btn, "#e6e6fa"))
	btn.bind("<Leave>", partial(color_config, btn, "blue"))
	menu = tkinter.Button(f2, text="MENU", bg="#ff009b", command = menu)
	menu.bind("<Enter>", partial(color_config, menu, "#e6e6fa"))
	menu.bind("<Leave>", partial(color_config, menu, "blue"))
	date.pack()
	ins.pack()
	dateTbox.pack()
	topic.pack()
	topicTbox.pack()
	story.pack()
	storyTbox.pack()
	btn.pack()
	menu.pack()
	
def viewEntry():
	window1.title("View Entry")
	mframe.pack_forget()
	f3 = Frame(window1, bg="skyblue", padx = 0, pady = 0)
	f3.pack()
	def menu():
		f3.pack_forget()
		mframe.pack()
	def submit():
		search = searchTbox.get()
		fileHandle = open("diary.txt", "r")
		for line in fileHandle:
			new = str(line)
			if search == new[0:8]:
				print(line[0:8])
				toprint = ""
				for i in line:
					if i == "!":
						toprint += "a"
					elif i == "@":
						toprint += "e"
					elif i == "#":
						toprint += "i"
					elif i == "$":
						toprint += "o"
					elif i == "%":
						toprint += "u"
					else:
						toprint += i
				newt = toprint.split("^")
				datetopic = newt[0].split("&")
				print(datetopic[0], "\n", datetopic[1])
				print(newt[1])
				etona = datetopic[0]+"\n\n"+datetopic[1]+"\n\n      "+newt[1]
				outputTbox.delete("1.0", END)
				outputTbox.insert(INSERT,etona)
	search = tkinter.Label(f3, text="Enter the date of your entry: ", bg="pink")
	ins = tkinter.Label(f3, text="Please follow the format: mm/dd/yy", bg="pink")
	searchTbox = tkinter.Entry(f3)
	btn = tkinter.Button(f3, text="SEARCH", bg="#ff009b", command = submit)
	btn.bind("<Enter>", partial(color_config, btn, "#e6e6fa"))
	btn.bind("<Leave>", partial(color_config, btn, "blue"))
	output = tkinter.Label(f3, text="This is your entry: ", bg="pink")
	outputTbox = tkinter.Text(f3, width=40, height=15)
	menu = tkinter.Button(f3, text="Back to Menu", bg="#ff009b", command = menu)
	menu.bind("<Enter>", partial(color_config, menu, "#e6e6fa"))
	menu.bind("<Leave>", partial(color_config, menu, "blue"))
	search.pack()
	ins.pack()
	searchTbox.pack()
	btn.pack()
	output.pack()
	outputTbox.pack()
	menu.pack()


def delEntry():
	def menu():
		f4.pack_forget()
		mframe.pack()
	def delete():
		entryo = dateTbox.get()
		fileHandle = open("diary.txt", "r+")
		lines = fileHandle.readlines()
		for line in lines:
			if entryo == line[0:8]:
				global todel
				todel = line
				refileHandle = open("diary.txt", "w")	#clears up the whole file
				refileHandle.close()
		for line in lines:
			if line != todel:
				fileHandle.write('\n' + line)
		fileHandle.close()
		messagebox.showinfo("Success.", "You have deleted an entry.")
		f4.pack_forget()
		mframe.pack()
	def submit():
		entryo = dateTbox.get()
		fileHandle = open("diary.txt", "r")
		for line in fileHandle:
			toprint = ""
			if entryo == line[0:8]:
				for i in line:
					if i == "!":
						toprint += "a"
					elif i == "@":
						toprint += "e"
					elif i == "#":
						toprint += "i"
					elif i == "$":
						toprint += "o"
					elif i == "%":
						toprint += "u"
					else:
						toprint += i
				newt = toprint.split("^")
				datetopic = newt[0].split("&")
				print(datetopic[0], "\n", datetopic[1])
				print(newt[1])
				etona = datetopic[0]+"\n\n"+datetopic[1]+"\n\n      "+newt[1]
				outputTbox.insert(INSERT,etona)
	window1.title("Delete an Entry")
	mframe.pack_forget()
	f4 = Frame(window1, bg="pink", padx = 0, pady = 0)
	f4.pack()
	date = tkinter.Label(f4, text="Enter the date(mm/dd/yy):", bg="skyblue")
	dateTbox = tkinter.Entry(f4)
	datesub = tkinter.Button(f4, text="Search", bg="#ff009b", command = submit)
	datesub.bind("<Enter>", partial(color_config, datesub, "#e6e6fa"))
	datesub.bind("<Leave>", partial(color_config, datesub, "blue"))
	date.pack()
	dateTbox.pack()
	datesub.pack()
	output = tkinter.Label(f4, text="This is your entry: ", bg="skyblue")
	outputTbox = tkinter.Text(f4, width = 40, height = 15)
	output.pack()
	outputTbox.pack()
	dele = tkinter.Button(f4, text="Delete", bg="#ff009b", command = delete)
	dele.bind("<Enter>", partial(color_config, dele, "#e6e6fa"))
	dele.bind("<Leave>", partial(color_config, dele, "blue"))
	dele.pack()
	menu = tkinter.Button(f4, text="MENU", bg="#ff009b", command = menu)
	menu.bind("<Enter>", partial(color_config, menu, "#e6e6fa"))
	menu.bind("<Leave>", partial(color_config, menu, "blue"))
	menu.pack()
	
def changepass():
	window1.title("Change Username and Password")
	mframe.pack_forget()
	f5 = Frame(window1, bg="skyblue", padx = 50, pady = 100)
	f5.pack()
	def submit():
		fileHandle = open("info.txt", "w")
		ofname = nameTbox.get()
		ofpass = passwTbox.get()
		fileHandle.write(ofname + "^")
		fileHandle.write(ofpass)
		fileHandle.close()
		messagebox.showinfo("Success", "You have changed your username and password.")
		exitna()
	def exitna():
		f5.pack_forget()
		mframe.pack()
	def menu():
		f5.pack_forget()
		mframe.pack()
	name = tkinter.Label(f5, bg="pink", text="Set your username: ")
	name.pack()
	nameTbox = tkinter.Entry(f5)
	nameTbox.pack()
	passw = tkinter.Label(f5, bg="pink", text="Set your password: ")
	passwTbox = tkinter.Entry(f5)
	passw.pack()
	passwTbox.pack()
	submit = tkinter.Button(f5, text="CHANGE", bg="#ff009b", command = submit)
	submit.bind("<Enter>", partial(color_config, submit, "#e6e6fa"))
	submit.bind("<Leave>", partial(color_config, submit, "blue"))
	submit.pack()
	menu = tkinter.Button(f5, text="MENU", bg="#ff009b", command = menu)
	menu.bind("<Enter>", partial(color_config, menu, "#e6e6fa"))
	menu.bind("<Leave>", partial(color_config, menu, "blue"))
	menu.pack()
	



window1 = main()
background_image = tkinter.PhotoImage(file="cute.png")
background_label = tkinter.Label(window1, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
mframe = Frame(window1, bg = "pink", padx = 50, pady = 20)
mframe.pack()



btn1 = tkinter.Button(mframe, text="New Entry", bg="#ff009b", pady= 25, padx=50, command = newEntry)
btn1.bind("<Enter>", partial(color_config, btn1, "#e6e6fa"))
btn1.bind("<Leave>", partial(color_config, btn1, "blue"))
btn1.pack()
btn2 = tkinter.Button(mframe, text="View Entry", bg="#ff66c3", pady= 25, padx=50, command= viewEntry)
btn2.bind("<Enter>", partial(color_config, btn2, "#e6e6fa"))
btn2.bind("<Leave>", partial(color_config, btn2, "blue"))
btn2.pack()
btn3 = tkinter.Button(mframe, text="Delete Entry", bg="#ffb2e1", pady=25, padx=50, command = delEntry)
btn3.bind("<Enter>", partial(color_config, btn3, "#e6e6fa"))
btn3.bind("<Leave>", partial(color_config, btn3, "blue"))
btn3.pack()
btn5 = tkinter.Button(mframe, text="Change Password", bg="#ffb2e1", pady=25, padx=50, command = changepass)
btn5.bind("<Enter>", partial(color_config, btn5, "#e6e6fa"))
btn5.bind("<Leave>", partial(color_config, btn5, "blue"))
btn5.pack()
btn4 = tkinter.Button(mframe, text="Exit", bg="#ffe5f5", pady=25, padx=50, command = exit)
btn4.bind("<Enter>", partial(color_config, btn4, "#e6e6fa"))
btn4.bind("<Leave>", partial(color_config, btn4, "blue"))
btn4.pack()
'''
PROJECT: CIARA'S DIARY
CIARA MAE GOTIS
2015-10323
This diary has different features such as adding new entries, viewing entries, deleting entries, changing username and password and exit button.
'''
window1.mainloop()
