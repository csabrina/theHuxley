qntPessoas= int(input());
cidade= input();
qntQuartos= int(input());

if (cidade.lower() == "pipa"):
  if (qntQuartos == 4):
    valorTotal = (qntPessoas * 75) + 600;
    valorUnitario = valorTotal / qntPessoas;
  else:
      valorTotal = (qntPessoas * 75) + 900;
      valorUnitario = valorTotal / qntPessoas;
    
else:
    if qntQuartos == 3:
        valorTotal = (qntPessoas * 60) + 950;
        valorUnitario = valorTotal / qntPessoas;
    else:
        valorTotal = (qntPessoas * 60) + 1120;
        valorUnitario = valorTotal / qntPessoas;

print("{:.2f}" .format(valorTotal));
print("{:.2f}" .format(valorUnitario));
    