
# Usamos o sep para dizer a função print qual é o separador que queremos
# Por padrão o python usa o espaço
# Usamos o end para dizer se a função deve quebrar linha ou não
# No exemplo podemos ver isso acontecendo na pratica:
print(1 , 'olá', 21, sep='---', end='-x-\r\n') # Coloca o -x- ao final da linha e quebra ela com o comando \r\n
print(2 , 'tchau', 12, sep='---', end='\r\n') # Somente quebra a linha, esse é o padrão da função
print(2 , 'tchau', 12, sep='---', end='-x--x-') # Adiciona o -x--x- no final e NÂO quebra a linha
print('teste')
# O resultado no terminal é:
"""
    1---olá---21-x-
    2---tchau---12
    2---tchau---12-x--x-teste
"""