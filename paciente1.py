class Paciente:
    def __init__(self, nombre, urgencia, llegada):
        self.nombre = nombre
        self.urgencia = urgencia
        self.llegada = llegada  # Número autoincremental (para orden de llegada)

    def __lt__(self, otro):
        if self.urgencia != otro.urgencia:
            return self.urgencia < otro.urgencia
        return self.llegada < otro.llegada

    def __str__(self):
        return f"{self.nombre} (Urgencia: {self.urgencia})"
