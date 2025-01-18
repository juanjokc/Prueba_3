from flask import render_template, request
from app import app
from app.funciones import calcular_estado, encontrar_nombre_mas_largo

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':

        notas = [int(request.form[f'nota{i+1}']) for i in range(3)]
        asistencia = int(request.form['asistencia'])

        promedio, estado = calcular_estado(notas, asistencia)
        return render_template('Ejercicio1.html', promedio=promedio, estado=estado)
    return render_template('Ejercicio1.html')

@app.route('/Ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':

        nombres = [request.form[f'nombre{i+1}'] for i in range(3)]

        nombre_largo, longitud = encontrar_nombre_mas_largo(nombres)
        return render_template('Ejercicio2.html', nombre_largo=nombre_largo, longitud=longitud)
    return render_template('Ejercicio2.html')