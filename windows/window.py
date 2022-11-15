from tkinter import *
from tkinter import ttk
import configFunctions.functions
import matplotlib.pyplot as plt
import numpy as np
import random

def loginWindow():
    login_window = Tk()

    login_window.title("Login")
    login_window.config(width=100, height=100)
    login_window.resizable(False, False)

    frame2 = Frame(login_window, width=650, height=700, relief='raised', borderwidth=6, pady=10, padx=10)
    frame2.pack(anchor=N)

    cabeca = Label(frame2, text='LOGIN', width=10, font=('argparse', 25))
    cabeca.grid(column=0, row=0, pady=20, columnspan=2)

    Login = Label(frame2, text='LOGIN:', padx=5, pady=5)
    Login.grid(column=0, row=1, pady=5, padx=5, sticky='W')
    et_login = Entry(frame2, width=30, border=3)
    et_login.grid(column=1, row=1)

    Senha = Label(frame2, text='PASSWORD:', padx=5, pady=5)
    Senha.grid(column=0, row=2, pady=4, padx=5, sticky='W')
    et_senha = Entry(frame2, width=30, border=3, show='*')
    et_senha.grid(column=1, row=2)

    """Aqui tive que declarar essa variável como global para poder acessa-la e e alterar seu valor de dentro do botão
    Não vi problemas devido a se tratarde de uma variável que semplesmente é usada para mudar o estado de mostrar ou 
    esconder senha"""

    global is_on
    is_on = True
    def switch(on_button, entry):
        global is_on

        # Determinando se está On ou Off
        if is_on:
            on_button.config(text="-")
            entry.config(show="")
            is_on = False
        else:
            on_button.config(text="°")
            entry.config(show="*")
            is_on = True

    mostrarSenha = Button(frame2, text='°', command=lambda: switch(mostrarSenha, et_senha))
    mostrarSenha.grid(column=2, row=2)

    NewWindow = Button(frame2, text='Entrar', width=10, height=2, command=lambda: configFunctions.functions.validate_login(et_login.get(), et_senha.get()))
    NewWindow.grid(columnspan=2, row=4)

    login_window.mainloop()

