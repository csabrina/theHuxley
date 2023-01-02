salario= float(input());
valorComprometido = float(input());

disponivel= salario-valorComprometido;
valorMax= disponivel - (salario*0.7);

if (valorMax < 0):
    print("0.00");
if (valorMax > 0):
    print("{:.2f}".format(valorMax));