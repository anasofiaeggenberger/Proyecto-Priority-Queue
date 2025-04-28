import heapq
from paciente import Paciente

class PriorityQueue:
    def __init__(self):
        self.cola = []
        self.contador_llegada = 0

    def insertar_paciente(self, nombre, urgencia):
        paciente = Paciente(nombre, urgencia, self.contador_llegada)
        heapq.heappush(self.cola, paciente)
        self.contador_llegada += 1
        print(f"✅ Paciente {nombre} agregado con urgencia {urgencia}.")

    def atender_paciente(self):
        if self.cola:
            paciente = heapq.heappop(self.cola)
            print(f"🚑 Atendiendo a {paciente.nombre} (Urgencia {paciente.urgencia})")
            return paciente
        else:
            print("⚠️ No hay pacientes en la cola.")
            return None

    def mostrar_cola(self):
        if not self.cola:
            print("⚠️ No hay pacientes en espera.")
        else:
            print("\n📋 Pacientes en espera:")
            for paciente in sorted(self.cola):
                print(f" - {paciente}")
