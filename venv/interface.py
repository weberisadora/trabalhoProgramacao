from tkinter import *
import tkinter as tk
import banco

class interface():

    def __init__(self):
        self.bd = banco.Banco()
        self.main()

    def cadastarAgenda(self, horario, segunda, terca, quarta, quinta, sexta):

        dias=[]
        dias.insert(0, "segunda")
        dias.insert(1, "terca")
        dias.insert(2, "quarta")
        dias.insert(3, "quinta")
        dias.insert(4, "sexta")

        materias = []
        materias.insert(0, segunda)
        materias.insert(1, terca)
        materias.insert(2, quarta)
        materias.insert(3, quinta)
        materias.insert(4, sexta)

        try:
            for i in range(0,5):
                for x in range(0,6):
                    if (materias[i][x].get() != "" and horario[x].get() != ""):
                        self.bd.insere(dias[i], materias[i][x].get(), horario[x].get())

            self.verAgenda()
        except:
            print("Erro")




    def main(self):

        janela = tk.Tk()
        janela.geometry("900x700")
        janela.title("Agenda")
        cor = StringVar(janela)
        cor.set("white")
        l = Label(background=cor.get())
        l.pack(fill='both', expand=True)

        lb = Label(janela, text="AGENDA", fg="magenta", font=("Verdana", 16, "bold"), bg="white").place(x=430, y=10)

        lb = Label(janela, text="Horário:", fg="black", font=("Verdana", 12, "bold"), bg="white").place(x=300, y=100)
        horario = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=8)
        horario.place(x=400, y=100)

        lb = Label(janela, text="Disciplina:", fg="black", font=("Verdana", 12, "bold"), bg="white").place(x=300, y=150)
        disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=25)
        disciplina.place(x=400, y=150)

        lb = Label(janela, text="Dia da semana:", fg="black", font=("Verdana", 12, "bold"), bg="white").place(x=300, y=200)
        rb1 = Radiobutton(janela, text="Segunda-feira", fg="black", font=("Verdana", 12), bg="white", width=25)

        bt=Button(janela, text="SALVAR", fg="white", font=("Verdana", 12, "bold"), bg="magenta", command = lambda: self.cadastarAgenda(h, seg,ter,qua, qui, sex))
        bt.place(x=430, y=500)

        # self.cadastrarAgenda(h, seg, ter, qua, qui, sex)

        # bd = Banco()
        # bd.insere("segunda","Matemática","9:30")


        janela.mainloop()


    def verAgenda(self):
        janela = tk.Tk()
        janela.geometry("1024x500")
        janela.title("Agenda")
        cor = StringVar(janela)
        cor.set("white")
        l = Label(background=cor.get())
        l.pack(fill='both', expand=True)

        lb = Label(janela, text="AGENDA", fg="magenta", font=("Verdana", 16, "bold"), bg="white").place(x=450, y=10)
        dias = ["segunda", "terca","quarta","quinta","sexta"]
        segunda = []
        terca = []
        quarta = []
        quinta = []
        sexta = []

        h = []
        seg = []
        ter = []
        qua = []
        qui = []
        sex = []

        lb = Label(janela, text="Horário", fg="black", font=("Verdana", 12, "bold"), bg="white").place(x=105, y=70)

        # SEGUNDA

        lb = Label(janela, text="Segunda", fg="black", font=("Verdana", 12, "bold"), bg="white").place(x=220, y=70)

        # TERÇA
        lb = Label(janela, text="Terça", fg="black", font=("Verdana", 12, "bold"), bg="white").place(x=385, y=70)

        # QUARTA
        lb = Label(janela, text="Quarta", fg="black", font=("Verdana", 12, "bold"), bg="white").place(x=530, y=70)

        # QUINTA
        lb = Label(janela, text="Quinta", fg="black", font=("Verdana", 12, "bold"), bg="white").place(x=680, y=70)

        # SEXTA
        lb = Label(janela, text="Sexta", fg="black", font=("Verdana", 12, "bold"), bg="white").place(x=830, y=70)

        for x in range(0,6):

            h.insert(x, Label(janela, fg="black", font=("Verdana", 12), bg=janela["bg"]))
            h[x].place(x = 100, y = 100+(40*x))

            seg.insert(x, Label(janela, fg="black", font=("Verdana", 12), bg=janela["bg"]))
            seg[x].place(x = 200, y = 100+(40*x))

            ter.insert(x, Label(janela, fg="black", font=("Verdana", 12), bg=janela["bg"]))
            ter[x].place(x = 350, y = 100+(40*x))

            qua.insert(x, Label(janela, fg="black", font=("Verdana", 12), bg=janela["bg"]))
            qua[x].place(x = 500, y = 100+(40*x))

            qui.insert(x, Label(janela, fg="black", font=("Verdana", 12), bg=janela["bg"]))
            qui[x].place(x = 650, y = 100+(40*x))

            sex.insert(x, Label(janela, fg="black", font=("Verdana", 12), bg=janela["bg"]))
            sex[x].place(x = 800, y = 100+(40*x))

        for d in range(0,5):
            try:
                self.bd.cursor.execute("select * from "+dias[i])
                resultado = self.bd.cursor.fetchall()
                for registro in resultado:
                    for hr in range(0,6):
                        if i == 0:
                            h[hr]["text"]= registro[1]
                            seg[i]["text"]= registro[0]
                        elif i == 1:
                            h[i]["text"] = registro[1]
                            ter[i]["text"] = registro[0]
                        elif i == 2:
                            h[i]["text"] = registro[1]
                            qua[i]["text"] = registro[0]
                        elif i == 3:
                            h[i]["text"] = registro[1]
                            qui[i]["text"] = registro[0]
                        elif i == 4:
                            h[i]["text"] = registro[1]
                            sex[i]["text"] = registro[0]

            except:
                print("Erro: Impossível obter dados")




        janela.mainloop()



interface()