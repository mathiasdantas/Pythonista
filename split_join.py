# SPLIT AND JOIN
frase = 'Olá, bem-vindo a este treinamento!'
print(frase.split())
print(frase.split(','))
print(frase.split('-'))

nomes = 'Jhonatan, Rafael, Carol, Amanda, Jefferson'
print(nomes.split())
print(nomes.split(','))

hashtags = '#musica #guitar #gamer #coder #python'
print(hashtags.split())
print(hashtags.split('#'))
print(hashtags.split('#', 3))

# Como concatenar(combinar) strings
hashtag_separadas_por_espaco = hashtags.split(' ')
print(hashtag_separadas_por_espaco)
print(','.join(hashtag_separadas_por_espaco))
print('.'.join(hashtag_separadas_por_espaco))
print(' '.join(hashtag_separadas_por_espaco))

# DESAFIOS
# Desafio 1: Transforme a frase1 numa lista de palvras e guarde o resultado em uma variável chamada palavra1
# Desafio 2: Transforme a frase2 numa lista de palvras e guarde o resultado em uma variável chamada palavra2
# Desafio 3: Pegue a palavra1 e transforme elas na seguinte string: "Desafio,manipulação,de,strings". Imprima o resultado no console.
# Desafio 4: Pegue a palavra2 e transforme elas na seguinte string: frase2 = "jhonatan & rafael & carol & camilla". Imprima no console.

frase1 = 'Desafio manipulação de strings'
frase2 = 'jhonatan,rafael,carol,camilla'
palavra1 = frase1.split()
palavra2 = frase2.split(',')
print(','.join(palavra1))
print(' & '.join(palavra2))
