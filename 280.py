nomeVendedor=(input());
salarioFixo= float(input());
vendasEfetudas= float(input());

salarioFinal=(vendasEfetudas*0.15)+salarioFixo;

print("TOTAL = R$ {:.2f}" .format(salarioFinal));