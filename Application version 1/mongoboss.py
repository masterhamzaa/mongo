#----------Python Mini Projet About Pymongo----------#
#                 Made by Hamza Mimih                #
#                   Dalouji Youssef                  #
#                    Azan Mohammed                   #
#                     DEV203                         #
#----------------------------------------------------#
# database name : pymongohamza
# collections : 
    # pythons : {{"_id": "1","name": "..","course": "..","email": ".."}}
    # users : {"login":...,"password":....}
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import pymongo
from pymongo import MongoClient

import time
import sys

"""___________________________________Loading_____________________________________"""
from time import sleep
def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='>'):
	percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
	filledLength = int(length * iteration // total)
	bar = fill * filledLength + '-' * (length - filledLength)
	print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
	if iteration == total:
		print()

items = list(range(0, 30))
l = len(items)

loadbar(0, l, prefix='Progress:', suffix='Done', length=l)
for i, item in enumerate(items):
	sleep(0.1)
	loadbar(i + 1, l, prefix='Progress:', suffix='Done', length=l)
 

"""_______________________________________MAIN______________________________________________________"""
def main():
    def clear():
        readId.config(state= "normal")
        readId.delete(0, END)
        readName.delete(0, END)
        readCourse.delete(0, END)
        readEmail_id.delete(0, END)
        readId.focus_set()

    def connect():
        """clthamza = MongoClient('localhost', 27017)  #SEPARATE FORMAT"""
        clt = MongoClient('mongodb://localhost:27017/') #URI FORMAT
        return clt;

    def getdata():
        hamza = connect()
        db = hamza.pymongohamza # hamza['test-test'] > ou cas ou une probleme de nom(test-test) de database on utilise le 2eme ecriture
        minidb = db.pythons #collection pythons
        return minidb;

    def erreurs(existe) :
        if existe :
            messagebox.showerror(title="Erreur" , message="Please fill out all the fields !")


    def selector(ecoute): 
        readName.focus_set()
        readId.delete(0, END)
        readName.delete(0, END)
        readCourse.delete(0, END)
        readEmail_id.delete(0, END)
        row_id = listBox.selection()[0]
        select = listBox.set(row_id)
        readId.insert(0,select['reference'])
        readId.config(state= "readonly")
        readName.insert(0,select['name'])
        readCourse.insert(0,select['course'])
        readEmail_id.insert(0,select['email'])
    
    def insertdata():
        readId.config(state= "normal")
        if readName.get() == "" or readCourse.get()=="" or readEmail_id.get() == "" :
            erreurs(True)
        if readName.get() != "" and readCourse.get()!="" and readEmail_id.get() != "" :
            if len(list( getdata().find())) == 0:
                data = {'_id':readId.get(),'name': readName.get(), 'course':readCourse.get(),'email':readEmail_id.get()}
                getdata().insert_one(data)
                for doc in getdata().find():
                    listBox.insert("", "end", values=(doc['_id'],doc['name'], doc['course'], doc['email']))
                    getdata().find().close() #kill the cursor
                    break 
                return
                
                
            if len(list(getdata().find())) != 0 :
                try:
                    exist = False
                    for doc in getdata().find():
                        if readId.get() == doc['_id']:
                            exist =True
                            break
                        else :
                            data = {'_id':readId.get(),'name': readName.get(), 'course':readCourse.get(),'email':readEmail_id.get()}
                            getdata().insert_one(data)
                            break      
                    if exist: 
                        messagebox.showwarning(master=None,title="exists", message="Already Exists !") 
                    if exist == False : 
                        for doc in getdata().find():
                            if readName.get() == doc['name'] and readCourse.get()==doc['course'] and readEmail_id.get() == doc['email'] :
                                listBox.insert("", "end", values=(doc['_id'],doc['name'], doc['course'], doc['email']))
                                getdata().find().close() #kill the cursor
                                break    
                        messagebox.showinfo(title="Success", message="Opertaion done !") 

    
                except Exception as e:
                    messagebox.showerror(title="Exception", message=e) 
    
    def update():
        cltid = readId.get()
        try:
            if readName.get() == "" or readCourse.get()=="" or readEmail_id.get() == "" :
                erreurs(True)
                return  
            getdata().update_one({ "_id": cltid}, {"$set":{'name': readName.get(), 'course':readCourse.get(),'email':readEmail_id.get()}})
            selected = listBox.focus()
            listBox.item(selected,text="",values=(cltid,readName.get(),readCourse.get(),readEmail_id.get()))
            clear()
            #messagebox.showinfo("information", "Record Updateddddd successfully...")
            #clear()
    
        except Exception as e:
            messagebox.showerror(title="Exception", message=e) 
    
    def delete():
        cltid = readId.get()
        results = list(getdata().find())
        if len(results)==0:
                messagebox.showinfo("db", "Collection is empty...")
                return
        try:
            if readName.get() == "" or readCourse.get()=="" or readEmail_id.get() == "" :
                erreurs(True)
                return       
            getdata().delete_one({'_id':cltid})
            index = listBox.selection()[0]
            listBox.delete(index)
            messagebox.showinfo("", "Record Deleted successfully...")
            clear()
           
        except Exception as e:
            
            messagebox.showerror(title="Exception", message=e) 

    def delall():
        try:      
            results = list(getdata().find())
            if len(results)==0:
                 messagebox.showinfo("db", "Collection is empty...")
                 return;
            getdata().delete_many({})
            for i in listBox.get_children():
                listBox.delete(i)
           
            messagebox.showinfo("information", "Record Deleteeeee successfully...")
            readId.config(state= "normal")
            readId.delete(0, END)
            readName.delete(0, END)
            readCourse.delete(0, END)
            readEmail_id.delete(0, END)
            readId.focus_set()
    
        except Exception as e:
    
            messagebox.showerror(title="Exception", message=e) 


        pass

    def select():  
        data = getdata()   
        data = data.find()
        i = 0
        for doc in data:
            i+=1
            listBox.insert("", "end", values=(doc['_id'],doc['name'], doc['course'], doc['email']))
        data.close() #kill the cursor

        

    root = Tk()
    root.configure(background='white')
    root.title('p y m o n g o')
    root.iconbitmap("./icon.ico")
    root.geometry('825x480+230+90')
    root.resizable(False,True) 
    global readId
    global readName
    global readCourse
    global readEmail_id
    
    # c'est comme <br /> 
    heading = Label(root, text="", bg="white")


    # create id label
    idd = Label(root, text="id",bg="white",fg="#1c100b",font=("Ubuntu", 11,'bold'))
    readId = Entry(root,text="")
    # create a Name label
    name = Label(root, text="Name",bg="white",fg="#1c100b",font=("Ubuntu", 11,"bold"))
    readName = Entry(root,text="")
    # create a Course label
    course = Label(root, text="Course",bg="white",fg="#1c100b",font=("Ubuntu", 11,"bold"))
    readCourse = Entry(root,text="")
    # create a Email id label
    email_id = Label(root, text="Email      ",bg="white",fg="#1c100b",font=("Ubuntu", 11,"bold"))
    readEmail_id  = Entry(root,text="")

    #copyright
    c =Label(root, text="copyright©2022 - g o p r o t e a m - hamza-youssef-mohamed",fg="blueviolet", bg="white",font=("Terminal" , 11,"bold"))
    c.place(x=245,y=450)

    heading.grid(row=0, column=2)
    idd.place(x=1,y=20)
    name.grid(row=2, column=0)
    name.place(x=1,y=40)
    course.grid(row=3, column=0)
    course.place(x=1, y=60)
    email_id.place(x=5,y=80)
    email_id.grid(row=6, column=0)


    readId.grid(row=1,column=2,ipadx="100")
    readName.grid(row=2, column=2, ipadx="100")
    readCourse.grid(row=3, column=2, ipadx="100")
    readEmail_id.grid(row=6, column=2, ipadx="100")
        
        
    # create  Buttons and place them into the root window
    inserer = Button(root, text="Submit", font=("Helvitica" , 11,"bold"),fg="white",width=15,cursor="exchange",relief=RAISED,background="#4dff4d", command=insertdata)
    inserer.place(x=30,y=125)

    modifier = Button(root, text="update", font=("Helvitica" , 11,"bold"),fg="white",width=15,cursor="exchange",relief=RAISED,background="#0080ff", command=update)
    modifier.place(x=240,y=125)


    supprimer = Button(root, text="delete", font=("Helvitica" , 11,"bold"),fg="white",background="red",width=15,cursor="exchange",relief=RAISED, command=delete)
    supprimer.place(x=440,y=125)

    deleteall = Button(root, text="delete all", font=("Helvitica" , 11,"bold"),fg="yellow",width=15,cursor="exchange",relief=RAISED,background="blueviolet",activebackground="red",activeforeground="white", command=delall)
    deleteall.place(x=640,y=125)


    global listBox
    cols = ('reference', 'name', 'course','email')
    listBox = ttk.Treeview(root, columns=cols, show='headings')
    ttk.Style(root).configure("Treeview.Heading", height= 8)

    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=10, column=0, columnspan=1)
        listBox.place(x=10, y=200)
    select()
    listBox.bind('<Double-Button-1>',selector)


    root.mainloop()


