from tkinter import *
from tkinter import ttk
import configFunctions.functions

deletar_depois = 0


def loginWindow():
    login_window = Tk()

    login_window.title("Login")
    login_window.config(width=100, height=100)
    login_window.resizable(False, False)

    frame2 = Frame(login_window, width=650, height=700, relief='raised', borderwidth=6, pady=10, padx=10)
    frame2.pack(anchor=N)

    cabeca = Label(frame2, text='LOGIN', width=10, font=('argparse', 25))
    cabeca.grid(column=0, row=0, pady=20, columnspan=2)

    Login2 = Label(frame2, text='LOGIN:', padx=5, pady=5)
    Login2.grid(column=0, row=1, pady=5, padx=5, sticky='W')
    et_login2 = Entry(frame2, width=30, border=3)
    et_login2.grid(column=1, row=1)

    Senha2 = Label(frame2, text='PASSWORD:', padx=5, pady=5)
    Senha2.grid(column=0, row=2, pady=4, padx=5, sticky='W')
    et_senha2 = Entry(frame2, width=30, border=3, show='*')
    et_senha2.grid(column=1, row=2)

    mostrarSenha = Button(frame2, text='°', command="")
    mostrarSenha.grid(column=2, row=2)

    NewWindow = Button(frame2, text='Janela 1', width=10, height=2, command="")
    NewWindow.grid(columnspan=2, row=4)

    login_window.mainloop()


def clientWindow():
    client_window = Tk()
    client_window.title("Dados de Clientes")
    client_window.state('zoomed')

    frame_clients = Frame(client_window, width=500, height=800, relief='raised', borderwidth=6, padx=2, pady=2)
    frame_clients.pack(side=LEFT, fill=Y, expand=False)

    # Lista de clientes:

    clients = ttk.Treeview(frame_clients, columns=(
        'Nome', 'Contato', 'Valor Total', 'CPF', 'ID'), show='headings', height=50)

    clients.heading('Nome', text='Nome')
    clients.heading('Contato', text='Contato')
    clients.heading('Valor Total', text='Valor Total')
    clients.heading('CPF', text='CPF')
    clients.heading('ID', text='ID')
    clients.pack(side=TOP, fill=X, expand=False)

    clients.column('ID', width=60)

    configFunctions.functions.databank(clients)

    clients.bind("<<TreeviewSelect>>", configFunctions.functions.print_element)

    # Frame de informações do cliente selecionado:

    frame_clients_informations = Frame(client_window, width=100, height=300, relief="raised", border=6, padx=2, pady=2)
    frame_clients_informations.pack(side=TOP, fill=X, expand=False)
    clientsInformations = ttk.Treeview(frame_clients_informations, columns=(
        'Valor da Compra', 'Data'), show='headings', height=10)

    clientsInformations.heading('Valor da Compra', text='Valor da Compra')
    clientsInformations.heading('Data', text='Data')
    clientsInformations.pack(side=TOP, fill=X, expand=False)

    clientsInformations.column('Valor da Compra', width=100)
    clientsInformations.column('Data', width=50)

    total_label = Label(frame_clients_informations, text='Total: ', font=("Arial", 25))
    total_label_value = Label(frame_clients_informations, text=deletar_depois, font=("Arial", 25))
    total_label.pack(side=LEFT, fill=X, expand=False)
    total_label_value.pack(side=LEFT, fill=X, expand=False)

    # Frame de cadastro de novos clientes:

    frame_clients_register = Frame(client_window, width=100, height=300, relief="raised", border=6, padx=2, pady=2)
    frame_clients_register.pack(side=BOTTOM, fill=X, expand=False)

    name_label = Label(frame_clients_register, text='Nome: ')
    name_entry = Entry(frame_clients_register, width=50, border=5)
    name_label.pack(padx=10, pady=10)
    name_entry.pack()
    contact_label = Label(frame_clients_register, text='Contato: ')
    contact_entry = Entry(frame_clients_register, width=50, border=5)
    contact_label.pack(padx=10, pady=10)
    contact_entry.pack()
    totalValue_label = Label(frame_clients_register, text='Divida Total: ')
    totalValue_entry = Entry(frame_clients_register, width=50, border=5)
    totalValue_label.pack(padx=10, pady=10)
    totalValue_entry.pack()
    cpf_label = Label(frame_clients_register, text='CPF: ')
    cpf_entry = Entry(frame_clients_register, width=50, border=5)
    cpf_label.pack(padx=10, pady=10)
    cpf_entry.pack()

    # Botões da cadastro e de deletar clientes:

    client_register_buttom = Button(client_window, text="Deletar Cliente", width=20, height=4, border=5)
    client_register_buttom.pack(side=RIGHT, fill=X, expand=False, padx=35)
    client_delete_buttom = Button(client_window, text="Deletar Cliente", width=20, height=4, border=5,
                                  command=lambda: clients)
    client_delete_buttom.pack(side=RIGHT, fill=X, expand=False, padx=35)

    client_window.mainloop()
