def ClassificaAluno ():
  if nota<7:
    print("REPROVADO")
  elif nota>=7 and nota<9.5 and faltas <=10:
    print("APROVADO")
  elif faltas<=10 and nota>=9.5:
    print("APROVADO COM LOUVOR")
  else:
    print("REPROVADO POR FALTAS")

nota= float(input())
faltas=int(input())


ClassificaAluno()