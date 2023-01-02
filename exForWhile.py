'''
num_notas= int(input("Quantas notas?"))

soma_notas=0 #variavel acumuladora de notas

for nota in range(num_notas):
    soma_notas += int(input("Nota: ")) #+= ta acumulando, mesma coisa de: soma_notas = soma_notas+input

print("A média das nota é: ", soma_notas/num_notas)

num= 0
while num <10: #enquanto num for menor q 10 imprime num e add +1
  print(num)
  num+=1
  '''

'''
soma_notas= 0; #acumula o somatorio das notas
qnt_notas= 0

while True: #começa com uma condicao ja verdadeira
    nota= int(input("Nota: "))
    if nota < 0:
      break #sai do laço
    soma_notas += nota
    qnt_notas +=1

media= soma_notas/qnt_notas

print("A média é:", media)

#ou

soma_notas= 0

nota = float(input("Nota: "))
qnt_notas = 0

while nota >=0:
  soma_notas += nota
  nota = float(input("Nota: "))
  qnt_notas += 1

media = soma_notas/qnt_notas

print("A média é:", media)
'''            

#excessoes em python

nome= input("Nome: ")

while True:
    try: #para tratar exessoes
      a= float(input("Altura: "))
      p= float(input("Peso: "))
      break #se chegar ao final da execucao do bloco que esta dentro do try e n ocorrer excessoes
    except ValueError:
      print("Valor de altura inválida! Digite um número!")

imc= p/(a**2)

print(nome, p, a, imc)
