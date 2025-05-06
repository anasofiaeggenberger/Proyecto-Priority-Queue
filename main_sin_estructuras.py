# PRIORITY QUEUE SIN ESTRUCTURAS - 3 PACIENTES POR URGENCIA

# ========================
# Variables por urgencia
# ========================

# Urgencia 1
paciente_u1_nombre_1 = ""
paciente_u1_presente_1 = False
paciente_u1_nombre_2 = ""
paciente_u1_presente_2 = False
paciente_u1_nombre_3 = ""
paciente_u1_presente_3 = False

# Urgencia 2
paciente_u2_nombre_1 = ""
paciente_u2_presente_1 = False
paciente_u2_nombre_2 = ""
paciente_u2_presente_2 = False
paciente_u2_nombre_3 = ""
paciente_u2_presente_3 = False

# Urgencia 3
paciente_u3_nombre_1 = ""
paciente_u3_presente_1 = False
paciente_u3_nombre_2 = ""
paciente_u3_presente_2 = False
paciente_u3_nombre_3 = ""
paciente_u3_presente_3 = False

# Urgencia 4
paciente_u4_nombre_1 = ""
paciente_u4_presente_1 = False
paciente_u4_nombre_2 = ""
paciente_u4_presente_2 = False
paciente_u4_nombre_3 = ""
paciente_u4_presente_3 = False

# Urgencia 5
paciente_u5_nombre_1 = ""
paciente_u5_presente_1 = False
paciente_u5_nombre_2 = ""
paciente_u5_presente_2 = False
paciente_u5_nombre_3 = ""
paciente_u5_presente_3 = False

# Estadisticas
conteo_u1 = 0
conteo_u2 = 0
conteo_u3 = 0
conteo_u4 = 0
conteo_u5 = 0
historial = ""

def insertar_paciente(nombre, urgencia):
    for i in range(1, 4):
        nombre_var = f"paciente_u{urgencia}_nombre_{i}"
        presente_var = f"paciente_u{urgencia}_presente_{i}"
        if not globals()[presente_var]:
            globals()[nombre_var] = nombre
            globals()[presente_var] = True
            print(f"✅ Paciente {nombre} agregado con urgencia {urgencia} (slot {i}).")
            return
    print(f"❌ Todos los espacios para urgencia {urgencia} están ocupados.")

def atender_paciente():
    global historial, conteo_u1, conteo_u2, conteo_u3, conteo_u4, conteo_u5
    for urgencia in range(1, 6):
        for i in range(1, 4):
            nombre_var = f"paciente_u{urgencia}_nombre_{i}"
            presente_var = f"paciente_u{urgencia}_presente_{i}"
            if globals()[presente_var]:
                nombre = globals()[nombre_var]
                print(f"🚑 Atendiendo a {nombre} (Urgencia {urgencia})")
                historial += f"{nombre} - Urgencia: {urgencia}\n"
                globals()[nombre_var] = ""
                globals()[presente_var] = False
                globals()[f"conteo_u{urgencia}"] += 1
                return
    print("⚠️ No hay pacientes en espera.")

def mostrar_cola():
    hay_pacientes = False
    print("\n📋 Pacientes en espera:")
    for urgencia in range(1, 6):
        for i in range(1, 4):
            nombre_var = f"paciente_u{urgencia}_nombre_{i}"
            presente_var = f"paciente_u{urgencia}_presente_{i}"
            if globals()[presente_var]:
                print(f" - {globals()[nombre_var]} (Urgencia {urgencia})")
                hay_pacientes = True
    if not hay_pacientes:
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
        print("\n=== PRIORITY QUEUE (sin estructuras, 3 pacientes por urgencia) ===")
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
            insertar_paciente(nombre, 1)
        elif opcion == "5":
            generar_reporte()
            print("👋 ¡Gracias por usar el sistema!")
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    menu()