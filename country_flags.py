from tkinter import *

root=Tk()
root.title("Planets for nerds")
root.geometry("500x500")
root.configure(background="lightblue")

planet = Label(root, text="Planet: ", bg="lightblue")
name = Label(root,font=("courier",18,"bold"),bg="lightblue")
imag = Label(root, bg="gold2", highlightthickness = 5, borderwidth=2,relief=SOLID)
radius=Label(root,font=("castellar"), bg="lightblue")
info = Label(root,font=("courier",10,"bold"),bg="lightblue",wraplength=500)

def plonet():
    print("I AM A PLONET")

button = Button(root,text="Show Planet Info", command=plonet)
button.place(relx=0.5,rely=0.18,anchor=CENTER)

planet.place(relx=0.2,rely=0.1,anchor=CENTER)
name.place(relx=0.5,rely=0.25,anchor=CENTER)
imag.place(relx=0.5,rely=0.5,anchor=CENTER)
radius.place(relx=0.5,rely=0.8,anchor=CENTER)
info.place(relx=0.5,rely=0.9,anchor=CENTER)

root.mainloop()