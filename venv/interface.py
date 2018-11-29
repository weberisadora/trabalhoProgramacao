from tkinter import *
import tkinter as tk
import banco
import datetime
import time
import pyttsx3


class interface():

    def __init__(self):
        self.bd = banco.Banco()
        self.main()

    def get_sec(self, time_str):
        h, m = time_str.split(':')
        return int(h) * 3600 + int(m) * 60

    def cadastarHorario(self, horario, disciplina, diaSemana, a):

        horario.lstrip('0 ')
        seg = self.get_sec(horario)
        Label(a, text=self.bd.insere(horario, disciplina, diaSemana, seg), fg="black", bg="white").place(x=430, y=600)
        # try:
        #
        # except:
        #     Label(a, text="O horário informado não tem formato de horário (HH:MM)").place(x= 430, y=600)


    def main(self):

        janela = tk.Tk()
        janela.geometry("900x700")
        janela.title("Agenda escolar")
        cor = StringVar(janela)
        cor.set("white")
        l = Label(background=cor.get())
        l.pack(fill='both', expand=True)

        lb = Label(janela, text="AGENDA ESCOLAR", fg="magenta", font=("Verdana", 16, "bold"), bg="white").place(x=430,
                                                                                                                y=10)

        lb = Label(janela, text="Horário:", fg="black", font=("Verdana", 12, "bold"), bg="white").place(x=300, y=100)
        horario = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=8)
        horario.place(x=400, y=100)

        lb = Label(janela, text="Disciplina:", fg="black", font=("Verdana", 12, "bold"), bg="white").place(x=300, y=150)
        disciplina = Entry(janela, fg="black", font=("Verdana", 12), bg="white", width=25)
        disciplina.place(x=400, y=150)

        lb = Label(janela, text="Dia da semana:", fg="black", font=("Verdana", 12, "bold"), bg="white").place(x=300,
                                                                                                              y=200)

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
            b.place(x=450, y=200 + (x * 30))
            x = x + 1

        btn = Button(janela, text="SALVAR", fg="white", font=("Verdana", 12, "bold"), bg="magenta",
                     command=lambda: self.cadastarHorario(horario.get(), disciplina.get(), v.get(), janela))
        btn.place(x=430, y=500)

        btn2 = Button(janela, text="VER AGENDA", fg="white", font=("Verdana", 12, "bold"), bg="magenta",
                      command=lambda: self.verAgenda(janela))
        btn2.place(x=530, y=500)

        # self.cadastrarAgenda(h, seg, ter, qua, qui, sex)

        # bd = Banco()
        # bd.insere("segunda","Matemática","9:30")

        janela.mainloop()

    def verAgenda(self, a):
        a.destroy()

        def atualizar(t):
            self.verAgenda(t)

        def abrirTela(a):
            a.destroy()
            self.main()



        def tercia(num):
            unidades = ["zero", "um", "dois", "três", "quatro",
                        "cinco", "seis", "sete", "oito", "nove"]

            teens = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito",
                     "dezenove"]

            tens = ["dez", "vinte", "trinta", "quarenta", "cinquenta",
                    "sessenta", "setenta", "oitenta", "noventa"]
            numero = str(num)
            numero.zfill(3)
            a = int(numero[0])
            b = int(numero[1])
            c = int(numero[2])
            if a == 0:
                if b == 0:
                    resultado = unidades[c]
                    return resultado
                elif b == 1:
                    if c >= 0 and c <= 9:
                        resultado = teens[c]
                        return resultado
                elif b == 2:
                    if c == 0:
                        resultado = 'vinte'
                        return resultado
                    elif c > 0 and c <= 9:
                        resultado = 'vinte e ' + unidades[c]
                        return resultado
                elif b >= 3 and b <= 9:
                    if c == 0:
                        resultado = tens[b - 1]
                        return resultado
                    if c >= 1 and c <= 9:
                        resultado = tens[b - 1] + ' e ' + unidades[c]
                        return resultado
            if a == 1:
                if b == 0:
                    if c == 0:
                        resultado = 'cem'
                        return resultado
                    elif c > 0 and c <= 9:
                        resultado = 'cento e ' + unidades[c]
                        return resultado
                elif b == 1:
                    if c >= 0 and c <= 9:
                        resultado = 'cento e ' + teens[c]
                        return resultado
                elif b == 2:
                    if c == 0:
                        resultado = 'cento e vinte'
                        return resultado
                    elif c > 0 and c <= 9:
                        resultado = 'cento e vinte e ' + unidades[c]
                        return resultado
                elif b >= 3 and b <= 9:
                    if c == 0:
                        resultado = 'cento e ' + tens[b - 1]
                        return resultado
                    elif c > 0 and c <= 9:
                        resultado = 'cento e ' + tens[b - 1] + ' e ' + unidades[c]
                        return resultado

            elif a >= 2 and a <= 9:
                if a == 2 and b == 0 and c == 0:
                    prefix = 'duzentos'
                elif a == 2:
                    prefix = 'duzentos e '

                if a == 3 and b == 0 and c == 0:
                    prefix = 'trezentos'
                elif a == 3:
                    prefix = 'trezentos e '
                if a == 4 and b == 0 and c == 0:
                    prefix = 'quatrocentos'
                elif a == 4:
                    prefix = 'quatrocentos e '
                if a == 5 and b == 0 and c == 0:
                    prefix = 'quinhentos'
                elif a == 5:
                    prefix = 'quinhentos e '
                if a == 6 and b == 0 and c == 0:
                    prefix = 'seiscentos'
                elif a == 6:
                    prefix = 'seiscentos e '

                if a == 7 and b == 0 and c == 0:
                    prefix = 'setecentos'

                elif a == 7:
                    prefix = 'setecentos e '
                if a == 8 and b == 0 and c == 0:
                    prefix = 'oitocentos'
                elif a == 8:
                    prefix = 'oitocentos e '
                if a == 9 and b == 0 and c == 0:
                    prefix = 'novecentos'
                elif a == 9:
                    prefix = 'novecentos e '

                if b == 0:
                    if c == 0:
                        resultado = prefix
                        return resultado
                    elif c > 0 and c <= 9:
                        resultado = prefix + unidades[c]
                        return resultado
                elif b == 1:
                    if c >= 0 and c <= 9:
                        resultado = prefix + teens[c]
                        return resultado
                        # elif c >= 6 and c <= 9:
                        # resultado = prefix+tens[b-1]+' e '+unidades[c]
                        return resultado
                elif b == 2:
                    if c == 0:
                        resultado = prefix + 'vinte'
                        return resultado
                    elif c > 0 and c <= 9:
                        resultado = prefix + 'vinte e ' + unidades[c]
                        return resultado
                elif b >= 3 and b <= 9:
                    if c == 0:
                        resultado = prefix + tens[b - 1]
                        return resultado
                    elif c > 0 and c <= 9:
                        resultado = prefix + tens[b - 1] + ' e ' + unidades[c]
                        return resultado

        def converter(num):

            result = ''
            numero = str(num)
            numero = numero.zfill(9) + numero
            posicion = 1
            for i in [0, 3, 6]:
                var = numero[i] + numero[i + 1] + numero[i + 2]
                if int(var) != 0:
                    res = tercia(var)
                    if i == 0:
                        result = res + " milhões "
                    elif i == 3:
                        result = result + res + " mil "
                    elif i == 6:
                        result = result + res
            return result

        def ouvir(id):

            sql = "SELECT * FROM horarios WHERE idHorario = {}".format(id)
            self.bd.executa(sql)
            print(id)
            resultado = self.bd.cursor.fetchall()
            result = None
            for registro in resultado:
                result = registro
            en = pyttsx3.init()
            en.setProperty('voice', b'brazil')
            DiasSemana = [
                "Segunda-feira",
                "Terça-feira",
                "Quarta-feira",
                "Quinta-feira",
                "Sexta-feira"
            ]
            horario = result[1].split(":")
            horario[0] = horario[0].lstrip('0 ')
            horario[1] = horario[1].lstrip('0 ')
            print(horario)

            en.say("Horário: {}".format(
                converter(int(horario[0])) + " horas e " + converter(int(horario[1])) + " minutos"))

            q = 2
            for x in range(0, 5):
                if result[q] != None:
                    en.say("Disciplina na {}: {}".format(DiasSemana[x], result[q]))
                else:
                    en.say("Sem disciplinas na {}".format(DiasSemana[x]))
                q = q + 1
            en.runAndWait()

        janela1 = tk.Tk()
        janela1.geometry("1024x500")
        janela1.title("Agenda escolar")
        cor = StringVar(janela1)
        cor.set("white")
        l = Label(background=cor.get())
        l.pack(fill='both', expand=True)

        def excluir(id):
            self.bd.exclui(id)
            atualizar(janela1)

        lb = Label(janela1, text="AGENDA ESCOLAR", fg="magenta", font=("Verdana", 16, "bold"), bg="white").place(
            x=400, y=10)

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

        arr = []

        variavel = IntVar(janela1)
        self.bd.cursor.execute("select * from horarios order by seconds asc")
        resultado = self.bd.cursor.fetchall()
        i = 0
        for registro in resultado:

            Label(janela1, fg="black", font=("Verdana", 12), bg=janela1["bg"], text="" + registro[1]).place(x=100,
                                                                                                            y=100 + (
                                                                                                                    40 * i))
            h = 2
            Radiobutton(janela1, bg="white",  variable=variavel, value=registro[0]).place(x=50,
                                                                                                           y=100 + (
                                                                                                                   40 * i))

            for a in range(0, 5):
                if registro[h] == None:
                    Label(janela1, fg="black", font=("Verdana", 12), bg=janela1["bg"], text=" ").place(
                        x=200 + (150 * a), y=100 + (40 * i))
                else:
                    Label(janela1, fg="black", font=("Verdana", 12), bg=janela1["bg"], text="" + registro[h]).place(
                        x=200 + (150 * a), y=100 + (40 * i))
                h = h + 1
            i = i + 1

        Button(janela1, text="Falar horário", fg="white", font=("Verdana", 12, "bold"), bg="magenta",
               command=lambda: ouvir(variavel.get())).place(x=100, y=10)
        Button(janela1, text = "Cadastrar horário", fg="white", font=("Verdana", 12,"bold"), bg="magenta", command=lambda:abrirTela(janela1)
               ).place(x= 800, y= 10)
        Button(janela1, text="Excluir horário", fg="white", font=("Verdana", 12, "bold"), bg="magenta",
               command=lambda: excluir(variavel.get())
               ).place(x=650, y=10)

        janela1.mainloop()

interface()
