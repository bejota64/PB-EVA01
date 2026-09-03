class Pago:
    def __init__(self, id_pago, monto, metodo, estado):
        self.id = id_pago
        self.monto = monto
        self.metodo = metodo
        self.estado = estado

    def obtenerMonto(self):
        return self.monto

    def generarComprobante(self):
        print("\n--- COMPROBANTE DE PAGO ---")
        print(f"ID Pago: {self.id}")
        print(f"Monto: ${self.monto}")
        print(f"Método de pago: {self.metodo}")
        print(f"Estado: {self.estado}")
        print("---------------------------\n")

    def obtenerEstado(self):
        print(f"Estado actual del viaje: {self.estado}")
        return self.estado    