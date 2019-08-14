class Carro:
    def __init__(self, modelo, ano, cor): # instancia com atributos como parametro
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

carro_do_meu_avo = Carro('Ferrari', 1980, 'vermelha')

print(carro_do_meu_avo.cor)

