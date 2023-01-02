temperatura= float(input());
secrecao= input();

if secrecao=="S" or secrecao=="N":
  if temperatura >= 37 and secrecao=="S":
      print("Exames Especiais");
  elif temperatura >= 37 and secrecao=="N":
      print("Exames Basicos");
  elif temperatura < 37 and secrecao=="N":
      print("Liberado");
  elif temperatura < 37 and secrecao=="S":
      print("Exames Basicos");

else:
  print("Erro");