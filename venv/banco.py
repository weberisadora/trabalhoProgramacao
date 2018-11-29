import pymysql

class Banco():

    def __init__(self):
        self.con = pymysql.connect("localhost", "root", "", "agenda")
        self.cursor = self.con.cursor()
        

    def insere(self, horario, disciplina, dia, seconds):
        igual = None
        self.cursor.execute("select horario from horarios")
        resultado = self.cursor.fetchall()
        for registro in resultado:

            if registro[0] == horario:
                igual = True
                break

        if igual:
            print("É igual")
            sql = "UPDATE horarios set " + dia + " = '" + disciplina + "' WHERE horario = '" + horario + "'"
            self.executa(sql)
            return "Horário atualizado com sucesso!"

        else:
            sql = "INSERT INTO horarios (horario, " + dia + ", seconds) VALUES ('" + horario + "', '" + disciplina + "', {})".format(seconds)
            print("Não é igual")
            self.executa(sql)
            return "Horário cadastrado com sucesso!"



    def exclui(self, id):
        sql = "DELETE FROM horarios WHERE idHorario = {}".format(id)
        self.executa(sql)

    def atualiza(self, dia, disciplina, horario):
        sql = "UPDATE FROM "+dia+" set disciplina='"+disciplina+"', horario='"+horario+"'"
        self.executa(sql)

    def executa(self, sql):
        try:
            self.cursor.execute(sql)
            self.con.commit()
            print("Cadastrado com sucesso!")
        except:
            print("Erro ao cadastrar")
            self.con.rollback()

