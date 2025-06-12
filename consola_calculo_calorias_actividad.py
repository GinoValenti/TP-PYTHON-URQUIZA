import calculadora_indices as calc

print("=" * 50)
print(" CALORÍAS SEGÚN ACTIVIDAD FÍSICA ".center(50))
print("=" * 50)

try:
    peso = float(input("Ingrese su peso (kg): "))
    altura = float(input("Ingrese su altura (m): "))
    edad = int(input("Ingrese su edad (años): "))
    genero = input("Ingrese su género (M/F): ").strip().upper()

    if genero not in ['M', 'F']:
        raise ValueError("Género inválido. Use 'M' o 'F'.")

    print("\nNivel de actividad física:")
    print("1. Poco o ningún ejercicio")
    print("2. Ejercicio ligero (1–3 días/semana)")
    print("3. Ejercicio moderado (3–5 días/semana)")
    print("4. Deportista (6–7 días/semana)")
    print("5. Atleta (doble jornada)")
    nivel = input("Seleccione el nivel (1-5): ")

    valores = {'1': 1.2, '2': 1.375, '3': 1.55, '4': 1.72, '5': 1.9}
    if nivel not in valores:
        raise ValueError("Nivel de actividad inválido.")

    valor_genero = 5 if genero == "M" else -161
    valor_actividad = valores[nivel]

    calorias = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
    print(f"\nCalorías quemadas con actividad física: {calorias:.2f} cal/día")

except Exception as e:
    print(f"\n[ERROR] {e}")
