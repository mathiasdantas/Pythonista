# Método Slice da String
# Podemos acessar caracter por meio do índice
teclado = 'Teclado'
print(teclado[-1])

# Podemos pegar o índice de um caracter
indice = teclado.index('a')
print(teclado[indice])
print(indice)

# Acessando partes de uma string
link = 'https://programacao.com/python'
print(link[0])
print(link[-1])
print(link[0:5])
print(link[0:])
print(link[-5:])
print(link[5:])
print(link[:-5])

# Podemos pegar um caracter repetido
fruta = 'banana'
print(teclado.rindex('a'))

# DESAFIO 1
# Encontre o índice de 'o' dentro da variável biblioteca
biblioteca = 'Biblioteca'
print(biblioteca.index('o'))

# DESAFIO 2
# Usando a frase - imprima apenas 'De Aplicações'
frase = 'Desenvolvimento De Aplicações'
index_d = frase.rindex('D')
index_s = frase.rindex('s')
print(frase[index_d:index_s+1])
print(frase[-13:])
print(frase[16:])
