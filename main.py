from priority_queue import PriorityQueue
from utils import imprimir_coloreado, validar_urgencia
from simulacion import simulacion_automatica

def menu():
    pq = PriorityQueue()

    while True:
        print("\n=== 🏥 HOSPITAL - SISTEMA DE PRIORIDADES ===")
        print("1. Registrar nuevo paciente")
        print("2. Atender siguiente paciente")
        print("3. Ver cola de pacientes")
        print("4. Simulación automática")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Nombre del paciente: ")
            urgencia_input = input("Nivel de urgencia (1=Máxima urgencia, 5=Menor urgencia): ")
            urgencia = validar_urgencia(urgencia_input)
            if urgencia:
                pq.insertar_paciente(nombre, urgencia)
        elif opcion == '2':
            pq.atender_paciente()
        elif opcion == '3':
            pq.mostrar_cola()
        elif opcion == '4':
            simulacion_automatica()
        elif opcion == '5':
            print("👋 Saliendo del sistema. ¡Gracias!")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
