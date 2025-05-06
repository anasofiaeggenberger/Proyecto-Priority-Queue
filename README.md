# INFORME FINAL - Proyecto "Priority Queue en Hospital"
Integrantes: Ana Sofía Eggenberger, Jan Ricica 

**Clase:** Estructura de Datos

**Tema:** Implementación de priority queue para hospital

**Descripción del proyecto:** Se desarrolló un sistema de simulación para la administración de pacientes en un hospital utilizando la estructura de datos Priority Queue. 
Cada paciente es ingresado con un nivel de urgencia del 1 al 5, donde 1 representa la máxima prioridad médica.

_Funciones principales:_
1. Registro de pacientes con urgencia asignada.
2. Atención de pacientes según nivel de urgencia y orden de llegada.
3. Visualización en tiempo real de la cola de espera.
4. Inserción inmediata de pacientes de emergencia (código rojo).
5. Simulación automática de llegadas y atención de pacientes.
6. Generación automática de un reporte en .txt con historial y estadísticas.

_Estructura del Proyecto:_
1. paciente.py: Clase paciente (datos y métodos de comparación).
2. priority_queue.py: Manejo de la cola de prioridad.
3. utils.py: Funciones de validación y colores en consola.
4. simulacion.py: Simulación automática de flujo hospitalario.
5. main.py: Menú principal del sistema.

_Resultados destacados:_
1. El sistema prioriza correctamente la atención de pacientes más urgentes.
2. La simulación automática permitió probar el sistema en escenarios variados.
3. Se logró generar reportes automáticos de pacientes atendidos con estadísticas por nivel de urgencia.

**Conclusión:** El uso de Priority Queue permite optimizar los tiempos de respuesta en situaciones críticas de atención médica, asegurando que los pacientes más urgentes sean tratados primero. 
El proyecto también refleja el uso adecuado de programación modular en Python y promueve buenas prácticas como separación de responsabilidades, validación de datos, y generación de reportes.
