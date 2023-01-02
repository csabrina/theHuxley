salario= float(input());

if(salario<=280):
  total= salario*1.20;
  aumento= total-salario;
  print("{:.2f}\n20\n{:.2f}\n{:.2f}" .format(salario, aumento, total));
  
elif(280<salario<700):
  total= salario* 1.15;
  aumento= total-salario;
  print("{:.2f}\n15\n{:.2f}\n{:.2f}" .format(salario, aumento, total));
    
elif(700<salario<1500):
  total= salario*1.10;
  aumento= total-salario;
  print("{:.2f}\n10\n{:.2f}\n{:.2f}" .format(salario, aumento, total));
    
elif(salario>=1500):
  total= salario*1.05;
  aumento= total-salario;
  print("{:.2f}\n5\n{:.2f}\n{:.2f}" .format(salario, aumento, total));

