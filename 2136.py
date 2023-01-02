espaco= input();
pmalas= input();
valor= float(input());
motor=float(input());
cambio=input();

if (espaco == "A"):
    if (pmalas == "G"):
        if (valor < 100000 and motor >= 1.5 and cambio == "A"):
          print("Pode comprar!");
        elif (valor < 100000 and motor >= 1.5 and cambio == "M"):
          print("Boa compra.");
        elif (valor < 100000 and motor < 1.5 and cambio == "A"):
          print("Boa compra.");
        elif (valor > 100000 and motor >= 1.5 and cambio == "A"):
          print("Boa compra.");
        elif (valor < 100000 and motor < 1.5 and cambio != "A"):
          print("Pode ser uma op��o.");
        elif (valor > 100000 and motor >= 1.5 and cambio != "A"):
          print("Pode ser uma op��o.");
        elif (valor > 100000 and motor < 1.5 and cambio == "A"):
          print("Pode ser uma op��o.");
    else:
        print("N�o compre!");
else:
    print("N�o compre!");