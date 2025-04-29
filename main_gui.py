import customtkinter as ctk
from customtkinter import CTk,CTkToplevel
from model import CarregarConfig
from second_gui import Segunda_tela

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")  # Tema padrão

class InformadorProdutos(ctk.CTk):
    
    def __init__(self):
        """Tela que ficará a Esquerda do usuario usuará a CustomTkinter para criar uma interfaces"""
        super().__init__()
        
        #Configurações da janela.
        self.title("Informador Produtos")
        self.geometry("450x810")

        #Atributo para sempre ficar por cima na tela
        self.attributes('-topmost',True)

        #Chama o método que monta os widgets
        self.config, self.mensagem = CarregarConfig().retornar_config()
        self.configurar_linhas_colunas()
        self.criar_widgets()
        
    def configurar_linhas_colunas(self):
        #Configurando o peso da coluna e da linha
        self.grid_columnconfigure(0,weight=1,minsize=10)
        self.grid_rowconfigure(0,weight=1,minsize=10)
        #Configurando grid do frame dos rotulos
        self.grid_columnconfigure(0,weight=5,minsize=10)
        self.grid_rowconfigure(1,weight=10,minsize=10)
        #self.grid_rowconfigure(2,weight=1)

    def alterar_tema(self):
        if self._get_appearance_mode() == 'light':
            self.tema['text'] = '🌞'
            ctk.set_appearance_mode("dark")
        else:
            self.tema['text'] = '🌙'
            ctk.set_appearance_mode("light")
            

    def criar_widgets(self):
        #Título da tela
        self.frametopo = ctk.CTkFrame(self,width=450)
        self.frametopo.grid_columnconfigure([0,2],weight=1)
        self.frametopo.grid_columnconfigure(1,weight=10)

        self.frametopo.grid_rowconfigure([0,1],weight=1)
        self.frametopo.grid(row=0,sticky="nsew")


        self.tema = ctk.CTkButton(self.frametopo,text='🌞',height=30,width=30,font=('sans-serif',20),command=self.alterar_tema)
        self.tema.grid(row=0,column=0,sticky='n')

        self.teladireita = ctk.CTkButton(self.frametopo,text='🗺',height=30,width=30,font=('sans-serif',20),command=lambda: Segunda_tela(self))
        self.teladireita.grid(row=0,column=2,sticky='n')

        self.titulo = ctk.CTkLabel(self.frametopo, text='Informador Produtos',font=("sans-serif",35,'bold','underline'))
        self.titulo.grid(row=0,column=1,sticky="nsew")

        self.frameinformacoes = ctk.CTkFrame(self,width=450,height=600)
        self.frameinformacoes.grid(row=1,sticky="nsew")
        self.frameinformacoes.grid_columnconfigure(0,weight=1)
        self.criar_informaçoes()

    
        self.framerotulo = ctk.CTkFrame(self,height=2,border_color='red',border_width=2)
        self.framerotulo.grid(row=2,column=0,sticky='nsew')

        self.rotulo = ctk.CTkLabel(self.framerotulo,text=self.mensagem,font=('sans-serif',15),wraplength=450,anchor='e',justify='left')
        self.rotulo.grid(pady=5,sticky='we')

        self.rotulo['text'] = self.mensagem

    def criar_informaçoes(self):
        self.desc = ctk.CTkLabel(self.frameinformacoes,text='Descrição:',font=('sans-serif',35,'bold'),wraplength=450,anchor='e',justify='left')
        self.desc.grid(row=0,column=0,sticky='w')

        self.info1 = ctk.CTkLabel(self.frameinformacoes,text='Dipirona 60 mg EURO'[0:15],font=('sans-serif',50),wraplength=450,anchor='e',justify='left')
        self.info1.grid(row=1,column=0,sticky='w')

        self.codint = ctk.CTkLabel(self.frameinformacoes,text='Código Interno',font=('sans-serif',35,'bold'),wraplength=450,anchor='e',justify='left')
        self.codint.grid(row=2,column=0,sticky='w',pady=(25,0))

        self.info2 = ctk.CTkLabel(self.frameinformacoes,text='658475',font=('sans-serif',50),wraplength=450,anchor='e',justify='left')
        self.info2.grid(row=3,column=0,sticky='w')

        self.endereco = ctk.CTkLabel(self.frameinformacoes,text='Endereço CD',font=('sans-serif',35,'bold'),wraplength=450,anchor='e',justify='left')
        self.endereco.grid(row=4,column=0,sticky='w',pady=(25,0))

        self.info3 = ctk.CTkLabel(self.frameinformacoes,text='51-A-003D',font=('sans-serif',50),wraplength=450,anchor='e',justify='left')
        self.info3.grid(row=5,column=0,sticky='w')



        self.frame_fornecedor = ctk.CTkFrame(self.frameinformacoes,fg_color='transparent')
        self.frame_fornecedor.grid(row=6,column=0,sticky='nsew',pady=(25,0))
        self.frame_fornecedor.grid_columnconfigure([0,1],weight=1)

        self.fornecedor = ctk.CTkLabel(self.frame_fornecedor,text='Fornecedor',font=('sans-serif',35,'bold'),wraplength=225,anchor='e',justify='left')
        self.fornecedor.grid(row=0,column=0,sticky='w')

        self.info4 = ctk.CTkLabel(self.frame_fornecedor,text='Euro Farma',font=('sans-serif',30),wraplength=450,anchor='e',justify='left')
        self.info4.grid(row=1,column=0,sticky='w')

        self.cod_fornece = ctk.CTkLabel(self.frame_fornecedor,text='Cod Fornece',font=('sans-serif',35,'bold'),wraplength=225,justify='left')
        self.cod_fornece.grid(row=0,column=1,sticky='w')

        self.info5 = ctk.CTkLabel(self.frame_fornecedor,text='M52145',font=('sans-serif',30))
        self.info5.grid(row=1,column=1,sticky='w')

        self.grupo = ctk.CTkLabel(self.frame_fornecedor,text='Grupo',font=('sans-serif',35,'bold'),wraplength=225,justify='left')
        self.grupo.grid(row=2,column=0,sticky='w',pady=(25,0))

        self.info5 = ctk.CTkLabel(self.frame_fornecedor,text='A1A2',font=('sans-serif',30))
        self.info5.grid(row=3,column=0,sticky='w')

        self.custo = ctk.CTkLabel(self.frame_fornecedor,text='Custo',font=('sans-serif',35,'bold'),wraplength=225,justify='left')
        self.custo.grid(row=2,column=1,sticky='w',pady=(25,0))

        self.info6 = ctk.CTkLabel(self.frame_fornecedor,text='R$ 41,50',font=('sans-serif',30))
        self.info6.grid(row=3,column=1,sticky='w')


# Executa o app
if __name__ == "__main__":
    app = InformadorProdutos()
    app.mainloop()