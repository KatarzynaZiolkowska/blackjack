from tkinter import*

root=Tk()

e=Entry(root, width="50")
e.pack()
e.insert(0, "Enter Your Name: ")
    # e.get() w nawiasie to co ta funkcja ma dostać
def myclick():
    hello="Hello " + e.get()
    myLabel=Label(root, text=hello)
    myLabel.pack()

myButton=Button(root, text="click Me", fg="blue", command=myclick)
myButton.pack()

root.mainloop()


def akcja_przycisk_5():
    okno2=Tk()
    # w rozgrywce przycisk wykonaj RUCH (hit, stand, double down) clasy okna?? Zeby po naqciesnięciu przycisku "wykonaj wuch" otwierało się nowe okienko, żeby można było zaznaczyć opcję
    wartosc=IntVar()
    def akcja_przycisk_ruch():
        if wartosc.get()==1 or 2 or 3:
            messagebox.showinfo("Twój ruch", "Właśnie wykonałeś swój ruch.")
        else:
            messagebox.showinfo("Twój ruch", "Żeby wykonać ruch musisz zaznaczyć którąś opcję.")

    # opcje ruchu w Radiobutton
przycisk_11=Radiobutton(okno,text="Hint", variable=wartosc, value=1).pack()
przycisk_12=Radiobutton(okno,text="stand", variable=wartosc, value=2).pack()
przycisk_13=Radiobutton(okno,text="Double down", variable=wartosc, value=3, ).pack()
przycisk_ruch=Button(okno, text="Wykonaj ruch", command=akcja_przycisk_ruch).pack()


przycisk_5=Button(okno, text="Wykonaj ruch", bg="pink", fg="black", font="none 15 bold", command=akcja_przycisk_5).grid(row=3,column=3)
