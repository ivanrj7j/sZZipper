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
 

def archive():
    """
    This takes the file as a parameter to function
    This will also archive the folder with a name
    """
    file = filedialog.askdirectory()
    # asks for a directory
    files_in_folder = os.listdir(file)
    # return all the file in folder 
    file_to_save = filedialog.asksaveasfilename(defaultextension='.zip', filetypes=[("Zip Files", "*.zip")])
    # ask a file name to save with 
    with zipfile.ZipFile(file_to_save, 'w', compression=zipfile.ZIP_DEFLATED) as target:
        for file_n in files_in_folder:
            
            file_complete_name = file + '/' + file_n
            # the new file name with directory 
            def append_the_file(file_list, dir_path):
                """
                This function checks if the file is a folder, if it is,
                This will append all the files to a new folder
                """
                for f in file_list:
                    if os.path.isdir(dir_path+'/'+f):
                        append_the_file(os.listdir(dir_path+'/'+f), dir_path+'/'+f)
                    else:
                        target.write(dir_path+'/'+f, str(dir_path+'/'+f).replace(file+'/', ''))
                    '''
                    checks if the file is a folder if the file is a folder,
                    it will list all the files and folder in that folder
                    if there is a folder in the folder, it will do
                    the thing once more
                    '''
            
            if os.path.isdir(file_complete_name):
                append_the_file(os.listdir(file_complete_name), file_complete_name)
                # if the file is a folder, this will execute 
            else:
                target.write(file_complete_name, file_n)
            # saves all the files in directory to a zip file 
            

def extract():
    """
    This will take a zip file as a parameter
    This will extract the folder with a name
    """
    file = filedialog.askopenfilenames(filetypes=[("Zip Files", "*.zip")])[0]
    # gets the file name
    new_folder_name = file.split('/')[-1]
    extension = new_folder_name.split('.')[-1]
    new_folder = new_folder_name.replace('.'+extension, '')
    # gets a new folder name 
    folder = filedialog.askdirectory()
    # asks a folder 
    with zipfile.ZipFile(file, 'r') as target:
        target.extractall(folder + '/' + new_folder)
        # extracts the file 

def zip_file():
    """
    Zips the single file
    """
    file_to_zip = filedialog.askopenfilename()
    file_to_save = filedialog.asksaveasfilename(defaultextension='.zip', filetypes=[("Zip Files", "*.zip")])
    with zipfile.ZipFile(file_to_save, 'w', compression=zipfile.ZIP_DEFLATED) as fl:
        fl.write(file_to_zip, file_to_zip.split('/')[-1])

root = Tk()
# this is the tkinter object 
root.geometry('400x200')
# this defines the dimensions of app 
root.resizable(False, False)
# this prevents user from resizing the window 
root.title(app_name)
# this makes the title of the app as defined
root.iconbitmap(app_icon)
# this changes the icon of the app 

frame = Frame(root)
frame.pack()
# this creates the frame 

archive_btn = Button(frame, text='Archive Folder', command=archive)
archive_btn.pack()
# this pack the archive button to the frame

archive_file_btn = Button(frame, text='Archive File', command=zip_file)
archive_file_btn.pack()

extract_btn = Button(frame, text='Extract File', command=extract)
extract_btn.pack()
# this pack the extract button to frame

root.mainloop()
# this runs the window 