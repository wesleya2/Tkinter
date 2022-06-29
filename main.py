from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()

class Funcs():
    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
    def conecta_db(self):
        self.conn = sqlite3.connect('Clientes.bd')
        self.cursor = self.conn.cursor(); print('Conectando banco de dados')
    def desconecta_bd(self):
        self.conn.close(); print('Desconectando banco de dados')
    def montaTabelas(self):
        self.conecta_db(); print('Conectando ao banco de dados')
        ###Criar tabela###
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)
            );
        """)
        self.conn.commit(); print('Banco de dados criado')
        self.desconecta_bd()
    def add_cliente(self):
        self.variaveis()
        self.conecta_db()
        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade)
                VALUES (?,?,?)""", (self.nome, self.telefone, self.cidade))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_db()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes 
            ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_bd()
    def duploclick(self, event):
        self.limpa_tela()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1,col2,col3,col4 = self.listaCli.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)
    def deleta_cliente(self):
        self.variaveis()
        self.conecta_db()
        self.cursor.execute("""DELETE FROM clientes WHERE cod = ?""",(self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_tela()
        self.select_lista()
    def alterar_cliente(self):
        self.variaveis()
        self.conecta_db()
        self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ?
            WHERE cod = ? """,(self.nome,self.telefone,self.cidade,self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()

class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.botoes_frame_1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
        self.Menus()
        root.mainloop()

    def tela(self):
        self.root.title('Cadastro de Clientes')
        self.root.configure(background='#1e3743')
        self.root.geometry('768x700')
        self.root.resizable(False, False)
        self.root.maxsize(width=768, height=700)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground= '#759fe6', highlightthickness= '2')
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.46)

        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness='2')
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def botoes_frame_1(self):
        #Botao Limpar #bg cor botão, ufg cor do texto, font(tipo,tamanho,italigo/negrito) fg
        self.bt_limpar = Button(self.frame_1, text='Limpar', border=2, bg = '#107db2', fg = 'white', command= self.limpa_tela)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        # Botao Buscar
        self.bt_buscar = Button(self.frame_1, text='Buscar', border=2, bg = '#107db2', fg = 'white')
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        # Botao Novo
        self.bt_novo = Button(self.frame_1, text='Novo', border=2, bg = '#107db2', fg = 'white', command=self.add_cliente)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        # Botao Alterar
        self.bt_alterar = Button(self.frame_1, text='Alterar', border=2, bg = '#107db2', fg = 'white', command=self.alterar_cliente)
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        # Botao Apagar
        self.bt_apagar = Button(self.frame_1, text='Apagar', border=2, bg = '#107db2', fg = 'white', command=self.deleta_cliente)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        #Label Frame1/Input Código fg = '#107db2'
        self.lb_codigo = Label(self.frame_1, text = 'Código', bg = '#dfe3ee')
        self.lb_codigo.place(relx=0.04, rely=0.05)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.04, rely=0.11, relwidth=0.15, relheight=0.14)

        #Label Frame1/Input Nome
        self.lb_nome = Label(self.frame_1, text='Nome')
        self.lb_nome.place(relx=0.04, rely=0.33)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.04, rely=0.43, relwidth=0.8, relheight=0.14)

        # Label Frame1/Input Telefone
        self.lb_telefone = Label(self.frame_1, text='Telefone')
        self.lb_telefone.place(relx=0.04, rely=0.63)

        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.04, rely=0.73, relwidth=0.16, relheight=0.14)

        #Label Frame1/Input Cidade

        self.lb_cidade = Label(self.frame_1, text='Cidade')
        self.lb_cidade.place(relx=0.21, rely=0.63)

        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.21, rely=0.73, relwidth=0.16, relheight=0.14)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height = 3, columns= ("col1", "col2", "col3", "col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Código")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")

        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscrollcommand=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.listaCli.bind("<Double-1>",self.duploclick)

    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.root.destroy()

        menubar.add_cascade(label= "Opções",menu= filemenu)
        menubar.add_cascade(label= "Sobre",menu= filemenu2)

        filemenu.add_command(label="Sair", command= Quit)
        filemenu2.add_command(label="Limpa Cliente",command= self.limpa_tela)


Application()