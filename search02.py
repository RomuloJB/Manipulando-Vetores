a = [1, 3, 6, 9, 11, 17, 21, 22]

i = 0
f = len(a) - 1
n = int(input("NUmero: "))
found = False

while(i <= f):
    m = (i + f)//2
    if(a[m] == n):
        found = True
        break
    elif(n > a[m]):
        i = m + 1
        found = False
    else:
        f = m - 1
        found = f

if(found == False):
    print(f"{n} não está no vetor")

else:
    print(f"{n} foi encontrado na posição {m}")
