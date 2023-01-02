escala= input();
temperatura= float(input());

if(escala=="C"):
  if(temperatura>= -273.0):
    f=(temperatura*1.8)+32;
    k=temperatura+273.15;
    print("{:.2f} F" .format(f));
    print("{:.2f} K" .format(k));
  else:
    print("Valor de temperatura abaixo do minimo");
    
elif(escala=="F"):
  if(temperatura>= -459,67):
    c=(temperatura-32)/1.8;
    k=(temperatura-32)*1.8+273.15;
    print("{:.2f} C" .format(c));
    print("{:.2f} K" .format(k));   
  else:
    print("Valor de temperatura abaixo do minimo");
    
elif(escala=="K"):
  if(temperatura>= 0.0):
    c=temperatura-273.15;
    f=(temperatura-273.15)*1.8+32;
    print("{:.2f} C" .format(c));
    print("{:.2f} F" .format(f));   
  else:
    print("Valor de temperatura abaixo do minimo");




    

    
    
  
