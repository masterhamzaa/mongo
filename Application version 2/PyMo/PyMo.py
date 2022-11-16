#------------------------------------------PyMo:CRUD Desktop App Python Tkinter MongoDB------------------------------------------#
#                                                       Made by Youssef Dalouji                                                  #
#                                                            Hamza Mimih                                                         #
#                                                           Mohammed Azan                                                        #
#                                                Group:DEV203OWFS ISMO TETOUAN MOROCCO                                           #
#--------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------Logiciel PyMo------------------------------------------------
#Import-----------------------------------------------------$$$
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import pymongo
import time
from tkinter import messagebox
#------------------------------------------------------------------
#Configuration Logiciel-----------------------------------------$$$
#------------------------------------------------------------------
Wind=Tk()
Wind.geometry('900x550+240+70')
Wind.resizable(False, False)
Wind.title("PyMo")
Wind.iconbitmap('./Icon/mongopy1.ico')
Wind.config(background='#233DFF')
Photo = ImageTk.PhotoImage(Image.open('Photo_programme/HOME.png'))
Labelx = Label(Wind, image=Photo,bg='#233DFF')
Labelx.place(x=0, y=0)
prog = ttk.Progressbar(Wind, orient=HORIZONTAL, length=100, mode='determinate')
for i in range(10):
    prog['value'] += 10
    Wind.update_idletasks()
    time.sleep(0.4)
#connexion avec mongodb-------------------------------------$$$
try:
    connexion = pymongo.MongoClient("mongodb://localhost:27017/")
    messagebox.showinfo("Connexion","Connecté avec succès!!!")
except:
    messagebox.showwarning("Connexion","Impossible de se connecter à MongoDB")
    Wind.destroy()