"""_______________________________________LOGIN______________________________________________________"""
def connect():
    """clthamza = MongoClient('localhost', 27017)  #SEPARATE FORMAT"""
    clt = MongoClient('mongodb://localhost:27017/') #URI FORMAT
    return clt;

def getaccess():
    hamza = connect()
    db = hamza.pymongohamza # hamza['test-test'] > ou cas ou une probleme de nom(test-test) de database on utilise le 2eme ecriture
    minidb = db.users #collection pythons
    return minidb;

def callback() :
    minidb = getaccess()
    login = readLogin.get()
    pwd = readPassword.get()
    try:
        exist = False
        for doc in minidb.find():
            if login == doc['login'] and pwd == doc['password']:
                exist =True
                break
        if exist: 
          

            #animation = "|/-\\"

            #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]

            animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

            for i in range(20):
                time.sleep(0.1)
                sys.stdout.write("\rwaiting.... " + animation[i % len(animation)])
                sys.stdout.flush()
                
            print("\nDone!")
            main()
            
        if exist == False : 
            messagebox.showerror(title="Access denied", message="Not Found") 


    except Exception as e:
        messagebox.showerror(title="Exception", message=e) 

global Login
Login = Tk()
Login.title('Login')
Login.iconbitmap("./icon.ico")
Login.geometry('720x580+260+40')
Login.resizable(False,False) #Login.minsize(720,580) Login.maxsize(720,580)
bg = PhotoImage(file="bg.png")
image = Label(Login,image=bg) 
image.place(x=0,y=0)

labelLogin = Label(Login,text="Login*",font=("Helvetica" , 14))
labelLogin.place(x=315,y=100)
readLogin = Entry(Login,text="",bd=1,width=33)
readLogin.place(x=250,y=155)


#password 
labelPassword = Label(Login,text="Password*",font=("Helvetica" , 14))
labelPassword.place(x=303,y=240)
readPassword = Entry(Login,show="*",bd=1,width=33)
readPassword.place(x=250,y=300)


#submit 
loginButton = Button(Login,text="login",fg="yellow",bg="blueviolet",width=12,bd=1,pady=4,cursor="watch",command=callback)
loginButton.place(x=305,y=380)

#Execution
Login.mainloop() 






