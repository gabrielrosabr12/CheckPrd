import configparser
import os

class CarregarConfig():
    def __init__(self,caminho:str=os.getcwd()):
        """Classe para carregar caminho config.ini"""
        
        #Cria o caminho e carrega o configparser
        self.config = configparser.ConfigParser()
        self.caminho = os.path.join(caminho,'caminho arquivo') #Caminho arquivo
        
        if not os.path.exists(self.caminho):
            self.msg = f'Arquivo {self.caminho} não encontrado, Criando um novo arquivo...'

            #Definindo o caminho no config.ini
            self.config['caminho'] = {'caminho': self.caminho}

            with open(self.caminho,'w') as configfile:
                self.config.write(configfile)

        else:
            self.msg = f'Arquivo {self.caminho} encontrado, Carregando...'

            self.config.read(self.caminho)
    

    def retornar_config(self):
        return self.config, self.msg

