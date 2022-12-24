# Precedência entre os operadores aritméticos
''' 
1- (n + n) -> Caso tenha essa situação (2 * ( 3 + 5 ) ), será resolvido de detro pra fora
2- **
3- *  /  //  % -> O que vier primeiro, da esquerda pra direita
4- +  - -> O que vier primeiro, da esquerda pra direita-> O que vier primeiro, da esquerda pra direita
'''

conta_1 = (1 + 1) ** (5 + 5)
print(conta_1)
