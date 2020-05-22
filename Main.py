import tkinter
from tkinter import messagebox, Label, Button
import tkinter.font as font
import webbrowser
import requests

top = tkinter.Tk()
top.geometry("500x500")
def openweb():
	webbrowser.open(url, new=new)
	
try:
	response = requests.get("https://github.com/DeepakChakravarthy/Software-Updation/releases/tag/V1.0")
	response.raise_for_status()
	messagebox.showinfo("SoftwareUpdater", "Click Ok to Update")
	new = 1
	url = "https://github.com/DeepakChakravarthy/Software-Updation/releases/tag/V1.0"
	openweb() 

except requests.exceptions.HTTPError as err:
	messagebox.showinfo("SoftwareUpdater","No New Upadates")

myFont = font.Font(size=15)
def openweb():
	try:
		#----ENTER THE LINK TO CheckUpdate ----------#
		response = requests.get("https://github.com/DeepakChakravarthy/Software-Updation/releases/tag/V1.0")
		response.raise_for_status()
	except requests.exceptions.Timeout:
		messagebox.showinfo("SoftwareUpdater","TimeOut..Connection Problem")#TIME INTERNET TOO SLOW
	except requests.exceptions.HTTPError as err:
		messagebox.showinfo("SoftwareUpdater","No New Updates")#NO UPDATE
	except requests.ConnectionError as exception:
		messagebox.showinfo("SoftwareUpdater","Connection Problem Contact the Provider")#CONNECTION
Title = Label(top,text="--SOFTWARE UPDATION PROGRAM---",bg="#754323",fg='white')
Title.pack()
B = Button(top, text ="CheckUpdate",bg='#520b00',fg='white', command = openweb)
name = Label(top,text="V1.0")
Title['font']= myFont
name.pack()
B['font'] = myFont
B.place(x=200,y=250)
top.config(bg="#754323")
top.mainloop()
