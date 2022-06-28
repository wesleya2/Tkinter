from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.botoes_frame_1()
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
        self.bt_limpar = Button(self.frame_1, text='Limpar', border=2, bg = '#107db2', fg = 'white')
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        # Botao Buscar
        self.bt_buscar = Button(self.frame_1, text='Buscar', border=2, bg = '#107db2', fg = 'white')
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        # Botao Novo
        self.bt_novo = Button(self.frame_1, text='Novo', border=2, bg = '#107db2', fg = 'white')
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        # Botao Alterar
        self.bt_alterar = Button(self.frame_1, text='Alterar', border=2, bg = '#107db2', fg = 'white')
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        # Botao Apagar
        self.bt_apagar = Button(self.frame_1, text='Apagar', border=2, bg = '#107db2', fg = 'white')
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


Application()