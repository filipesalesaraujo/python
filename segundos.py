segundos_total = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundos_total // 86400
resto = segundos_total % 86400

horas = resto // 3600
resto = resto % 3600

minutos = resto // 60
segundos = resto % 60

print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.")