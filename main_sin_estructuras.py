paciente_u1_nombre = ""
paciente_u1_presente = False

paciente_u2_nombre = ""
paciente_u2_presente = False

paciente_u3_nombre = ""
paciente_u3_presente = False

paciente_u4_nombre = ""
paciente_u4_presente = False

paciente_u5_nombre = ""
paciente_u5_presente = False

conteo_u1 = 0
conteo_u2 = 0
conteo_u3 = 0
conteo_u4 = 0
conteo_u5 = 0

historial = ""

def insertar_paciente(nombre, urgencia):
    global paciente_u1_nombre, paciente_u1_presente
    global paciente_u2_nombre, paciente_u2_presente
    global paciente_u3_nombre, paciente_u3_presente
    global paciente_u4_nombre, paciente_u4_presente
    global paciente_u5_nombre, paciente_u5_presente

    if urgencia == 1 and not paciente_u1_presente:
        paciente_u1_nombre = nombre
        paciente_u1_presente = True
        print(f"✅ Paciente {nombre} agregado con urgencia 1.")
    elif urgencia == 2 and not paciente_u2_presente:
        paciente_u2_nombre = nombre
        paciente_u2_presente = True
        print(f"✅ Paciente {nombre} agregado con urgencia 2.")
    elif urgencia == 3 and not paciente_u3_presente:
        paciente_u3_nombre = nombre
        paciente_u3_presente = True
        print(f"✅ Paciente {nombre} agregado con urgencia 3.")
    elif urgencia == 4 and not paciente_u4_presente:
        paciente_u4_nombre = nombre
        paciente_u4_presente = True
        print(f"✅ Paciente {nombre} agregado con urgencia 4.")
    elif urgencia == 5 and not paciente_u5_presente:
        paciente_u5_nombre = nombre
        paciente_u5_presente = True
        print(f"✅ Paciente {nombre} agregado con urgencia 5.")
    else:
        print(f"❌ Ya hay un paciente en urgencia {urgencia}. No se puede agregar otro.")

def atender_paciente():
    global paciente_u1_nombre, paciente_u1_presente
    global paciente_u2_nombre, paciente_u2_presente
    global paciente_u3_nombre, paciente_u3_presente
    global paciente_u4_nombre, paciente_u4_presente
    global paciente_u5_nombre, paciente_u5_presente
    global historial, conteo_u1, conteo_u2, conteo_u3, conteo_u4, conteo_u5

    if paciente_u1_presente:
        print(f"🚑 Atendiendo a {paciente_u1_nombre} (Urgencia 1)")
        historial += f"{paciente_u1_nombre} - Urgencia: 1\n"
        conteo_u1 += 1
        paciente_u1_nombre = ""
        paciente_u1_presente = False
    elif paciente_u2_presente:
        print(f"🚑 Atendiendo a {paciente_u2_nombre} (Urgencia 2)")
        historial += f"{paciente_u2_nombre} - Urgencia: 2\n"
        conteo_u2 += 1
        paciente_u2_nombre = ""
        paciente_u2_presente = False
    elif paciente_u3_presente:
        print(f"🚑 Atendiendo a {paciente_u3_nombre} (Urgencia 3)")
        historial += f"{paciente_u3_nombre} - Urgencia: 3\n"
        conteo_u3 += 1
        paciente_u3_nombre = ""
        paciente_u3_presente = False
    elif paciente_u4_presente:
        print(f"🚑 Atendiendo a {paciente_u4_nombre} (Urgencia 4)")
        historial += f"{paciente_u4_nombre} - Urgencia: 4\n"
        conteo_u4 += 1
        paciente_u4_nombre = ""
        paciente_u4_presente = False
    elif paciente_u5_presente:
        print(f"🚑 Atendiendo a {paciente_u5_nombre} (Urgencia 5)")
        historial += f"{paciente_u5_nombre} - Urgencia: 5\n"
        conteo_u5 += 1
        paciente_u5_nombre = ""
        paciente_u5_presente = False
    else:
        print("⚠️ No hay pacientes en espera.")

def mostrar_cola():
    print("\n📋 Pacientes en espera:")
    if paciente_u1_presente:
        print(f" - {paciente_u1_nombre} (Urgencia 1)")
    if paciente_u2_presente:
        print(f" - {paciente_u2_nombre} (Urgencia 2)")
    if paciente_u3_presente:
        print(f" - {paciente_u3_nombre} (Urgencia 3)")
    if paciente_u4_presente:
        print(f" - {paciente_u4_nombre} (Urgencia 4)")
    if paciente_u5_presente:
        print(f" - {paciente_u5_nombre} (Urgencia 5)")

    if not any([
        paciente_u1_presente, paciente_u2_presente, paciente_u3_presente,
        paciente_u4_presente, paciente_u5_presente
    ]):
        print(" - Ningún paciente registrado.")

def generar_reporte():
    total = conteo_u1 + conteo_u2 + conteo_u3 + conteo_u4 + conteo_u5
    urgentes = conteo_u1 + conteo_u2
    porcentaje = (urgentes / total * 100) if total else 0

    with open("reporte_sin_estructuras.txt", "w") as f:
        f.write("=== REPORTE DE PACIENTES ATENDIDOS ===\n\n")
        f.write(historial)
        f.write("\n=== ESTADÍSTICAS ===\n")
        f.write(f"Urgencia 1: {conteo_u1}\n")
        f.write(f"Urgencia 2: {conteo_u2}\n")
        f.write(f"Urgencia 3: {conteo_u3}\n")
        f.write(f"Urgencia 4: {conteo_u4}\n")
        f.write(f"Urgencia 5: {conteo_u5}\n")
        f.write(f"\nTotal atendidos: {total}\n")
        f.write(f"Pacientes urgentes (1 y 2): {urgentes} ({porcentaje:.2f}%)\n")

    print("📄 Reporte generado: reporte_sin_estructuras.txt")

def menu():
    while True:
        print("\n=== PRIORITY QUEUE (sin estructuras) ===")
        print("1. Registrar nuevo paciente")
        print("2. Atender siguiente paciente")
        print("3. Ver cola de pacientes")
        print("4. Emergencia crítica")
        print("5. Generar reporte y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del paciente: ")
            try:
                urgencia = int(input("Urgencia (1 a 5): "))
                if 1 <= urgencia <= 5:
                    insertar_paciente(nombre, urgencia)
                else:
                    print("❌ Urgencia fuera de rango.")
            except ValueError:
                print("❌ Entrada inválida.")
        elif opcion == "2":
            atender_paciente()
        elif opcion == "3":
            mostrar_cola()
        elif opcion == "4":
            nombre = input("Nombre del paciente de emergencia: ")
            insertar_paciente(nombre, 1)  # Emergencia = urgencia 1
        elif opcion == "5":
            generar_reporte()
            print("👋 ¡Gracias por usar el sistema!")
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    menu()

