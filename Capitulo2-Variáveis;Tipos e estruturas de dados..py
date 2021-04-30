#Exercícios Cap02 (dsa)

#Ex 1 -- Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números -- 

Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (Lista)

#Ex 2 -- Crie uma lista de 5 objetos e imprima na tela  --

Lista = ['Caneta', 'Borracha', 'Lapis', 'Branquinho', 'Tesoura']
print (Lista)

#Ex 3 -- Crie duas strings e concatene as duas em uma terceira string  --

Frase1 = 'História'
Frase2 = ' e Matemática'
s = Frase1 + Frase2
print (s)

#Ex 4 -- Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla -- 

Tupla1 = (1,2,2,3,4,4,4,5)
count = Tupla1.count(4)
print ('Quantas vezes o 4 aparece:', count)

#Ex 5 -- Crie um dicionário vazio e imprima na tela -- 
Dic = {}
print (Dic)

#Ex 6 -- Crie um dicionário com 3 chaves e 3 valores e imprima na tela --
Dic1 = {'Bianca':20, 'Tatiane':30, 'Eduarda':19}
print (Dic1)

#Ex7 -- Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela --
Dic1 = {'Bianca':20, 'Tatiane':30, 'Eduarda':19, 'Celso':58}
print (Dic1)

#Ex8 -- Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela. -- 
Dic1 = {'Chave1':'Algebra', 'Chave2':'Historia', 'Chave3':[10,10]}
print(Dic1)

#Ex9 -- Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela. -- 
Lista = ['Bianca', (15,12), {'Sul':0, 'Norte':30}, 15.14]
print (Lista)

#Ex10 -- Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais legal do século XXI' 
frase = ('Cientista de Dados é o profissional mais legal do século XXI')
print (frase [0:18])