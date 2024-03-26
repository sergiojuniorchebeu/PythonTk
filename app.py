from tkinter import *
import webbrowser


def open_chanel():
    webbrowser.open_new("http://youtube.com/@sergiojuniorchebeu5374")
#creation de la première fenetre

window= Tk()
#personaliser la fenetre
window.title("app")
window.geometry("720x480")
window.minsize(480, 360)
window.iconbitmap("logo.ico")
window.config(background='#41B77F')

#creer la frame
frame =Frame(window, bg='#41B77F')

#ajouter un composant texte
label_titre= Label(frame, text="Bienvenue sur l'app", font=("Courrier", 25), bg='#41B77F', fg='White')
label_titre.pack()

label_sous_titre= Label(frame, text="Hey salut à tous c'est sergio", font=("Courrier", 15), bg='#41B77F', fg='White')
label_sous_titre.pack()

#ajouter un premier boutton

yt_button = Button(frame, text="Ouvrir Youtube",font=("Courrier", 25), bg='white', fg='green', command=open_chanel)
yt_button.pack(pady=25, fill=X,)

#ajouter la frame
frame.pack(expand=YES)

#afficher

window.mainloop()