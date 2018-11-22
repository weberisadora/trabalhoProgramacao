from tkinter import *
import tkinter as tk
import banco
import datetime
class interface():

    def __init__(self):
        self.bd = banco.Banco()
        self.main()

    def cadastarHorario(self, horario, disciplina, diaSemana):
       self.bd.insere(horario, disciplina, diaSemana)



    def main(self):

        janela = tk.Tk()
        janela.geometry("900x700")
        janela.title("Agenda escolar")
        cor = StringVar(janela)
        cor.set("white")
        l = Label(background=cor.get())
        l.pack(fill='both', expand=True)

        lb = Label(janela, text="AGENDA ESCOLAR", fg="magenta", font=("Verdana", 16, "bold"), bg="white").place(x=430, y=10)

        lb = Label(janela, text="Horário:", fg="black", font=("Verdana", 12, "bold"), bg="white").place(x=300, y=100)
        horario = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=8)
        horario.place(x=400, y=100)

        lb = Label(janela, text="Disciplina:", fg="black", font=("Verdana", 12, "bold"), bg="white").place(x=300, y=150)
        disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=25)
        disciplina.place(x=400, y=150)

        lb = Label(janela, text="Dia da semana:", fg="black", font=("Verdana", 12, "bold"), bg="white").place(x=300, y=200)

        MODES = [
            "Segunda",
            "Terca",
            "Quarta",
            "Quinta",
            "Sexta"
        ]
        x = 0
        v = StringVar()
        v.set("Segunda")
        for text in MODES:

            b = Radiobutton(janela, text=text, bg="white",
                            variable=v, value=text)
            b.place(x=450, y= 200+(x*30))
            x = x + 1


        btn = Button(janela, text="SALVAR", fg="white", font=("Verdana", 12, "bold"), bg="magenta", command = lambda: self.cadastarHorario(horario.get(), disciplina.get(), v.get()))
        btn.place(x=430, y=500)

        btn2 = Button(janela, text="VER AGENDA", fg="white", font=("Verdana", 12, "bold"), bg="magenta", command = lambda: self.verAgenda())
        btn2.place(x = 530, y=500)

        # self.cadastrarAgenda(h, seg, ter, qua, qui, sex)

        # bd = Banco()
        # bd.insere("segunda","Matemática","9:30")


        janela.mainloop()


    def verAgenda(self):
        janela1 = tk.Tk()
        janela1.geometry("1024x500")
        janela1.title("Agenda escolar")
        cor = StringVar(janela1)
        cor.set("white")
        l = Label(background=cor.get())
        l.pack(fill='both', expand=True)

        lb = Label(janela1, text="AGENDA ESCOLAR", fg="magenta", font=("Verdana", 16, "bold"), bg="white").place(x=450, y=10)




        lb = Label(janela1, text="Horário", fg="black", font=("Verdana", 12, "bold"), bg="white").place(x=105, y=70)

        # SEGUNDA

        lb = Label(janela1, text="Segunda", fg="black", font=("Verdana", 12, "bold"), bg="white").place(x=220, y=70)

        # TERÇA
        lb = Label(janela1, text="Terça", fg="black", font=("Verdana", 12, "bold"), bg="white").place(x=385, y=70)

        # QUARTA
        lb = Label(janela1, text="Quarta", fg="black", font=("Verdana", 12, "bold"), bg="white").place(x=530, y=70)

        # QUINTA
        lb = Label(janela1, text="Quinta", fg="black", font=("Verdana", 12, "bold"), bg="white").place(x=680, y=70)

        # SEXTA
        lb = Label(janela1, text="Sexta", fg="black", font=("Verdana", 12, "bold"), bg="white").place(x=830, y=70)





        arr = [
        ]



        v = IntVar()
        self.bd.cursor.execute("select * from horarios order by horario asc")
        resultado = self.bd.cursor.fetchall()
        i=0
        
        for registro in resultado:


            arr.insert(i, registro[0])
            Label(janela1, fg="black", font=("Verdana", 12), bg=janela1["bg"], text=""+registro[1]).place(x = 100, y = 100+(40*i))
            h = 2
            for a in range(0, 5):

                if registro[h] == None:
                    Label(janela1, fg="black", font=("Verdana", 12), bg=janela1["bg"], text = " ").place(x= 200+(150*a), y=100 + (40 * i))
                else:
                    Label(janela1, fg="black", font=("Verdana", 12), bg=janela1["bg"], text=""+registro[h]).place(x= 200+(150*a), y=100 + (40 * i))

                h = h + 1

            i=i+1
        

        q = 0
        for text in arr:

            b = Radiobutton(janela1,  bg="white",
                            variable=v, value=text)
            b.place(x=50, y=100 + (40 * q))
            q = q + 1



        janela1.mainloop()



interface()