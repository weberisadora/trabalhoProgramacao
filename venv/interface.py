from tkinter import *
from banco import *

class interface():

    def __init__(self):
        self.main()

    def main(self):
        janela = Tk()
        janela.geometry("900x700")
        janela.title("Agenda")
        cor = StringVar(janela)
        cor.set("white")
        l = Label(background=cor.get())
        l.pack(fill='both', expand=True)

        lb = Label(janela, text="AGENDA", fg="magenta", font=("Verdana", 16, "bold"), bg="white").place(x=400, y=10)

        # bd = Banco()
        # bd.insere("segunda","Matemática","9:30")

        janela.mainloop()


interface()