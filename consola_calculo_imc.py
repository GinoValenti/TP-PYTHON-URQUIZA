# consola_calculo_imc.py
import calculadora_indices as calc

try:
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = calc.calcular_IMC(peso, altura)
    print(f"Su IMC es: {imc:.2f}")
except Exception as e:
    print(e)
