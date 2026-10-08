from flask import Flask, render_template, request, redirect, url_for
from backend.ticket_manager import TicketManager

app = Flask(__name__)
manager = TicketManager()

@app.route("/")
def index():
    siguiente = manager.consultar_siguiente()
    promedio = manager.obtener_promedio_tiempo()
    
    return render_template(
        "index.html",
        fila_prioritaria=list(manager.fila_prioritaria),
        fila_normal=list(manager.fila_normal),
        total_atendidos=manager.total_atendidos,
        promedio_tiempo=promedio,
        ultimo_atendido=manager.ultimo_atendido,
        siguiente=siguiente
    )

@app.route("/registrar", methods=["POST"])
def registrar():
    data = {
        "id": request.form.get("id"),
        "cliente": request.form.get("cliente"),
        "solicitante": request.form.get("solicitante"),
        "problema": request.form.get("problema"),
        "prioridad": request.form.get("prioridad"),
        "tiempo": request.form.get("tiempo")
    }
    manager.registrar_ticket(data)
    return redirect(url_for("index"))

@app.route("/atender", methods=["POST"])
def atender():
    manager.atender_siguiente()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)