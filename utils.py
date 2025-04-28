from colorama import Fore, Style

def imprimir_coloreado(texto, urgencia):
    if urgencia == 1:
        color = Fore.RED
    elif urgencia == 2:
        color = Fore.MAGENTA
    elif urgencia == 3:
        color = Fore.YELLOW
    elif urgencia == 4:
        color = Fore.CYAN
    else:
        color = Fore.GREEN

    print(color + texto + Style.RESET_ALL)

def validar_urgencia(urgencia):
    try:
        urgencia = int(urgencia)
        if 1 <= urgencia <= 5:
            return urgencia
        else:
            print("❌ Urgencia debe ser un número entre 1 y 5.")
            return None
    except ValueError:
        print("❌ Entrada inválida. Debe ser un número.")
        return None
