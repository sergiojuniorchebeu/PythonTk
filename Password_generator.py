import string
from random import randint, choice
from tkinter import *

def genarate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice (all_chars) for x in range (randint(password_min, password_max)))
    label_entry.delete(0, END)
    label_entry.insert(0, password)



#creer la fenetre
window = Tk()
window.title("Generateur de mot de passe")
window.geometry("720x480")
window.iconbitmap("logo.ico")
window.config(background="#4065A4")

frame = Frame(window, bg='#4065A4')
# creation d'image
width = 300
height = 300
image = PhotoImage(file="la-cyber-securite.png").zoom(10).subsample(30)
canvas = Canvas(frame, width=width, height=height, bg='#4065A4', bd=0, highlightthickness=0)
canvas.create_image(width / 2, height / 2, image=image)
canvas.grid(row=0, column=0, sticky=W)
# sous boite
right_frame = Frame(frame, bg='#4065A4')
# creer le titre
label_title = Label(right_frame, text="Mot de passe", font=("Comic Sans MS", 20), bg='#4065A4', fg="white")
label_title.pack()

# creer le champ
label_entry = Entry(right_frame, font=("Comic Sans MS", 14), bg='white', fg="#4065A4")
label_entry.pack()

# creer le boutton
genarate_button = Button(right_frame, text="Generer", font=("Comic Sans MS", 14), fg='white', bg="#4065A4", command=genarate_password)
genarate_button.pack()

# on place à droite la frame de droite
right_frame.grid(row=0, column=1, sticky=W)
frame.pack(expand=YES)

#creation d'une barre de menu

menu_bar = Menu(window)
#creer un premier menu
file_menu= Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau mot de passe", command=genarate_password)
file_menu.add_command(label="quitter", command=window.quit)
menu_bar.add_cascade(label="fichier", menu=file_menu)
#ajouter menu barre
window.config(menu=menu_bar)

window.mainloop()
