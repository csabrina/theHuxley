matriz = []

soma = 0
delta = 0
somaFDiag = 0
positivos = 0

for i in range(3):
    matriz.append([int(input()), int(input()), int(input())])

menor = matriz[0][0]

for x in range(3):
  
    for j in range(3):
      
        if matriz[x][j] > 0:
            positivos +=1
            soma += matriz[x][j]
          
        if matriz[x][j] < menor:
            menor = matriz[x][j]
          
        if menor % 2 == 0:
            delta = 1
          
        else:
            delta = 0
          
        if x != j:
            somaFDiag += matriz[x][j]
          
print("{:.2f} {} {} {}".format(soma/positivos, menor, delta, somaFDiag))