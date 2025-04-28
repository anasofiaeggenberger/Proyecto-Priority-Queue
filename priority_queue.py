import heapq
from paciente import Paciente

class PriorityQueue:
    def __init__(self):
        self.cola = []
        self.contador_llegada = 0
        self.historial = []

    def insertar_paciente(self, nombre, urgencia):
        paciente = Paciente(nombre, urgencia, self.contador_llegada)
        heapq.heappush(self.cola, paciente)
        self.contador_llegada += 1
        print(f"✅ Paciente {nombre} agregado con urgencia {urgencia}.")

    def atender_paciente(self):
        if self.cola:
            paciente = heapq.heappop(self.cola)
            self.historial.append(paciente)
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

    def generar_reporte(self):
        if not self.historial:
            print("⚠️ No hay pacientes atendidos aún. No se puede generar reporte.")
            return

        with open("reporte_pacientes.txt", "w") as f:
            f.write("=== REPORTE DE PACIENTES ATENDIDOS ===\n\n")
            for paciente in self.historial:
                f.write(f"{paciente.nombre} - Urgencia: {paciente.urgencia}\n")

            # Estadísticas básicas
            f.write("\n=== ESTADÍSTICAS ===\n")
            niveles = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
            for paciente in self.historial:
                niveles[paciente.urgencia] += 1

            for nivel, cantidad in niveles.items():
                f.write(f"Pacientes de urgencia {nivel}: {cantidad}\n")

            total_pacientes = len(self.historial)
            urgentes = niveles[1] + niveles[2]
            porcentaje_urgentes = (urgentes / total_pacientes) * 100 if total_pacientes else 0

            f.write(f"\nTotal de pacientes atendidos: {total_pacientes}\n")
            f.write(f"Pacientes con urgencia alta (1 y 2): {urgentes} ({porcentaje_urgentes:.2f}%)\n")

        print("📄 Reporte generado exitosamente: reporte_pacientes.txt")
