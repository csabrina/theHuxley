total=0

while True:
  n= float(input())
  if n>0:
    total+=n
  else:
    break

print("Lojas Tabajara")
print("Total: {:.2f}" .format(total))

dinheiro= float(input())
troco= dinheiro-total

print("Dinheiro: R$ {:.2f}" .format(dinheiro))
print("Troco: R$ {:.2f}" .format(troco))
