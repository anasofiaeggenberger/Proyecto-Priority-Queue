import random
from priority_queue import PriorityQueue

def simulacion_automatica():
    nombres = ["Ana", "José", "María", "Carlos", "Lucía", "Pedro", "Sofía", "Daniel"]
    pq = PriorityQueue()

    print("\n🔄 Simulación de llegada de pacientes...")

    for _ in range(10):
        nombre = random.choice(nombres)
        urgencia = random.randint(1, 5)
        pq.insertar_paciente(nombre, urgencia)

    pq.mostrar_cola()

    print("\n👩‍⚕️ Simulando atención médica...")

    while pq.cola:
        pq.atender_paciente()

    pq.generar_reporte()
