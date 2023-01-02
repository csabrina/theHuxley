dia= input();
precoDoProduto= float(input());
opcaoDoProduto= input();
nomeDoProduto= input();

if (dia=="seg" or dia=="ter" or dia=="qua"):
  if opcaoDoProduto== "ouro":
    print("O preco do produto {} no dia {} eh {:.2f}" .format(nomeDoProduto, dia, precoDoProduto/2));
  else:
     print("O preco do produto {} no dia {} eh {:.2f}" .format(nomeDoProduto, dia, precoDoProduto*2));
   
elif (dia=="qui" or dia=="sex"):
  if precoDoProduto > 10 and precoDoProduto < 100:
    print("O preco do produto {} no dia {} eh {:.2f}" .format(nomeDoProduto, dia, precoDoProduto/3));
  else:
     print("O preco do produto {} no dia {} eh {:.2f}" .format(nomeDoProduto, dia, precoDoProduto*2));
  
elif (dia=="sab"):
  if opcaoDoProduto=="prata":
    print("O preco do produto {} no dia {} eh {:.2f}" .format(nomeDoProduto, dia, precoDoProduto*3));
  else:
     print("O preco do produto {} no dia {} eh {:.2f}" .format(nomeDoProduto, dia, precoDoProduto*2));
  
else:
  print("O preco do produto {} no dia {} eh {:.2f}" .format(nomeDoProduto, dia, precoDoProduto*2));
