# Programa 3: Índice de Masa Corporal (IMC)

peso = float(input("Ingresa tu peso (kg): "))
altura = float(input("Ingresa tu altura (m): "))

imc = peso / (altura ** 2)

print("Tu IMC es:", round(imc, 2))
