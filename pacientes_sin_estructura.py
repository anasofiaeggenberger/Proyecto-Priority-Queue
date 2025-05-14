# Variables globales
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
    global historial

    if urgencia == 1 and not paciente_u1_presente:
        paciente_u1_nombre = nombre
        paciente_u1_presente = True
        print(f"Paciente {nombre} agregado con urgencia 1.")
    elif urgencia == 2 and not paciente_u2_presente:
        paciente_u2_nombre = nombre
        paciente_u2_presente = True
        print(f"Paciente {nombre} agregado con urgencia 2.")
    elif urgencia == 3 and not paciente_u3_presente:
        paciente_u3_nombre = nombre
        paciente_u3_presente = True
        print(f"Paciente {nombre} agregado con urgencia 3.")
    elif urgencia == 4 and not paciente_u4_presente:
        paciente_u4_nombre = nombre
        paciente_u4_presente = True
        print(f"Paciente {nombre} agregado con urgencia 4.")
    elif urgencia == 5 and not paciente_u5_presente:
        paciente_u5_nombre = nombre
        paciente_u5_presente = True
        print(f"Paciente {nombre} agregado con urgencia 5.")
    else:
        print(f"No se pudo agregar a {nombre}. Ya hay un paciente en urgencia {urgencia}.")

def atender_paciente():
    global paciente_u1_nombre, paciente_u1_presente, conteo_u1
    global paciente_u2_nombre, paciente_u2_presente, conteo_u2
    global paciente_u3_nombre, paciente_u3_presente, conteo_u3
    global paciente_u4_nombre, paciente_u4_presente, conteo_u4
    global paciente_u5_nombre, paciente_u5_presente, conteo_u5
    global historial

    if paciente_u1_presente:
        print(f"Paciente atendido: {paciente_u1_nombre} (urgencia 1)")
        historial += f"{paciente_u1_nombre} (urgencia 1)\n"
        conteo_u1 += 1
        paciente_u1_nombre = ""
        paciente_u1_presente = False
    elif paciente_u2_presente:
        print(f"Paciente atendido: {paciente_u2_nombre} (urgencia 2)")
        historial += f"{paciente_u2_nombre} (urgencia 2)\n"
        conteo_u2 += 1
        paciente_u2_nombre = ""
        paciente_u2_presente = False
    elif paciente_u3_presente:
        print(f"Paciente atendido: {paciente_u3_nombre} (urgencia 3)")
        historial += f"{paciente_u3_nombre} (urgencia 3)\n"
        conteo_u3 += 1
        paciente_u3_nombre = ""
        paciente_u3_presente = False
    elif paciente_u4_presente:
        print(f"Paciente atendido: {paciente_u4_nombre} (urgencia 4)")
        historial += f"{paciente_u4_nombre} (urgencia 4)\n"
        conteo_u4 += 1
        paciente_u4_nombre = ""
        paciente_u4_presente = False
    elif paciente_u5_presente:
        print(f"Paciente atendido: {paciente_u5_nombre} (urgencia 5)")
        historial += f"{paciente_u5_nombre} (urgencia 5)\n"
        conteo_u5 += 1
        paciente_u5_nombre = ""
        paciente_u5_presente = False
    else:
        print("No hay pacientes en la cola.")

def mostrar_cola():
    print("=== COLA DE PACIENTES ===")
    if paciente_u1_presente:
        print(f"1. {paciente_u1_nombre} (urgencia 1)")
    if paciente_u2_presente:
        print(f"2. {paciente_u2_nombre} (urgencia 2)")
    if paciente_u3_presente:
        print(f"3. {paciente_u3_nombre} (urgencia 3)")
    if paciente_u4_presente:
        print(f"4. {paciente_u4_nombre} (urgencia 4)")
    if paciente_u5_presente:
        print(f"5. {paciente_u5_nombre} (urgencia 5)")
    if not (paciente_u1_presente or paciente_u2_presente or paciente_u3_presente or paciente_u4_presente or paciente_u5_presente):
        print("La cola está vacía.")
    print("==========================")
