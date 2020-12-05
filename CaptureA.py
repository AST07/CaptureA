'''
Idea for a personal utility software 05-12-2020
Screenshot
'''

from tkinter import *
from tkinter import filedialog
import pyscreenshot

def capture():
	image = pyscreenshot.grab()
	image.save()

#GUI
root=Tk()
root.title('Screenshot')
root.attributes('-alpha',0.1)
root.attributes('-toolwindow', True)

root.mainloop()