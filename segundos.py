valor = int(input('Por favor, entre com o número de segundos que deseja converter:'))
dias = valor // 86400
horas = (valor % 86400) // 3600
minutos = ((valor % 86400) % 3600)//60
segundos =  ((valor % 86400) % 3600)%60
print('{} dias, {} horas, {} minutos e {} segundos.'.format(dias, horas, minutos, segundos))

