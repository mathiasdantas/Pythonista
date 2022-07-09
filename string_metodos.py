# METODOS COMUNS NO PYTHON
nome_curso = '  Edição de vídeo   '
print(nome_curso.upper())  # Transforma a string em maiúscula
print(nome_curso.lower())  # Transforma a string em minúscula
# Remover os espaços em branco tanto da esquerda quanto da direita
print(nome_curso.strip())
print(nome_curso.lstrip())  # Remove os espaços em branco da parte esquerda
print(nome_curso.rstrip())  # Remove os espaços em branco da parte direita
print(nome_curso.find('ção'))  # Buscar uma informação dentro da string
# Substritui informações de 'vídeo' para 'música'
print(nome_curso.replace('vídeo', 'música'))
# Substritui informações de 'motos' para 'carros'
print('https://www.google.com.br/motos'.replace('motos', 'carros'))

# DESAFIO
# Através da criação de strings dinâmicos e os métodos de um string que acabou de aprender, use como base as variáveis a seguir para criar as seguintes frases:
a = 'é'
b = 'MELHOR'
c = 'QUE'
d = 'feito'
e = 'perfeito'
print('É melhor FEITO que PERFEITO')
print(f'{a.upper()} {b.lower()} {d.upper()} {c.lower()} {e.upper()}')
