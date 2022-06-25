from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        root.mainloop()

    def tela(self):
        self.root.title('Cadastro de Clientes')
        self.root.configure(background='#1e3743')
        self.root.geometry('768x700')
        self.root.resizable(True, True)
        self.root.maxsize(width=768, height=700)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg = '#dfe3ee', highlightbackground= '#759fe6', highlightthickness= '2')
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.46)

        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness='2')
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

Application()