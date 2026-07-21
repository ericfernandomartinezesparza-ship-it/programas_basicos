# Programa 4: Salario neto

salario_bruto = float(input("Ingresa el salario bruto: "))
impuestos = float(input("Porcentaje de impuestos (%): "))
deducciones = float(input("Monto de deducciones: "))

impuesto = salario_bruto * (impuestos / 100)
salario_neto = salario_bruto - impuesto - deducciones

print("Salario neto:", salario_neto)
