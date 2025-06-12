import calculadora_indices as calc

print("=" * 50)
print(" CALORÍAS RECOMENDADAS PARA ADELGAZAR ".center(50))
print("=" * 50)

try:
    peso = float(input("Ingrese su peso (kg): "))
    altura = float(input("Ingrese su altura (m): "))
    edad = int(input("Ingrese su edad (años): "))
    genero = input("Ingrese su género (M/F): ").strip().upper()

    if genero not in ['M', 'F']:
        raise ValueError("Género inválido. Use 'M' o 'F'.")

    valor_genero = 5 if genero == "M" else -161

    resultado = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
    print(f"\n{resultado}")

except Exception as e:
    print(f"\n[ERROR] {e}")
