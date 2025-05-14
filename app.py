from flask import Flask, render_template, request, redirect, url_for
from paciente import agregar_paciente, obtener_pacientes_ordenados, atender_paciente, eliminar_paciente
from pacientes_sin_estructura import insertar_paciente as sin_insertar, atender_paciente as sin_atender, mostrar_cola

import sys
from io import StringIO

app = Flask(__name__)

# --- Sistema con estructuras ---

@app.route('/')
def index():
    pacientes = obtener_pacientes_ordenados()
    return render_template('index.html', pacientes=pacientes)

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    prioridad = int(request.form['prioridad'])
    agregar_paciente(nombre, prioridad)
    return redirect(url_for('index'))

@app.route('/atender', methods=['POST'])
def atender():
    atender_paciente()
    return redirect(url_for('index'))

@app.route('/eliminar/', methods=['GET', 'POST'])
def eliminar_default():
    return redirect(url_for('index'))

@app.route('/eliminar/<nombre>', methods=['GET', 'POST'])
def eliminar(nombre):
    if eliminar_paciente(nombre):
        print(f"Paciente {nombre} eliminado definitivamente.")
    else:
        print(f"No se pudo eliminar al paciente {nombre}.")
    return redirect(url_for('index'))

# --- Sistema sin estructuras ---

@app.route('/sinestructura')
def sinestructura():
    # Captura la salida impresa de mostrar_cola()
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    mostrar_cola()
    sys.stdout = old_stdout
    salida = mystdout.getvalue()
    return render_template('sinestructura.html', salida=salida, reporte=None)

@app.route('/sinestructura/agregar', methods=['POST'])
def sinestructura_agregar():
    nombre = request.form['nombre']
    urgencia = int(request.form['urgencia'])
    sin_insertar(nombre, urgencia)
    return redirect(url_for('sinestructura'))

@app.route('/sinestructura/atender', methods=['POST'])
def sinestructura_atender():
    sin_atender()
    return redirect(url_for('sinestructura'))


if __name__ == '__main__':
    app.run(debug=True)
