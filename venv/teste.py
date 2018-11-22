import banco

bd = banco.Banco()
dias = ["segunda", "terca","quarta","quinta","sexta"]
for i in range(0, 5):
    try:
        bd.cursor.execute("select * from " + dias[i])
        resultado = bd.cursor.fetchall()
        for registro in resultado:
            if i == 0:
                print(""+dias[i] +": ", registro)
            elif i == 1:
                print("" + dias[i] + ": ", registro)
            elif i == 2:
                print("" + dias[i] + ": ", registro)
            elif i == 3:
                print("" + dias[i] + ": ", registro)
            elif i == 4:
                print("" + dias[i] + ": ", registro)
            elif i == 5:
                print("" + dias[i] + ": ", registro)


    except:
        print("Erro: Impossível obter dados")