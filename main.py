from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop()

    def tela(self):
        self.root.title('Cadastro de Clientes')
        self.root.configure(background='#1e3743')
        #self.root.geometry('768x700')
        self.root.resizable(True, True)
        self.root.maxsize(width=768, height=700)

    def frames_da_tela(self):
        self.frame1 = Frame(self.root)


Application()