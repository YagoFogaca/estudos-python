# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool

print('a' + 'b') # concatenação == juntar

print(1 + 2) # somar os valores

# print('2' + 1) # Vai gerar um error ao executar

print(int('1') + 1) # converte de str para int e depois executa a soma

print(type(bool('true'))) # converte de str para bool 

print(float('1.9') + 2.2) # converte de str para float e depois executa a soma

print(float('1') + 1) # converte de str para float e depois executa a soma ** Aqui podemos observar que ao executar esse código o que será impresso será do tipo float, mesmo que o tipo foi é do tipo float

print(str(11) + 'b') # converte de int para str e realizar a concatenação