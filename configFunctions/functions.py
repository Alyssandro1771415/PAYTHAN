from tkinter import messagebox
import mysql.connector


def databank(treeview):
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

def atualizar(treeview):
    try:
        treeview.delete(*treeview.get_children())

        con = mysql.connector.connect(host='localhost', database='projetos', user='root', password='')
        consulta = "select * from projeto order by id"
        cursor = con.cursor()
        cursor.execute(consulta)
        linhas = cursor.fetchall()
        for v in linhas:
            treeview.insert("", "end", values=v)
        con.close()
        cursor.close()
    except:
        messagebox.showerror(title='Database error.', message='Erro! verifique se o banco de dados MySQL está ativo.')

def deletar(treeview):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="projetos"
    )

    item = treeview.selection()

    valor = treeview.item(item, "values")[0]

    mycursor = mydb.cursor()

    sql = f"DELETE FROM projeto WHERE id = '{valor}';"

    consulta = "select * from projeto order by id"

    mycursor.execute(sql)

    mydb.commit()

    treeview.delete(*treeview.get_children())

    mycursor.execute(consulta)

    linhas = mycursor.fetchall()

    for v in linhas:
        treeview.insert("", "end", values=v)
    mydb.close()

    mycursor.close()

def pesquisar(treeview, entry):
    try:
        treeview.delete(*treeview.get_children())

        con = mysql.connector.connect(host='localhost', database='projetos', user='root', password='')
        consulta = f"""select * from projeto
        where project like '{entry.get()}%';"""
        cursor = con.cursor()
        cursor.execute(consulta)
        linhas = cursor.fetchall()
        for v in linhas:
            treeview.insert("", "end", values=v)
        con.close()
        cursor.close()
    except:
        messagebox.showerror(title='Database error.', message='Erro! verifique se o banco de dados MySQL está ativo.')

def NewUser(nome, contato, valor_inicial, cpf):
    try:
        con = mysql.connector.connect(host='localhost', database='UEPB_PROJECT', user='root', password='')
        inserir = f"""INSERT INTO USERS
                       (NOME, CONTATO, VALOR_INICIAL, CPF) 
                       VALUES 
                       ('{nome}', '{contato}', '{valor_inicial}', '{cpf}')"""

        get_id = f"""select id from USERS wherer CPF="{cpf}"
                """
        cursor = con.cursor()
        cursor.execute(inserir)

        id = 0

        valor_id = cursor.execute(get_id)
        for i in valor_id:
            for j in i:
                id = j
        userTable = f"""CREATE TABLE user{id}(valor_compra float default 0,
                    Data_atual timestamp default current_timestamp)
                                     """
        cursor.execute(userTable)
        con.commit()
        con.close()
        cursor.close()
    except:
        messagebox.showerror(title='Erro de dados.',
                             message='Os dados fornecidos estão incompatíveis, verifique-os e tente novamente.',
                             icon='error')

def print_element(event):
    tree = event.widget
    teste = tree.item(tree.selection())
    print(teste["values"][4])
