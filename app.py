'''
This application is a Zip archiver and a zip decompressor using
Tkinter for GUI
For any doubts, you can email me on:
ivanrj7j@gmail.com
'''

from tkinter import *
from tkinter import filedialog
'''
the above code will import the tkinter module this
will be used for making of GUI
'''
import os
'''
os module will be used for the operating system
functions
'''
import zipfile
'''
This is the most important module, as it is going
to archive and extract the zip file
'''

app_name = 'sZZipper'
# you can change this as you wish 
app_icon = 'icon.ico'
# this is the icon of app, you can change it too 

root = Tk()
# this is the tkinter object 
root.geometry('400x200')
# this defines the dimensions of app 
root.resizable(False, False)
# this prevents user from resizing the window 
root.title(app_name)
# this makes the title of the app as defined
root.iconbitmap(app_icon)

root.mainloop()
# this runs the window 