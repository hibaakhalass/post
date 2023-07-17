#1 formation du tk 

from tkinter import *
import csv
from os import path
from tkinter.scrolledtext import ScrolledText

root = Tk()


root['background']='gray'
root.geometry("400x400")
#pour ne pas agrandir la plate forme 
root.resizable(False, False)


''''pour l'enregistrer dans une variable '''

#get : Renvoie le texte actuel de ‘Entry’ sous forme de chaîne.
#get prend les donnees entrez par l'utilisateur et le stock dans titre comme exemple

def enregistrer_formulaire():
    titre = ent1.get()
    description = ent2.get()
    contenu = ent3.get('1.0', END)
    categorie = ent4.get()
    mot_cle = ent5.get()
    
    
    if path.exists('form1.csv') is False:
        with open('form1.csv', 'w', newline='') as fichier_csv:
            
            writer = csv.writer(fichier_csv)
            writer.writerow(["titre", "description", "contenu", "categorie", "mot_cle"])
            # Écrire les données du formulaire dans le fichier CSV par l'ordre suivant :
            writer.writerow([titre, description, contenu, categorie, mot_cle])
    else:
        with open('form1.csv', 'a', newline='') as fichier_csv:
            
            writer = csv.writer(fichier_csv)
            # Écrire les données du formulaire dans le fichier CSV par l'ordre suivant :
            writer.writerow([titre, description, contenu, categorie, mot_cle])
        
        
    # Réinitialiser les champs du formulaire a chaque fois qu'on entre les informations
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(1.0, END)
    ent4.delete(0, END)
    ent5.delete(0, END)
    
    
    
"""le titre de la fenêtre principale"""

root.title("*'*formulaire*'*")


# '''entry ''' : la case 

lb1 = Label(root, text="Title:",width='200',fg='red')
lb1.pack()
lb1['background']='gray'
ent1 = Entry(root,width='300')
ent1.pack()

lb2= Label(root, text="short description:",width='300',fg='red')
lb2.pack()
lb2['background']='gray'
ent2 = Entry(root,width='300')
ent2.pack()

lb3 = Label(root, text="content:",width='300',fg='red')
lb3.pack()
lb3['background']='gray'

ent3 = ScrolledText(root ,wrap=WORD,width = 40, height = 10)
ent3.pack()

lb4 = Label(root, text="category:",width='300',fg='red')
lb4.pack()
lb4['background']='gray'
ent4 = Entry(root,width='300')
ent4.pack()


lb5 = Label(root, text="Mot-clé:",width='300',fg='red')
lb5.pack()
lb5['background']='gray'
ent5 = Entry(root,width='300')
ent5.pack() 

#la boutton appliquer

button = Button(root, text="cliquer ici ", command=enregistrer_formulaire,bg='red')
button.pack(fill='y',side="bottom",padx=15, pady=20)



root.mainloop()

'''
import pandas as pd 
data = pd.read_csv('form1.csv')
print(data)
'''



