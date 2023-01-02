number1= int(input());
number2= int(input());

soma=0;

if number1 >= number2:
  maior= number1;
  menor= number2;

else:
  maior= number2;
  menor= number1;

if menor<0:
   menor=0;

for n in range(menor, maior+1):
  soma+=n;

print(soma);
