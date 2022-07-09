# STRING DINÂMICO
nome = "Mathias Sammer"
email = "teste@gmail.com"
# Para utilizar uma string dinâmica basta inserimos (f'') e passando a variável entre chaves {}.
print(f'Olá {nome}, recebemos seu cadastro com o seguinte email: {email}.\nVocê confirma essa informação?')

# DESAFIO 1
# Crie a seguinte string dinâmica
nome = 'Carol'
hobby = 'ouvir música'
print(f'Olá sou a {nome} e gosto de {hobby}')

# DESAFIO 2
# Monte a seguinte frase, usando as sílabas como base
b = 'ba'
parte2 = 'nica'
a = 'a'
r = 'ri'
parte1 = 'eletrô'
t = 'te'
print(f'{b}{t}{r}{a} {parte1}{parte2}')
