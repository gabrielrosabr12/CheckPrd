import customtkinter as ctk
from customtkinter import CTkToplevel

class Segunda_tela(ctk.CTkToplevel):
    """Abrir Segunda Janela"""
    def __init__(self,janela):
        self.abrir_tela(janela)


    def abrir_tela(self,janela):
        self.nova_janela = CTkToplevel(janela)
        self.nova_janela.title('Essa é uma nova janela')
        self.nova_janela.geometry('450x810')

        self.nova_janela.attributes('-topmost',True)


