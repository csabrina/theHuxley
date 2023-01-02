cont=0;
total=0;
creBaixo=11; #7.2
temp= "";

while True:
   matricula=input(); #902
   if matricula=="999":
    break
     
   else:
    cre= float(input()) #6
    cont= cont+1;
    total= total+cre;
     
    if creBaixo > cre: #7.2 > 6
        creBaixo=cre;
        temp=matricula;
  
print(temp);
print("{:.2f}" .format(total/cont));