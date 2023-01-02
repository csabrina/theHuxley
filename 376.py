livros= int(input());
alunos= int(input());

regra= alunos/livros;

if (regra <= 8):
  print("A");
  
elif (regra <= 12):
  print("B");
  
elif (regra <= 18):
  print("C");
  
else:
  print("D");
