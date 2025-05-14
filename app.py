from flask import Flask, render_template, request, redirect, url_for
from paciente import agregar_paciente, obtener_pacientes_ordenados, atender_paciente, eliminar_paciente

app = Flask(__name__)

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
    # Handle the case where no name is provided
    return redirect(url_for('index'))

@app.route('/eliminar/<nombre>', methods=['GET', 'POST'])
def eliminar(nombre):
    if eliminar_paciente(nombre):  # Ensure the function returns True if deletion is successful
        print(f"Paciente {nombre} eliminado definitivamente.")
    else:
        print(f"No se pudo eliminar al paciente {nombre}.")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
