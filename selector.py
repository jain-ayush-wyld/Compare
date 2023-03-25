from tkinter  import *
from tkinter import filedialog
from finals import compy
from tkinter import messagebox
#root =Tk()
#root.withdraw()
def sub1():
    global file_path1
    file_path1= filedialog.askopenfilename()
    print(file_path1)
    messagebox.showinfo('msg',"FIle Uploaded")
def sub2():
    global file_path2
    file_path2= filedialog.askopenfilename()
    print(file_path2)
    messagebox.showinfo('msg',"FIle Uploaded")
def compy1():
   global  file_path1,file_path2
   compy(file_path1,file_path2)
def quit3():
    root.destroy()
root=Tk()
root.title("compare")
root.minsize(width=400,height=300)
root.geometry("500x400")
same=True
canvas = Canvas(width=600, height=500)
canvas.pack(expand=YES, fill=BOTH)
headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \n COMPARE ", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

labelFrame = Frame(root,bg='grey')
labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
 
lb3 = Label(labelFrame,text="OLD FILE", bg='black', fg='white')
lb3.place(relx=0.15,rely=0.3)

btn2 = Button(labelFrame,text="choose file",bg='#d1ccc0', fg='black', command=sub1)
btn2.place(relx=0.33,rely=0.3, relwidth=0.45,relheight=0.1)

lb4 = Label(labelFrame,text="NEW FILE", bg='black', fg='white')
lb4.place(relx=0.15,rely=0.45)

btn1 = Button(labelFrame,text="choose file",bg='#d1ccc0', fg='black', command=sub2)
btn1.place(relx=0.33,rely=0.45, relwidth=0.45,relheight=0.1)

comp=Button(labelFrame,text="Compare",bg='#d1ccc0',fg='black',command=compy1)
comp.place(relx=.25,rely=0.9,relwidth=0.20,relheight=0.08)
QuitBtn=Button(labelFrame,text="QUIT",bg='#d1ccc0', fg='black',command=quit3)
QuitBtn.place(relx=0.5,rely=0.9, relwidth=0.18,relheight=0.08)



