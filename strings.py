# Para trabalhar com strings no python basta colocar entre aspas simples ou duplas
exemplo_1 = 'String com aspas simples.'
exemplo_2 = 'String com aspas duplas.'
print(exemplo_1)
print(exemplo_2)

# Se quisermos escrever em várias linhas, utilizamos aspas triplas
exemplo_3 = """Ingredientes:
1. Ovos
2. Trigo
3. Fermento"""
print(exemplo_3)

# CARACTERES DE ESCAPE
print("Meu país é o: \nBrasil")  # (\n) Quebrar linha na string
print('Caixa D\'água')  # (\) ignora algo no python
# (\\) para escabar da barra que ignora
print('Arquivo localizo em: \\c:drive\\arquivo.py')
# Se quisermos saber quantos caracteres possuí uma string
selecao = "Brasil"
print(len(selecao))

# DESAFIO
desafio_1 = "Vamos codar!"
desafio_2 = "Vamos 'codar!'"
desafio_3 = "Vamos \n'codar'"
print(desafio_1)
print(desafio_2)
print(desafio_3)
