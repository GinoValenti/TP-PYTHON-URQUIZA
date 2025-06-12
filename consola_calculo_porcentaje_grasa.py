import calculadora_indices as calc

print("=" * 50)
print(" CALCULO DE PORCENTAJE DE GRASA CORPORAL ".center(50))
print("=" * 50)

try:
    peso = float(input("Ingrese su peso (kg): "))
    altura = float(input("Ingrese su altura (m): "))
    edad = int(input("Ingrese su edad (años): "))
    genero = input("Ingrese su género (M/F): ").strip().upper()

    if genero not in ['M', 'F']:
        raise ValueError("Género inválido. Use 'M' o 'F'.")

    valor_genero = 10.8 if genero == "M" else 0

    porcentaje = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
    print(f"\nPorcentaje de grasa corporal estimado: {porcentaje:.2f}%")

except Exception as e:
    print(f"\n[ERROR] {e}")
