from tkinter import *
import banco

class interface():

    def __init__(self):
        self.main()

    def main(self):
        bd = banco.Banco()
        janela = Tk()
        janela.geometry("1024x500")
        janela.title("Agenda")
        cor = StringVar(janela)
        cor.set("white")
        l = Label(background=cor.get())
        l.pack(fill='both', expand=True)

        lb = Label(janela, text="AGENDA", fg="magenta", font=("Verdana", 16, "bold"), bg="white").place(x=450, y=10)

        lb = Label(janela, text="Horário", fg="black", font=("Verdana", 12, "bold"), bg="white").place(x=105, y=70)

        # horario = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=8)
        # horario.place(x=100, y=100)
        #
        # horario = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=8)
        # horario.place(x=100, y=140)
        #
        # horario = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=8)
        # horario.place(x=100, y=180)
        #
        # horario = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=8)
        # horario.place(x=100, y=220)
        #
        # horario5 = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=8)
        # horario5.place(x=100, y=260)
        #
        # horario6 = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=8)
        # horario6.place(x=100, y=300)

        h = []


        seg = []
        ter = []
        qua = []
        qui = []
        sex = []

        for x in range(0,6):

            h.insert(x, Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=8))
            h[x].place(x = 100, y = 100+(40*x))

            seg.insert(x, Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12))
            seg[x].place(x = 200, y = 100+(40*x))

            ter.insert(x, Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12))
            ter[x].place(x = 350, y = 100+(40*x))

            qua.insert(x, Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12))
            qua[x].place(x = 500, y = 100+(40*x))

            qui.insert(x, Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12))
            qui[x].place(x = 650, y = 100+(40*x))

            sex.insert(x, Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12))
            sex[x].place(x = 800, y = 100+(40*x))




        print()
        # SEGUNDA
        lb = Label(janela, text="Segunda", fg="black", font=("Verdana", 12, "bold"), bg="white").place(x=220, y=70)
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=200, y=100)
        #
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=200, y=140)
        #
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=200, y=180)
        #
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=200, y=220)
        #
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=200, y=260)
        #
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=200, y=300)

        # TERÇA
        lb = Label(janela, text="Terça", fg="black", font=("Verdana", 12, "bold"), bg="white").place(x=385, y=70)
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=350, y=100)
        #
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=350, y=140)
        #
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=350, y=180)
        #
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=350, y=220)
        #
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=350, y=260)
        #
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=350, y=300)

        # QUARTA
        lb = Label(janela, text="Quarta", fg="black", font=("Verdana", 12, "bold"), bg="white").place(x=530, y=70)
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=500, y=100)
        #
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=500, y=140)
        #
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=500, y=180)
        #
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=500, y=220)
        #
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=500, y=260)
        #
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=500, y=300)

        # QUINTA
        lb = Label(janela, text="Quinta", fg="black", font=("Verdana", 12, "bold"), bg="white").place(x=680, y=70)
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=650, y=100)
        #
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=650, y=140)
        #
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=650, y=180)
        #
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=650, y=220)
        #
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=650, y=260)
        #
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=650, y=300)

        #SEXTA
        lb = Label(janela, text="Sexta", fg="black", font=("Verdana", 12, "bold"), bg="white").place(x=830, y=70)
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=800, y=100)
        #
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=800, y=140)
        #
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=800, y=180)
        #
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=800, y=220)
        #
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=800, y=260)
        #
        # disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=12)
        # disciplina.place(x=800, y=300)

        btn = Button(janela, text="SALVAR", fg="white", font=("Verdana", 12, "bold"), bg="magenta").place(x=835, y=350)
        # bd = Banco()
        # bd.insere("segunda","Matemática","9:30")

        
        janela.mainloop()


interface()