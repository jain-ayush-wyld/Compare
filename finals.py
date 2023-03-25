from tkinter import *
#def strike(text):
#   return ''.join([u'\u0336{}'.format(c) for c in text])
def compy(file_path11,file_path22):

    root =Tk()
    root.title("compare it ")
    width1= root.winfo_screenwidth()   
    height1= root.winfo_screenheight()   
    root.geometry("%dx%d" % (width1, height1))
    root.state('zoomed')
    headingFrame1 = Frame(root,bg="#FFBB00",bd=2)
    headingFrame1.place(relx=0.15,rely=0.0,relwidth=0.15,relheight=0.04)
    headingLabel = Label(headingFrame1, text="OLD FILE ", bg='black', fg='white', font=('Courier New',7))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    headingFrame2 = Frame(root,bg="#FFBB00",bd=2)
    headingFrame2.place(relx=0.65,rely=0.0,relwidth=0.15,relheight=0.04)
    headingLabe2 = Label(headingFrame2, text="NEW FILE ", bg='black', fg='white', font=('Courier New',7))
    headingLabe2.place(relx=0,rely=0, relwidth=1, relheight=1)

    #frame
    my_frame=Frame(root)
    my_frame.pack(pady=30)

    def multiple_yview(*args):
        text1.yview(*args)
        text2.yview(*args)
    def multiple_xview(*args):
        text1.xview(*args)
        text2.xview(*args)
        

    #create our scrollbar
    text1_scroll = Scrollbar(my_frame)
    text1_scroll.pack(side=RIGHT,fill=Y)
    text2_scroll=Scrollbar(my_frame, orient = HORIZONTAL)
    text2_scroll.pack(side=BOTTOM,fill=X)

    #create two text boxes
    text1=Text(my_frame,width=60,height=50,font=("Courier New",14),yscrollcommand=text1_scroll.set,xscrollcommand=text2_scroll.set,wrap= "none")
    text1.pack(side=RIGHT,padx=5)
    text2=Text(my_frame,width=60,height=50,font=("Courier New",14),yscrollcommand=text1_scroll.set,xscrollcommand=text2_scroll.set,wrap= "none")
    text2.pack(side=LEFT)
    text1_scroll.config(command=multiple_yview)
    text2_scroll.config(command=multiple_xview)



    f1=open(file_path11,"r")
    f2=open(file_path22,"r")
    i=0;j=0
    lis1=f1.readlines()
    lis2=f2.readlines()
    lis3=lis1.copy()
    lis4=lis2.copy()
    while True:
        if(lis3[i] in lis4):
            
            posi=lis4.index(lis3[i])
            for k in range (0,posi):
                #perfect
                text1.insert(END,lis4[0].upper())
                lis4.remove(lis4[0])
                #print('')
                text2.insert(END,'\n')
            text1.insert(END,lis4[0])
            lis4.remove(lis4[0])
            #print("this it is  ",lis4)
            #print(lis3[i],end='')
            text2.insert(END,lis3[i])
            i+=1
        #elif lis3[i]=='\n':
           # text2.insert(END,'\n')
            #i+=1;
        else:
            l=0
            tup1=lis3[i].split()
            tup2=lis4[l].split()
            c=0
            for l in range(0,len(lis4)):
                for st1 in tup1:
                    tup2=lis4[l].split()
                    for st2 in tup2:
                        if(st1.lower()==st2.lower()):
                            c=1
                            num1=l;
                        if(c==1):
                            break
                    if(c==1):
                        break
                if c==1:
                    break
            if (c==1):
                for a in range(0,l):
                    text1.insert(END,lis4[0].upper())
                    lis4.remove(lis4[0])
                    #print('')
                    text2.insert(END,'\n')
                lis4.remove(lis4[0])
                len1=0
                len2=0
                lisi=[]
                print(tup1)
                print(tup2)
                for s1 in range(0,len(tup1)):
                    for s2 in range(0,len(tup2)):
                        if (tup1[s1].lower() in tup2[s2].lower()):
                            #print(st2,end='')
                            lisi.append(tup1[s1].lower())
                            text2.insert(END,tup1[s1].lower()+" ")
                            #text1.insert(END,st2)
                            len1+=1
                            len2+=1
                           
                    else:
                        #print(st1.upper(),end=' ')
                        text2.insert(END,tup1[s1].upper()+" ")
                        #text1.insert(END,st2.upper()+" ")
                        len1+=1
                        len2+=1
                            
                        
                text2.insert(END,"\n")
                #print(lisi)
                for st2 in tup2:
                    if st2.lower() in lisi:
                        text1.insert(END,st2+" ")
                        continue
                    else:
                        text1.insert(END,st2.upper()+" ")
                            
                text1.insert(END,"\n")    
                        #if (len2==len(tup2)):
                            #text1.insert(END,"\n")
            else:
                #print(lis3[i].upper(),end='')
                text1.insert(END,"\n")
                text2.insert(END,lis3[i].upper())
            i+=1
        
            
        if i==len(lis3):
            break
    for i in lis4:
            text1.insert(END,i.upper())
            text2.insert(END,'\n')
            
        

