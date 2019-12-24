from tkinter import *
from krawling import lets_go
from random import randint
def front_signup():
    global email_entry, password_entry,root        
    root = Tk()
    # charin = randint(44,124)
    root.title("OHHHHHHHHKKKKKKKKKKAAAAAYAYAYAYAYAYAYAYAY")
    email_add_label = Label(root, text="Email Address Bitch").grid(row=1, column=0, sticky=W)
    password_label = Label(root, text="Password Bitch").grid(row=2, column=0, sticky=W)
    email_entry = Entry(root)
    email_entry.grid(row=1, column=1, sticky=W,  columnspan=10)
    password_entry = Entry(root, show= chr(randint(44,124)))
    password_entry.grid(row=2, column=1, sticky=W,columnspan=10)
    
    enter_signup_button = Button(root, text="Lets Go Bitch!",command=she_ran).grid(columnspan=2, sticky=W)
    root.mainloop()
def she_ran():
    email_ad = email_entry.get()
    pass_ad = password_entry.get()
    if re.match(r"[\w\.-]+@(login)\.(cuny)\.(edu)$", email_ad):
        lets_go(email_ad,pass_ad,root)
    else:
        rat = Tk()
        two_so = Label(rat, text="you fucking idiot, you forgot @login.cuny.edu").grid(row=1, column=0)
        two_so = Label(rat, text=email_ad, font=("Comic Sans MS",20,'bold')).grid(
            row=2, column=0)
        retch = Button(rat, text="fuck you", command=lambda: rat.destroy()).grid(columnspan=3, sticky=W)
        rat.mainloop()
def end():
    root.destroy()

front_signup()
