from flask import Flask, render_template, request, redirect, url_for
from paciente import agregar_paciente, obtener_pacientes_ordenados, atender_paciente

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

if __name__ == '__main__':
    app.run(debug=True)
