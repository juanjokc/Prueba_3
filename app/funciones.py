def calcular_estado(notas, asistencia):
    promedio = sum(notas) / len(notas)

    if promedio >= 40 and asistencia >= 75:
        estado = "Aprobado"
    else:
        estado = "Reprobado"

    return promedio, estado

def encontrar_nombre_mas_largo(nombres):
    nombre_largo = max(nombres, key=len)
    return nombre_largo, len(nombre_largo)