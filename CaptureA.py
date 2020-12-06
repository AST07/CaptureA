'''
Idea for a personal utility software 05-12-2020
Screenshot
'''

from tkinter import *
from tkinter import ttk,filedialog,messagebox
from datetime import datetime
import os
from PIL import Image,ImageTk,ImageGrab
from threading import Thread

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def launch_button_change(opt):
	global launch_button,cap,inst_label
	options=[['Launch','RoyalBlue2','launch',''],['Close','red','lambda:on_close()',inst]]
	launch_button.configure(text=options[opt][0],bg=options[opt][1],command=eval(options[opt][2]))
	inst_label.config(text=options[opt][3])

def capture(loc):
	def save():
		image.save(os.path.join(loc,f'Capture {"{:%d-%m-%Y %H_%M_%S}".format(datetime.now())}.png'))
	global cap,transp
	cap.attributes('-alpha',0.0)
	image=ImageGrab.grab()
	cap.attributes('-alpha',transp.get())
	Thread(target=save).start()

def on_close():
	global cap
	cap.destroy()
	launch_button_change(0)

def launch():
	global save_loc,cap,transp
	if save_loc.get():
		launch_button_change(1)
		cap=Toplevel(root)
		cap.title('')
		if transp.get()=='':
			transp=0.1
		cap.attributes('-alpha',transp.get())
		cap.overrideredirect(True)
		cap.attributes('-topmost', True)
		cap.protocol("WM_DELETE_WINDOW",on_close)
		click=Button(cap,image=logo,command=lambda:capture(save_loc.get()))
		click.pack(ipadx=0,ipady=0)
		screen_width=root.winfo_screenwidth()
		screen_height=root.winfo_screenheight()
		x=screen_width-click.winfo_reqwidth()
		y=screen_height-click.winfo_reqheight()
		cap.geometry('%dx%d+%d+%d'%(click.winfo_reqwidth(),click.winfo_reqheight(),x,y))
	else:
		messagebox.showerror('Error','Save Location not provided')

def getSaveLocation():
	global save_loc
	loc=filedialog.askdirectory()
	if loc!='':
		save_loc.set(loc)

#GUI
root=Tk()
root.title('CaptureA')
root.minsize(300,400)
root.resizable(False,False)
root.iconphoto(False,PhotoImage(file=resource_path('CaptureA_logo.png')))
root.configure(bg='grey10')

logo=Image.open(resource_path('CaptureA_logo.png'))
logo_disp=logo.resize((100, 100), Image.ANTIALIAS)
logo_disp=ImageTk.PhotoImage(logo_disp)
logo=logo.resize((50, 50), Image.ANTIALIAS)
logo=ImageTk.PhotoImage(logo)

head=Label(root,text='CaptureA',bg='grey10',fg='white',font=('',20)).pack(padx=10,pady=10)

cpyrt_label=Label(root,text='Copyright © 2020 Aditya Singh Tejas',bg='grey35',fg='white')
cpyrt_label.pack(side='bottom',fill='x')
launch_button=Button(root,fg='white',font=('Sans',15))
launch_button.pack(side='bottom',padx=10,pady=10,fill='x')
inst='Click the botton at the bottom of your screen to capture screenshot'
inst_label=Label(root,bg='grey10',fg='white')
inst_label.pack(fill='x',side='bottom')
launch_button_change(0)
logo_label=Label(root,image=logo_disp,bg='grey10')
logo_label.pack(fill='both',side='bottom',pady=20)


label_frame=Frame(root,bg='grey10')
label_frame.pack(side='left',fill='both',padx=10)
disp_frame=Frame(root,bg='grey10')
disp_frame.pack(side='left',fill='both')
act_frame=Frame(root,bg='grey10')
act_frame.pack(side='right',fill='both',padx=10)

save_label=Label(label_frame,text='Save Location',bg='grey10',fg='white',font=('Helvetica',12)).pack(side='top',pady=10)
save_loc=StringVar()
loc_entry=Entry(disp_frame,textvariable=save_loc,bg='grey25',fg='white',font=('Helvetica',12),relief='flat',insertbackground='white')
loc_entry.pack(side='top',pady=10,fill='x')
browse_save_button=Button(act_frame,text='Browse',command=getSaveLocation,bg='black',fg='white',font=('Helvetica',10),relief='flat')
browse_save_button.pack(side='top',pady=8,fill='x')

transp_label=Label(label_frame,text='Transparency',bg='grey10',fg='white',font=('Helvetica',12)).pack(side='top',pady=(8,10))
transp=StringVar()
loc_entry=Entry(disp_frame,textvariable=transp,bg='grey25',fg='white',font=('Helvetica',12),relief='flat',insertbackground='white')
transp.set('0.1')
loc_entry.pack(side='top',pady=10,fill='x')
transpsc_label=Label(act_frame,text='0 - 1',bg='grey10',fg='white',font=('Helvetica',12)).pack(side='top',pady=(8,10))

root.mainloop()