def clientWindow():

    client_window = Tk()
    client_window.title("Dados de Clientes")
    client_window.state('zoomed')
    client_window.config(background="green")

    # Lista de clientes:

    frame_clients = Frame(client_window, width=500, height=50, relief='raised', borderwidth=6, padx=2, pady=2)
    frame_clients.pack(side=LEFT, fill=Y,expand=False)

    clients = ttk.Treeview(frame_clients, columns=(
        'Nome', 'Contato', 'CPF', 'ID'), show='headings', height=20)

    clients.heading('Nome', text='Nome')
    clients.heading('Contato', text='Contato')
    clients.heading('CPF', text='CPF')
    clients.heading('ID', text='ID')
    clients.pack(side=TOP, fill=X, expand=False)

    clients.column('ID', width=60)

    configFunctions.functions.databankClients(clients)

    search_label = Label(frame_clients, text='Pesquisar: ')
    search_label.pack(side=TOP, expand=False)
    search_entry = Entry(frame_clients, width=50, border=5)
    search_entry.pack(side=TOP, expand=False)
    search_buttom = Button(frame_clients, text='Pesquisar', command=lambda: configFunctions.functions.search(clients, search_entry))
    search_buttom.pack(side=TOP, expand=False)

    client_delete_buttom = Button(frame_clients, background='sea green', text="Deletar Cliente", width=15, height=3, border=5,
                                  command=lambda: configFunctions.functions.deletar(clients, clientsInformations))
    client_delete_buttom.pack(side=RIGHT, fill=X, expand=False, padx=35, pady=35)

    client_SUM_buttom = Button(frame_clients, background='sea green', text="Somar Dividas", width=15, height=3, border=5,
                                  command=lambda: configFunctions.functions.totalDebt(clients, clientsInformations, total_label_value))
    client_SUM_buttom.pack(side=LEFT, fill=X, expand=False, padx=35, pady=35)

    statistcs_buttom = Button(frame_clients, background='sea green', text='Estatísticas de Vendas', width=15, border=5, height=3, command=statistcsWindow)
    statistcs_buttom.pack(side=BOTTOM, fill=X, expand=False, padx=35, pady=35)

    # Frame de cadastro de novos clientes:

    frame_clients_register = Frame(client_window, width=100, height=3, relief="raised", border=6, padx=2, pady=2)
    frame_clients_register.pack(side=BOTTOM, fill=X, expand=False)

    name_label = Label(frame_clients_register, text='Nome: ')
    name_entry = Entry(frame_clients_register, width=50, border=5)
    name_label.pack(padx=10, pady=10)
    name_entry.pack()
    contact_label = Label(frame_clients_register, text='Contato: ')
    contact_entry = Entry(frame_clients_register, width=50, border=5)
    contact_label.pack(padx=10, pady=10)
    contact_entry.pack()
    cpf_label = Label(frame_clients_register, text='CPF: ')
    cpf_entry = Entry(frame_clients_register, width=50, border=5)
    cpf_label.pack(padx=10, pady=10)
    cpf_entry.pack()

    client_register_buttom = Button(frame_clients_register,background='sea green', text="Cadastrar Cliente", width=15, height=3, border=5,
                                    command=lambda: configFunctions.functions.NewUser
                                    (name_entry.get(), contact_entry.get(), cpf_entry.get(), clients))
    client_register_buttom.pack(side=TOP, fill=Y, expand=False)

    # Frame de informações do cliente selecionado:

    frame_clients_informations = Frame(client_window,width=100, height=600, relief="raised", border=6, padx=2, pady=2)
    frame_clients_informations.pack(side=TOP, fill=X, expand=False)
    clientsInformations = ttk.Treeview(frame_clients_informations, columns=(
        'Valor da Compra', 'Data', 'id'), show='headings', height=10)

    clientsInformations.heading('Valor da Compra', text='Valor da Compra')
    clientsInformations.heading('Data', text='Data')
    clientsInformations.heading('id', text='Id')
    clientsInformations.pack(side=TOP, fill=X, expand=False)

    clientsInformations.column('Valor da Compra', width=100)
    clientsInformations.column('Data', width=25)
    clientsInformations.column('id', width=10)

    configFunctions.functions.databankDebts(clientsInformations)

    payment = Label(frame_clients_informations, text="Pagamento: ", padx=5, pady=5)
    payment.pack(side=TOP, expand=False)
    paymentEntry = Entry(frame_clients_informations, width=30, border=5)
    paymentEntry.pack(side=TOP, expand=False)
    paymentButtom = Button(frame_clients_informations, background='sea green', text="Pagar", padx=15, pady=5, command=lambda: configFunctions.functions.payment(clients, clientsInformations, paymentEntry.get()))
    paymentButtom.pack(side=TOP, expand=False)
    newPurchase = Label(frame_clients_informations, text="Nova Compra: ", padx=5,pady=5)
    newPurchase.pack(side=TOP, expand=False)
    newPurchaseEntry = Entry(frame_clients_informations, width=30, border=5)
    newPurchaseEntry.pack(side=TOP,expand=False)
    newPurchaseButtom = Button(frame_clients_informations, background='sea green', text="Comprar", padx=5, pady=5, command=lambda: configFunctions.functions.newPurchase(clients, newPurchaseEntry.get(), clientsInformations))
    newPurchaseButtom.pack(side=TOP, expand=False)

    total_label = Label(frame_clients_informations, text='Total: ', font=("Arial", 25))
    total_label_value = Label(frame_clients_informations, text='', font=("Arial", 25))
    total_label.pack(side=LEFT, fill=X, expand=False)
    total_label_value.pack(side=LEFT, fill=X, expand=False)

    client_window.mainloop()

def statistcsWindow():
    # Gráficos de barras 3D
    fig = plt.figure(figsize=(8, 8))
    ax = plt.axes(projection="3d")
    num_barras = 10  # cada barra tem uma posição e um tamanho (ver isso para os 3 eixos)
    x_pos = random.sample(range(20), num_barras)
    print("x_pos", x_pos)
    y_pos = random.sample(range(20), num_barras)
    z_pos = [0] * num_barras
    x_size = np.ones(num_barras)
    y_size = np.ones(num_barras)
    print("y_pos", y_pos)
    z_size = random.sample(range(20), num_barras)
    print("z_size", z_size)
    ax.bar3d(x_pos, y_pos, z_pos, x_size, y_size, z_size, color='green')
    ax.set_title('Estatíticas da Vendas Mensais', fontsize=18)
    ax.set_xlabel('Valor de Vendas', fontsize=15)
    ax.set_ylabel('Mês', fontsize=15)
    ax.set_zlabel('Valor Quitado', fontsize=15)
    ax.view_init(20, 45)
    plt.show()

statistcsWindow()
