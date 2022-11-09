import datetime
from tkinter import messagebox
import mysql.connector
from math import ceil

def cfp_validatior(cpf):
    CPF = cpf
    digitos = [int(a) for a in str(CPF)]
    mult = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    x = ()
    y = ()

    if len(digitos) == 11:

        prod = [x * y for x, y in zip(digitos[0:9], mult[1:10])]
        print(prod)
        soma = sum(prod)
        resto = soma % 11

        if resto == 0 or 1:
            x = 0

        if resto >= 2:
            x = 11 - resto
        prod = [x * y for x, y in zip(digitos[0:10], mult[0:])]
        print(prod)
        soma = sum(prod)
        resto = soma % 11

        if resto == 0 or 1:
            y = 0

        if resto >= 2:
            y = 11 - resto

        if x == digitos[9] and y == digitos[10]:
            return 'Válido'
        else:
            return 'Inválido'

def databankClients(treeview):
    try:
        con = mysql.connector.connect(host='localhost', database='UEPB_PROJECT', user='root', password='')
        consulta = "select * from USERS order by id"
        cursor = con.cursor()
        cursor.execute(consulta)
        linhas = cursor.fetchall()
        for v in linhas:
            treeview.insert("", "end", values=v)
        con.close()
        cursor.close()
    except:
        messagebox.showerror(title='Database error.',
                             message='Erro ao tentar estabelecer conexão com o banco de dados.', icon='error')

def databankDebts(treeview):
    try:
        con = mysql.connector.connect(host='localhost', database='UEPB_PROJECT', user='root', password='')
        consulta = "select * from debtuser order by id"
        cursor = con.cursor()
        cursor.execute(consulta)
        linhas = cursor.fetchall()
        for v in linhas:
            treeview.insert("", "end", values=v)
        con.close()
        cursor.close()
    except:
        messagebox.showerror(title='Database error.',
                             message='Erro ao tentar estabelecer conexão com o banco de dados.', icon='error')

def deletar(treeview, treeviewDebt):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="UEPB_PROJECT"
        )

        item = treeview.selection()

        valor = treeview.item(item, "values")[3]

        mycursor = mydb.cursor()

        commandDeleteUser = f"DELETE FROM USERS WHERE id = '{valor}';"
        commandDeleteDebts = f"DELETE FROM debtuser WHERE id = '{valor}';"
        consultUsers = "select * from USERS order by id;"
        consultDebts = "select * from debtuser order by id;"

        mycursor.execute(commandDeleteUser)
        mycursor.execute(commandDeleteDebts)

        treeview.delete(*treeview.get_children())
        treeviewDebt.delete(*treeviewDebt.get_children())

        mycursor.execute(consultUsers)
        linhas = mycursor.fetchall()
        for v in linhas:
            treeview.insert("", "end", values=v)

        mycursor.execute(consultDebts)
        linhas = mycursor.fetchall()
        for i in linhas:
            treeviewDebt.insert("", "end", values=i)

        mydb.close()
        mycursor.close()
    except:
        messagebox.showerror(title='Erro de dados.',
                             message='Selecione na arvore de dados um cliente a ser deletado.',
                             icon='error')

def search(treeview, entry):
    try:
        treeview.delete(*treeview.get_children())

        con = mysql.connector.connect(host='localhost', database='UEPB_PROJECT', user='root', password='')
        consulta = f"""select * from USERS
        where NOME like '{entry.get()}%' order by ID;"""
        cursor = con.cursor()
        cursor.execute(consulta)
        linhas = cursor.fetchall()
        for v in linhas:
            treeview.insert("", "end", values=v)
        con.close()
        cursor.close()
    except:
        messagebox.showerror(title='Database error.', message='Erro! verifique se o banco de dados MySQL está ativo.')

def NewUser(nome, contato, cpf, treeview):
    try:

        con = mysql.connector.connect(host='localhost', database='UEPB_PROJECT', user='root', password='')

        validade = cfp_validatior(cpf)

        if validade == 'Válido':

            inserir = f"""INSERT INTO USERS
                           (NOME, CONTATO, CPF) 
                           VALUES 
                           ('{nome}', '{contato}', '{cpf}')"""

            consulta = "select * from USERS order by id"

            cursor = con.cursor()
            cursor.execute(inserir)
            treeview.delete(*treeview.get_children())
            cursor.execute(consulta)

            linhas = cursor.fetchall()

            for v in linhas:
                treeview.insert("", "end", values=v)

            con.commit()
            con.close()
            cursor.close()
        else:
            messagebox.showwarning(title='Erro de validade',
                                 message='CPF inválido, digite corretamente e tente mais uma vez!',
                                 icon='error')
    except:
        messagebox.showerror(title='Erro de dados.',
                             message='Os dados fornecidos estão incompatíveis, verifique-os e tente novamente.',
                             icon='error')

def newPurchase(treeview, entryValue, treeviewDebts):

    treeviewDebts.delete(*treeviewDebts.get_children())

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="UEPB_PROJECT"
    )

    tree = treeview.selection()

    clientId = int(treeview.item(tree, "values")[3])

    date = datetime.datetime.today()

    mycursor = mydb.cursor()

    insertDebt = f"""INSERT INTO debtuser
                       (valor_compra, Data_atual, id) 
                       VALUES 
                       ('{entryValue}', '{date}', '{clientId}')"""
    consulta = "select * from debtuser order by id"

    mycursor.execute(insertDebt)
    mycursor.execute(consulta)

    linhas = mycursor.fetchall()

    for v in linhas:
        treeviewDebts.insert("", "end", values=v)

    mydb.commit()

    mydb.close()

    mycursor.close()

def totalDebt(treeviewId, treeviewDebts, label):
    try:
        treeviewDebts.delete(*treeviewDebts.get_children())
        item = treeviewId.selection()
        valor = treeviewId.item(item, "values")[3]
        con = mysql.connector.connect(host='localhost', database='UEPB_PROJECT', user='root', password='')
        comando = f"select * from debtuser where id = '{valor}'"
        cursor = con.cursor()
        cursor.execute(comando)
        linhas = cursor.fetchall()
        for v in linhas:
            treeviewDebts.insert("", "end", values=v)

        comando = f"SELECT SUM(valor_compra) FROM debtuser where id='{valor}'"
        cursor.execute(comando)

        valor = cursor.fetchone()
        label.config(text=valor)

        con.close()
        cursor.close()
    except:
        messagebox.showerror(title='Database error.',
                             message='Erro ao tentar estabelecer conexão com o banco de dados.', icon='error')

def payment(treeviewId, treeviewDebts, paymentValue):
    try:
        print(paymentValue)
        treeviewDebts.delete(*treeviewDebts.get_children())
        item = treeviewId.selection()
        valor = treeviewId.item(item, "values")[3]
        con = mysql.connector.connect(host='localhost', database='UEPB_PROJECT', user='root', password='')
        comando = f"select * from debtuser where id = '{valor}'"
        cursor = con.cursor()
        cursor.execute(comando)
        linhas = cursor.fetchall()

        for i in linhas:
            print(i[0], i[1])
            #Usar a data e hora como um tipo de ID para as dívidas

        con.close()
        cursor.close()

    except:
        messagebox.showerror(title='Database error.',
                             message='Erro ao tentar estabelecer conexão com o banco de dados.', icon='error')
