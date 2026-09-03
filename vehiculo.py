class Vehiculo:
    def __init__(self, patente, marca, modelo, año, capacidad, estado="Operativo"):
        
        self.patente = patente  
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.capacidad = capacidad
        self.estado = estado

    def obtenerInformacion(self):
        print(f"Vehículo: {self.marca} {self.modelo} ({self.año})  Patente: {self.patente}  Estado: {self.estado}")

    def cambiarEstado(self, estado):
        self.estado = estado        