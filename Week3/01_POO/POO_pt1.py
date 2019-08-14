class Carro:
	pass


meu_carro = Carro()
# meu_carro
# <__main__.Carro object at 0x000001FBB7E1C748>
carro_do_ime = Carro()
print(carro_do_ime)
# <__main__.Carro object at 0x000001FBB7DF6CF8>
meu_carro.ano = 1968
meu_carro.modelo = 'Fusca'
meu_carro.cor = 'azul'

print(meu_carro.ano)
# 1968
print(meu_carro.cor)
# 'azul'

carro_do_ime.ano = 1981
carro_do_ime.modelo = 'Brasília'
carro_do_ime.cor = 'amarelo'

print(carro_do_ime.modelo)
# 'Brasília'

print(meu_carro.modelo)
# 'Fusca'

novo_fusca = meu_carro

novo_fusca.ano += 10
print(novo_fusca.ano)
# 1978
print(meu_carro.ano)
# 1978