Labelx.destroy()
f1 = Frame(Wind, width='450', height='550', bg='#233DFF')
f1.place(x=0, y=0)
f2 = Frame(Wind, width='450', height='550', bg='#233DFF')
f2.place(x=450, y=0)
Photo=ImageTk.PhotoImage(Image.open('Photo_programme/740042.png'))
Labele=Label(f1, image=Photo)
Labele.place(x=-2,y=-2)
Photo1=ImageTk.PhotoImage(Image.open('user/user3.png'))
labl2=Label(f2,image=Photo1,bg='#233DFF')
labl2.place(x=199,y=85)
# Function : Login--->Auhentification-----------------------$$$
#Variable Global Pour Frame Suppression----
global Supper
Supper=""
#------------------------------------------
def Login():
    if(entloginauthen.get()=="" or entpasswordauthen.get()==""):
        messagebox.showinfo("Obligatoire","Les Champs Obligatoire")
    else:
        mydatabase = connexion["GestionUtilisateurs"]
        mycollection = mydatabase["Users"]
        data=mycollection.find_one({"login":f"{entloginauthen.get()}","motpasse":f"{entpasswordauthen.get()}"})
        if(data):
            if (data["role"]=="Admin"):
                Supper=entloginauthen.get()
                f1.destroy()
                f2.destroy()
                nbt = ttk.Notebook(Wind)
                nbt.pack()
                fr1 = Frame(width='900', height='550', bg='green')
                nbt.add(fr1, text='Ajouter')
                fr2 = Frame(width='900', height='550', bg='yellow')
                nbt.add(fr2, text='Afficher')
                fr3 = Frame(width='900', height='550', bg='blue')
                nbt.add(fr3, text='Modifier')
                fr4 = Frame(width='900', height='550', bg='red')
                nbt.add(fr4, text='Supprimer')

                # ------------------------------------------------------------------
                # Frame 1 Ajouter-------------------------------------------------$$$
                # ------------------------------------------------------------------
                def Ajouter():
                    if (
                            entlogin.get() == "" or entname.get() == "" or entpassword.get() == "" or entemail.get() == "" or selectAjou.get() == ""):
                        messagebox.showinfo("Obligatoire", "Les Champs Obligatoire")
                    else:
                        dataimport = mycollection.find_one({"login": f"{entlogin.get()}"})
                        if (dataimport):
                            messagebox.showwarning("Error", "Login deja existe")
                        else:
                            dataimport = mycollection.find_one({"email": f"{entlogin.get()}"})
                            if (dataimport):
                                messagebox.showwarning("Error", "Email deja existe")
                            else:
                                datainsert = {"nom_complet": f"{entname.get()}", "login": f"{entlogin.get()}",
                                              "motpasse": f"{entpassword.get()}", "email": f"{entemail.get()}",
                                              "role": f"{selectAjou.get()}"}
                                mycollection.insert_one(datainsert)
                                messagebox.showinfo("État de l’opération", "Succès")
                                entlogin.delete(0, END)
                                entpassword.delete(0, END)
                                entemail.delete(0, END)
                                entname.delete(0, END)
                                selectAjou.delete(0, END)

                def AnnulerAjouter():
                    entlogin.delete(0, END)
                    entpassword.delete(0, END)
                    entemail.delete(0, END)
                    entname.delete(0, END)
                    selectAjou.delete(0, END)

                # ----->>>#END Function---------------------------$$$
                global imgverfier
                global imgannuler
                imgverfier = ImageTk.PhotoImage(Image.open('logo/Ajouter3.png'))
                imgannuler = ImageTk.PhotoImage(Image.open('logo/annuler.png'))
                lblAFF = Label(fr1, text="Login", bg="green", fg="#fff", font=('Malgun Gothic', 12, 'bold'))
                lblAFF.place(x=280, y=120)
                entlogin = Entry(fr1)
                entlogin.place(x=420, y=122, width=200, height=20)
                lblAFFname = Label(fr1, text="Nom Complet", bg="green", fg="#fff", font=('Malgun Gothic', 12, 'bold'))
                lblAFFname.place(x=280, y=170)
                entname = Entry(fr1)
                entname.place(x=420, y=172, width=200, height=20)
                lblAFF1 = Label(fr1, text="Mot Passe", bg="green", fg="#fff", font=('Malgun Gothic', 12, 'bold'))
                lblAFF1.place(x=280, y=226)
                entpassword = Entry(fr1, show="*")
                entpassword.place(x=420, y=229, width=200, height=20)
                lblAFF2 = Label(fr1, text="Email", bg="green", fg="#fff", font=('Malgun Gothic', 12, 'bold'))
                lblAFF2.place(x=280, y=281)
                entemail = Entry(fr1)
                entemail.place(x=420, y=283, width=200, height=20)
                selectAjou = ttk.Combobox(fr1, width='30')
                lblSelect = Label(fr1, text="Role", bg="green", fg="#fff", font=('Malgun Gothic', 12, 'bold'))
                lblSelect.place(x=280, y=335)
                selectAjou["values"] = ("Admin", "User")
                selectAjou.place(x=420, y=337)
                btnlogin = Button(fr1, image=imgverfier, bg='#009933', activebackground='#009933', command=Ajouter)
                btnlogin.place(x=350, y=391)
                btnann = Button(fr1, image=imgannuler, bg='#ff0000', activebackground='#ff0000', command=AnnulerAjouter)
                btnann.place(x=452, y=391)
                lblsujet = Label(fr1, text="Ajouter", bg="green", fg="#fff", font=('Malgun Gothic', 35, 'bold'))
                lblsujet.place(x=350, y=5)
                # ------------------------------------------------------------------
                # Frame 2 Afficher------------------------------------------------$$$
                # ------------------------------------------------------------------
                lblsujetAFF = Label(fr2, text="Affichage", bg="yellow", fg="#000", font=('Malgun Gothic', 35, 'bold'))
                lblsujetAFF.place(x=330, y=5)
                ScrollY = Scrollbar(fr2, orient="vertical")
                Contenu = Listbox(fr2, width=86, height=18, background="black", fg="yellow", selectbackground="black",
                                  highlightcolor="yellow", font=('Aerial 13'), yscrollcommand=ScrollY.set)
                ScrollY.config(command=Contenu.yview)
                ScrollY.pack(side=RIGHT, fill=Y)
                Contenu.place(x=52, y=150)

                # ----->>>#Function :Affichage Users---------------------------$$$
                def Affichage():
                    Contenu.delete(0, END)
                    dataImportUsers = mycollection.find()
                    for i in dataImportUsers:
                        Contenu.insert(END, f"*ID :----------------{i['_id']}----------------------*")
                        Contenu.insert(END, f"Nom Complet : {i['nom_complet']}")
                        Contenu.insert(END, " ")
                        Contenu.insert(END, f"Login : {i['login']}")
                        Contenu.insert(END, " ")
                        Contenu.insert(END, f"Mot Passe : {i['motpasse']}")
                        Contenu.insert(END, " ")
                        Contenu.insert(END, f"E-mail : {i['email']}")
                        Contenu.insert(END, " ")
                        Contenu.insert(END, f" Role : {i['role']}")
                        Contenu.insert(END, " ")
                        Contenu.insert(END,
                                       "*-----------------------------------------------------------------------------*")
                        Contenu.insert(END, " ")

                # ----->>>#END Function---------------------------$$$
                global imgAfficher
                imgAfficher = ImageTk.PhotoImage(Image.open('logo/Afficher.png'))
                btnAfficher = Button(fr2, image=imgAfficher, bg='#000', activebackground='yellow', command=Affichage)
                btnAfficher.place(x=390, y=100)
                # ------------------------------------------------------------------
                # Frame 3 Modifier------------------------------------------------$$$
                # ------------------------------------------------------------------
                global imgVerfierMod
                global imgrefresh
                global reponse
                reponse = ""
                imgVerfierMod = ImageTk.PhotoImage(Image.open('logo/validier.png'))
                imgrefresh=ImageTk.PhotoImage(Image.open('logo/refresh.png'))
                selectAjouMOD = ttk.Combobox(fr3, width='30', state="readonly")
                lblSelectMOD = Label(fr3, text="Utilisateur", bg="blue", fg="#fff", font=('Malgun Gothic', 12, 'bold'))
                lblSelectMOD.place(x=260, y=238)
                def refreshDataSelectMOD():
                    dataimportLogin = mycollection.find()
                    dataPure = []
                    for j in dataimportLogin:
                        dataPure.append(j["login"])
                    selectAjouMOD["values"] = tuple(dataPure)
                refreshDataSelectMOD()
                selectAjouMOD.place(x=355, y=242)

                # ----->>>#Function :Modifier Users---------------------------$$$
                def Modifier():
                    if (selectAjouMOD.get() == ""):
                        messagebox.showinfo("Obligatoire", "Selection Obligatoire")
                    else:
                        reponse = selectAjouMOD.get()
                        selectAjouMOD.place_forget()
                        lblSelectMOD.place_forget()
                        btnloginMOD.place_forget()
                        lblsujetMOD.place_forget()

                        def Modification():
                            if (
                                    entnamemodplus.get() == "" or entpasswordmodplus.get() == "" or entemailmodplus.get() == "" or selectAjouMODplus.get() == ""):
                                messagebox.showinfo("Obligatoire", "Les Champs Obligatoire")
                            else:
                                verfiction = False
                                emailexist = entemailmodplus.get()
                                dataimport = mycollection.find({"email": f"{entemailmodplus.get()}"})
                                for t in dataimport:
                                    if (t["email"] != emailexist):
                                        messagebox.showwarning("Error", "Email deja existe")
                                    else:
                                        verfiction = True
                                if (verfiction):
                                    data1 = messagebox.askquestion("Preuve", "Es-tu sûr")
                                    if (data1 == "yes"):
                                        dataupdate = {"nom_complet": f"{entnamemodplus.get()}",
                                                      "motpasse": f"{entpasswordmodplus.get()}",
                                                      "email": f"{entemailmodplus.get()}",
                                                      "role": f"{selectAjouMODplus.get()}"}
                                        mycollection.update_one({"login": f"{reponse}"}, {"$set": dataupdate})
                                        messagebox.showinfo("État de l’opération", "Succès")
                                        entloginmodplus.destroy()
                                        entpasswordmodplus.destroy()
                                        entemailmodplus.destroy()
                                        entnamemodplus.destroy()
                                        selectAjouMODplus.destroy()
                                        btnloginmodplus.destroy()
                                        lblsujetmodplus.destroy()
                                        lblMOD.destroy()
                                        lblMODname.destroy()
                                        lblMOD1.destroy()
                                        lblMOD2.destroy()
                                        lblSelectMODplus.destroy()
                                        selectAjouMOD.place(x=355, y=242)
                                        lblSelectMOD.place(x=260, y=238)
                                        btnloginMOD.place(x=575, y=229)
                                        lblsujetMOD.place(x=350, y=90)

                        # ----->>>#END Function---------------------------$$$
                        global imgverfierMOD
                        imgverfierMOD = ImageTk.PhotoImage(Image.open('logo/sync.png'))
                        lblMOD = Label(fr3, text="Login", bg="blue", fg="#fff", font=('Malgun Gothic', 12, 'bold'))
                        lblMOD.place(x=280, y=120)
                        entloginmodplus = Entry(fr3, state="readonly")
                        entloginmodplus.place(x=420, y=122, width=200, height=20)
                        lblMODname = Label(fr3, text="Nom Complet", bg="blue", fg="#fff",
                                           font=('Malgun Gothic', 12, 'bold'))
                        lblMODname.place(x=280, y=170)
                        entnamemodplus = Entry(fr3)
                        entnamemodplus.place(x=420, y=172, width=200, height=20)
                        lblMOD1 = Label(fr3, text="Mot Passe", bg="blue", fg="#fff", font=('Malgun Gothic', 12, 'bold'))
                        lblMOD1.place(x=280, y=226)
                        entpasswordmodplus = Entry(fr3, show="*")
                        entpasswordmodplus.place(x=420, y=229, width=200, height=20)
                        lblMOD2 = Label(fr3, text="Email", bg="blue", fg="#fff", font=('Malgun Gothic', 12, 'bold'))
                        lblMOD2.place(x=280, y=281)
                        entemailmodplus = Entry(fr3)
                        entemailmodplus.place(x=420, y=283, width=200, height=20)
                        selectAjouMODplus = ttk.Combobox(fr3, width='30')
                        lblSelectMODplus = Label(fr3, text="Role", bg="blue", fg="#fff",
                                                 font=('Malgun Gothic', 12, 'bold'))
                        lblSelectMODplus.place(x=280, y=335)
                        selectAjouMODplus["values"] = ("Admin", "User")
                        selectAjouMODplus.place(x=420, y=337)
                        btnloginmodplus = Button(fr3, image=imgverfierMOD, bg='#00c2cb', activebackground='#009933',
                                                 command=Modification)
                        btnloginmodplus.place(x=410, y=391)
                        lblsujetmodplus = Label(fr3, text="Modification", bg="blue", fg="#fff",
                                                font=('Malgun Gothic', 35, 'bold'))
                        lblsujetmodplus.place(x=310, y=5)
                        dataImportInsertMOD = mycollection.find_one({"login": f"{reponse}"})
                        entloginmodplus.insert(0, dataImportInsertMOD["login"])
                        entpasswordmodplus.insert(0, dataImportInsertMOD["motpasse"])
                        entemailmodplus.insert(0, dataImportInsertMOD["email"])
                        entnamemodplus.insert(0, dataImportInsertMOD["nom_complet"])
                        selectAjouMODplus.insert(0, dataImportInsertMOD["role"])

                # ----->>>#END Function---------------------------$$$
                btnloginMOD = Button(fr3, image=imgVerfierMod, bg='#009933', activebackground='#009933',
                                     command=Modifier)
                btnloginMOD.place(x=575, y=229)
                btnrefreshMDO=Button(fr3, image=imgrefresh, bg='#D9D9D9', activebackground='#009933',command=refreshDataSelectMOD)
                btnrefreshMDO.place(x=788, y=15)
                lblsujetMOD = Label(fr3, text="Modifier", bg="blue", fg="#fff", font=('Malgun Gothic', 35, 'bold'))
                lblsujetMOD.place(x=350, y=90)
                # ------------------------------------------------------------------
                # Frame 4 Supprimer-----------------------------------------------$$$
                # ------------------------------------------------------------------
                global imgSupprimer
                imgSupprimer = ImageTk.PhotoImage(Image.open('logo/remv.png'))
                selectAjouSupp = ttk.Combobox(fr4, width='30')
                lblSelectSupp = Label(fr4, text="Utilisateur", bg="red", fg="#fff", font=('Malgun Gothic', 12, 'bold'))
                lblSelectSupp.place(x=260, y=238)
                # ----->>>#Function :Refresh Login---------------------------$$$
                def refreshDataSelectSupp():
                    dataimportLoSupp = mycollection.find()
                    dataPSupp = []
                    for x in dataimportLoSupp:
                        if (x["login"] != Supper):
                            dataPSupp.append(x["login"])
                    selectAjouSupp["values"] = tuple(dataPSupp)
                refreshDataSelectSupp()
                # ----->>>#END Function---------------------------$$$
                # ----->>>#Function :Supprimer Documents---------------------------$$$
                def Supprimer():
                    if (selectAjouSupp.get() == ""):
                        messagebox.showinfo("Obligatoire", "Selection Obligatoire")
                    else:
                        ask = messagebox.askquestion("Preuve", "Es-tu sûr")
                        if (ask == "yes"):
                            mycollection.delete_one({"login": f"{selectAjouSupp.get()}"})
                            messagebox.showinfo("État de l’opération", "Succès")
                            refreshDataSelectSupp()
                            selectAjouSupp.delete(0,END)
                # ----->>>#END Function---------------------------$$$
                selectAjouSupp.place(x=355, y=242)
                btnlogiSupp = Button(fr4, image=imgSupprimer, bg='#ff0000', activebackground='#ff0000',command=Supprimer)
                btnlogiSupp.place(x=575, y=229)
                btnrefreshSupp = Button(fr4, image=imgrefresh, bg='#D9D9D9', activebackground='#009933',
                                       command=refreshDataSelectSupp)
                btnrefreshSupp.place(x=788, y=15)
                lblsujeSupp = Label(fr4, text="Suppression", bg="red", fg="#fff", font=('Malgun Gothic', 35, 'bold'))
                lblsujeSupp.place(x=300, y=90)
            else:
                Loginusers=entloginauthen.get()
                f1.destroy()
                f2.destroy()
                global imgdeconnexion
                imgdeconnexion=ImageTk.PhotoImage(Image.open('logo/deconnexion.png'))
                # ----->>>#Function :Deconnexion---------------------------$$$
                def Deconnexion():
                    Wind.quit()
                # ----->>>#END Function---------------------------$$$
                frameuser=Frame(Wind, width='900', height='550', bg='black')
                frameuser.place(x=0, y=0)
                lbluser=Label(frameuser, text="Welcome", bg="black", fg="#fff", font=('Malgun Gothic', 35, 'bold'))
                lbluser.place(x=340,y=70)
                datausers=mycollection.find_one({"login":f"{Loginusers}"})
                lblusername = Label(frameuser, text=f"{datausers['nom_complet']}", bg="black", fg="#fff", font=('Malgun Gothic', 35, 'bold'))
                lblusername.place(x=290, y=150)
                btndeconnexion=Button(frameuser, image=imgdeconnexion, bg='#ff0000', activebackground='red',command=Deconnexion)
                btndeconnexion.place(x=380,y=250)
        else:
            messagebox.showerror("Invalid","Login ou Mot Passe Incorrect")
