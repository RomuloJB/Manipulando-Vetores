#exemplo de vetor
#Array example
a = [1, 3, 4, 8, 9, 10, 15, 16, 20, 45, 99, 99]

n = int(input("Digite um numero para ver se ele existe no vetor a: ")) #Type a number to see if it's part of the array

found = -1
for i in range(0, len(a)):
    if(a[i] == n):
        found = i
        break

if(found == -1):
    print(f"{n} Não foi encontrado no vetor") #The number typed wasn't found in the array

else:
    print(f"O numero {n} existe dentro do vetor a, e está na posição {i}") #The number typed is part of the array and it's located at the position {i}
