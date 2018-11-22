import pymysql

class Banco():

    def __init__(self):
        self.con = pymysql.connect("localhost", "root", "", "agenda")
        self.cursor = self.con.cursor()
        

    def insere(self, horario, disciplina, dia):
        igual = False
        self.cursor.execute("select horario from horarios")
        resultado = self.cursor.fetchall()
        for registro in resultado:
            if registro == horario:
                igual = True
                break

        if igual == True:
            print("É igual")
            sql = "UPDATE horarios set " + dia + " = '" + disciplina + "' WHERE horario = '" + horario + "'"

        else:
            sql = "INSERT INTO horarios (horario, " + dia + ") VALUES ('" + horario + "', '" + disciplina + "')"
            print("Não é igual")

        self.executa(sql)

    def exclui(self, dia, disciplina):
        sql = "DELETE FROM "+dia+" WHERE disciplina = '"+disciplina+"'"
        self.executa(sql)

    def atualiza(self, dia, disciplina, horario):
        sql = "UPDATE FROM "+dia+" set disciplina='"+disciplina+"', horario='"+horario+"'"
        self.executa(sql)

    def executa(self, sql):
        print()
        try:
            self.cursor.execute(sql)
            self.con.commit()
            print("Deu")
        except:
            print("Não deu")
            self.con.rollback()

