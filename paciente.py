import heapq

class Paciente:
    _contador = 0  # Para mantener orden de llegada

    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad
        self.orden = Paciente._contador
        Paciente._contador += 1

    def __lt__(self, otro):
        if self.prioridad == otro.prioridad:
            return self.orden < otro.orden
        return self.prioridad < otro.prioridad

    def __repr__(self):
        return f'{self.nombre} (Prioridad: {self.prioridad})'

# Cola global
cola_prioridad = []

def agregar_paciente(nombre, prioridad):
    heapq.heappush(cola_prioridad, Paciente(nombre, prioridad))

def obtener_pacientes_ordenados():
    return heapq.nsmallest(len(cola_prioridad), cola_prioridad)

def atender_paciente():
    if cola_prioridad:
        return heapq.heappop(cola_prioridad)
    return None
