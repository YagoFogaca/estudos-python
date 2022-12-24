# Formatação de strings com o método format
# Aqui temos os conceitos de argumentos e parametros
# Parametros:
# - Nomeados: Como no exemplo da linha 6, onde passamos o seu nome
# - Não nomeados: Pratamos por index

# Argumentos:
# São os valores do parametros

# Exemplo de argumentos e parametros:
# def func( a, x): Aqui temos os Parametros
# func(1, 2) Aqui temos os argumentos

a = 'A'
b = 'B'
c = 1.1
formato = 'a={parametro_a} b={parametro_b} c={parametro_c:.2f}'.format(
    parametro_a=a,
    parametro_b=b,
    parametro_c=c
)

print(10*20)

print(formato)
