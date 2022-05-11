# from tkinter import *
from tkinter import*
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
import subprocess
from threading import *
root = Tk()
root.title('Untitled-python')
root.geometry('1400x700')
#OUR FUNCTION
def newfile():
    global file
    root.title('Untitled-Notepad')
    file = None
    Textarea.delete(1.0,END)
def openfile():
    global file
    file = askopenfilename(defaultextension='.py',
    filetypes=[('All Files','*.*'),('Python','*.py')])
    if file == '':
        file = None
    else:
        root.title(os.path.basename(file)+'-python')
        Textarea.delete(1.0,END)
        f = open(file,'r')
        Textarea.insert(1.0,f.read())
        f.close()
def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.py',defaultextension='.py',
    filetypes=[('All Files','*.*'),('Python','*.py')])
        if file=='':
            file = None
        else:
            #save as new file
            f = open(file,'w')
            f.write(Textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+'-Python')
            
    else:
        #save the file
            f = open(file,'w')
            f.write(Textarea.get(1.0,END))
            f.close()

def quitapp():
    root.destroy()
def cut():
    Textarea.event_generate(('<<Cut>>'))
def copy():
    Textarea.event_generate(('<<Copy>>'))
def paste():
    Textarea.event_generate(('<<Paste>>'))
def about():
    messagebox.showinfo('IDE','IDE by codevision')
def run():
    
    command = f'{file}'
    process = subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    output,error = process.communicate()
    output_code.insert(1.0, output)
    output_code.insert(1.0, error)
    
def threading(): 
    # Call work function 
    t1=Thread(target=run) 
    t1.start()
#textarea

# Textarea.pack(fill=BOTH,expand=True)
#OUTPUT CODE



# output_code.pack(fill=BOTH)
#paned windwo
paned_1 = PanedWindow(orient=VERTICAL)

paned_1.pack(fill=BOTH,expand=1)


output_code = Text(paned_1,bg='black',fg='yellow')
output_code.insert(1.0,'OUTPUT:\n')
Textarea = Text(paned_1,bg='black',fg='white')
paned_1.add(Textarea)
paned_1.add(output_code)



file = None

#ADDING MENU
menu_bar = Menu()
filemenu = Menu(menu_bar,tearoff=0)
#to open new file
filemenu.add_command(label='New',command=newfile)
#to open already existing file
filemenu.add_command(label='Open',command=openfile)
#to save curent file
filemenu.add_command(label='Save',command=savefile)
# to exit
filemenu.add_command(label='Exit',command=quitapp)
menu_bar.add_cascade(label='File',menu=filemenu)

#Edit Menu
editmenu = Menu(menu_bar,tearoff=0)
editmenu.add_command(label='Cut',command=cut)
editmenu.add_command(label='Copy',command=copy)
editmenu.add_command(label='Paste',command=paste)
menu_bar.add_cascade(label='Edit',menu=editmenu)
#HELP Menu
helpmenu = Menu(menu_bar,tearoff=0)
helpmenu.add_command(label='About Notepad',command=about)
menu_bar.add_cascade(label='Help',menu=helpmenu)
# RUN menu
runmenu = Menu(menu_bar,tearoff=0)
runmenu.add_command(label='Run',command=run)
menu_bar.add_cascade(label='Run',menu=runmenu)

root.config(menu=menu_bar)
#ADDING SCROLLBAR
Scroll = Scrollbar(Textarea)
Scroll.pack(side=RIGHT,fill=BOTH)
Scroll.config(command=Textarea.yview)
Textarea.config(yscrollcommand=Scroll.set)


Scroll_1 = Scrollbar(output_code)
Scroll_1.pack(side=RIGHT,fill=BOTH)
Scroll_1.config(command=output_code.yview)
output_code.config(yscrollcommand=Scroll_1.set)
root.mainloop()