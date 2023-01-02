unidadeEnergia= int(input());

if(unidadeEnergia<=99):
  total= unidadeEnergia*1.35;
  if(total>35):
    print("{:.2f}" .format(total));
    print(1.35);
  elif(total<=35):
    print("{:.2f}" .format(35));
    
elif(100<=unidadeEnergia<=299):
  total= unidadeEnergia*1.55; 
  print("{:.2f}" .format(total));
  print(1.55);
  
elif(300<=unidadeEnergia<=574):
  total= (unidadeEnergia*1.75)*1.1;
  print("{:.2f}" .format(total));
  print(1.75);
  
elif(unidadeEnergia>=575):
  total= (unidadeEnergia*2.15)*1.1;
  print("{:.2f}" .format(total));
  print(2.15);