
def calcular_IMC(peso, altura):
    try:
        if altura <= 0:
            raise ValueError("La altura debe ser mayor a cero.")
        return peso / (altura ** 2)
    except Exception as e:
        raise ValueError(f"Error al calcular IMC: {e}")


def calcular_porcentaje_grasa(peso, altura, edad, valor_genero):
    try:
        imc = calcular_IMC(peso, altura)
        return 1.2 * imc + 0.23 * edad - 5.4 - valor_genero
    except Exception as e:
        raise ValueError(f"Error al calcular %GC: {e}")


def calcular_calorias_en_reposo(peso, altura, edad, valor_genero):
    try:
        return (10 * peso) + (6.25 * altura * 100) - (5 * edad) + valor_genero
    except Exception as e:
        raise ValueError(f"Error al calcular calorías en reposo: {e}")


def calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad):
    try:
        tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
        return tmb * valor_actividad
    except Exception as e:
        raise ValueError(f"Error al calcular calorías con actividad: {e}")


def consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero):
    try:
        tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
        rango_inferior = tmb * 0.80
        rango_superior = tmb * 0.85
        return f"Para adelgazar es recomendado que consumas entre: {int(rango_inferior)} y {int(rango_superior)} calorías al día."
    except Exception as e:
        raise ValueError(f"Error al calcular consumo para adelgazar: {e}")
