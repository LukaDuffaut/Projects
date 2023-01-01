import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


def Login():
    print("Test")

def CreateObject(x,y,name,theMaster):                       # Creer un objet de type frame avec un titre et des textes
    frame = ctk.CTkFrame(master=theMaster)
    frame.place(x=x, y=y)   

    labelRectangle = ctk.CTkLabel(master=frame,text=name)
    labelRectangle.pack(pady=10,padx=40)

    labelProgramme = ctk.CTkLabel(master=frame,text="Programme")
    labelProgramme.pack(pady=20,padx=10)
    labelProgramme = ctk.CTkLabel(master=frame,text="Programme2")
    labelProgramme.pack(pady=20,padx=10)

def readParametersCration(frame):
    CreateObject(entry.get(),entry.get(),entry3.get(),frame)
    
root = ctk.CTk()
root.geometry("1000x500")

root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=10)
root.rowconfigure(0,weight=1)

################################################################## Création de la 1ère frame

frame = ctk.CTkFrame(master=root)
frame.grid(row=0,column=0,sticky="NSWE",padx=10,pady=10)

label = ctk.CTkLabel(master=frame,text="Login System")
label.pack(pady=12,padx=10)

################################################################## Definition des entrées qui vont permettre la création d'objets

entry = ctk.CTkEntry(master=frame,placeholder_text="Position X")
entry.pack(pady=12,padx=10)

entry2= ctk.CTkEntry(master=frame,placeholder_text="Position Y")
entry2.pack(pady=12,padx=10)

entry3= ctk.CTkEntry(master=frame,placeholder_text="Nom de l'objet")
entry3.pack(pady=12,padx=10)


################################################################## Création de la 2ème frame

frame2 = ctk.CTkFrame(master=root)
frame2.grid(row=0,column=1,sticky="NSWE",padx=10, pady=10)

button = ctk.CTkButton(master=frame,height=2,width=10,text='Créer') # Bouton créer
button.bind('<KeyRelease>',lambda event:readParametersCration(frame2))
button.focus()
button.pack(expand=True)

buttonZoom = ctk.CTkButton(master=frame2,width=30,height=30,text="+").pack(side="top",anchor="ne")      
buttonUnZoom = ctk.CTkButton(master=frame2,width=30,height=30,text="-").pack(side="top",anchor="ne")



root.mainloop()



#Definitions de fonctions


