#Crie um vetor e armazene os números de 1 a 100. Cada número deve ocupar uma posição do vetor (lista). Obs. O vetor criado aqui será utilizado nos exercícios abaixo.

#Create an array capable of stocking numbers from 1 to 100. Each number must occupy a position on the array (list). This array (list) will be used for several cases.

lista = [0] * 100
for i in range(0, len(lista)):
    lista[i] = i + 1
#Mostre na tela todos os números do vetor em ordem crescente (1 a 100).
#Show on the screen all of the numbers in the array ordered ascending.
for i in range(0, len(lista)):
    print(lista[i])
#Mostre na tela todos os números do vetor em ordem decrescente (100 a 1).
#Show on the screen all of the numbers in the array ordered descending.
for i in range(len(lista)-1, -1, -1):
    print(lista[i])
#Mostre na tela o dobro de todos os números.
#Show on the screen all of the numbers multiplied by 2.
for i in range(0, len(lista)):
    print(lista[i] * 2)
#Apresente na tela a soma de todos os números.
#Show in the screen the sum of all the numbers.
soma = 0
for i in range(0, len(lista)):
    soma += lista[i]
print(f"\nA soma de todos os valores é igual a: {soma}\n")

#Apresente na tela a média geral dos valores contidos na lista.
#Show in the screen the general average of all the values in the list.
media = soma / len(lista)
print(f"\nA media aritmetica do vetor lista é: {media}\n")

#Mostre na tela a quantidade de números pares.
#Show in the screen the number of odd values in the list.
pares = 0
for i in range(0, len(lista)):
    if(lista[i] % 2 == 0):
        pares += 1
print(f"\nExistem {pares} numeros pares no vetor lista\n")
