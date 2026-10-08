from collections import deque

class TicketManager:
    def __init__(self):
        # Estructura FIFO
        self.fila_normal = deque()
        self.fila_prioritaria = deque()
        
        # Estadísticas y estados
        self.total_atendidos = 0
        self.suma_tiempo_atendidos = 0
        self.ultimo_atendido = None

    def registrar_ticket(self, data):
        ticket = {
            "id": data.get("id"),
            "cliente": data.get("cliente"),
            "solicitante": data.get("solicitante"),
            "problema": data.get("problema"),
            "prioridad": data.get("prioridad"),
            "tiempo": int(data.get("tiempo", 0))
        }

        # FIFO: agregar al final de la cola correspondiente
        if ticket["prioridad"] == "Prioritaria":
            self.fila_prioritaria.append(ticket)
        else:
            self.fila_normal.append(ticket)

    def consultar_siguiente(self):
        if self.fila_prioritaria:
            return {"ticket": self.fila_prioritaria[0], "fila": "Prioritaria"}
        elif self.fila_normal:
            return {"ticket": self.fila_normal[0], "fila": "Normal"}
        return None

    def atender_siguiente(self):
        ticket = None
        # Principio de prioridad y FIFO
        if self.fila_prioritaria:
            ticket = self.fila_prioritaria.popleft()
        elif self.fila_normal:
            ticket = self.fila_normal.popleft()

        if ticket:
            self.total_atendidos += 1
            self.suma_tiempo_atendidos += ticket["tiempo"]
            self.ultimo_atendido = ticket

    def obtener_promedio_tiempo(self):
        if self.total_atendidos > 0:
            return round(self.suma_tiempo_atendidos / self.total_atendidos, 2)
        return 0