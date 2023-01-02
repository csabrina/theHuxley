taxaMaximaT= float(input());
audio= float(input());
dados= float(input());
capCanal= float(input());

qdMax = (taxaMaximaT*5.2 + audio*3.4 + dados*1.5)/capCanal;

print("{:.2f}" .format(qdMax));