#------------------------------------------------------------------
#Frame f2 Authntifiction-----------------------------------------------$$$
#------------------------------------------------------------------
def Annuler():
    entloginauthen.delete(0,END)
    entpasswordauthen.delete(0,END)
global imglogin
global imgannuler
imglogin=ImageTk.PhotoImage(Image.open('logo/login.png'))
imgannuler=ImageTk.PhotoImage(Image.open('logo/annuler.png'))
lbl3=Label(f2,text="Login",bg="#233DFF",fg="#fff",font=('Malgun Gothic',12,'bold'))
lbl3.place(x=40,y=200)
entloginauthen=Entry(f2)
entloginauthen.place(x=140,y=204,width=200,height=20)
lbl4 = Label(f2, text="Mot Passe", bg="#233DFF", fg="#fff", font=('Malgun Gothic', 12, 'bold'))
lbl4.place(x=40, y=276)
entpasswordauthen = Entry(f2,show="*")
entpasswordauthen.place(x=140, y=280,width=200,height=20)
btnlogin=Button(f2,image=imglogin,bg='#009933',activebackground='#009933',command=Login)
btnlogin.place(x=140,y=350)
btnann = Button(f2,image=imgannuler, bg='#ff0000',activebackground='#ff0000',command=Annuler)
btnann.place(x=245, y=350)
#Executer Boucle Logiciel Loresque Executer Logiciel-------------$$$
Wind.mainloop()
