meta=0;
cofrinho= float(input());
anterior=cofrinho;

for dia in range(6):
  valorDia= float(input());
  if valorDia>=anterior+0.50:
    meta+=1
  cofrinho+=valorDia
  anterior=valorDia


print("R$ {:.2f}" .format(cofrinho))
print(meta)
  
