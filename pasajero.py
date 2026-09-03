import random
from persona import Persona
from viaje import Viaje


class Pasajero(Persona):

    def __init__(self, id, nombre, email, telefono, metodoPago, calificacionPromedio=0.0):

        super().__init__(id, nombre, email, telefono)

        self.metodoPago = metodoPago
        self.calificacionPromedio = calificacionPromedio

    def solicitarViaje(self, origen, destino):

        if origen == destino:
            print("Error: el origen y el destino no pueden ser iguales.")
            return None

        # tuve que generar un id numérico para cumplir con los requerimientos de la clase Viaje no encontre otra forma que me funcionara ksks
        id_viaje = random.randint(100, 999)
        viaje = Viaje(id_viaje, origen, destino)

        return viaje

    def cancelarViaje(self, viaje):

        if viaje.estado == "PENDIENTE" or viaje.estado == "ACEPTADO":
            viaje.estado = "CANCELADO"
            return True

        print("Error: el viaje no puede ser cancelado.")
        return False


    def calificarViaje(self, viaje, puntuacion):
        if viaje.estado != "FINALIZADO":
            print("Error: Solo se pueden calificar viajes en estado FINALIZADO.")
            return False
            
        if not (1 <= puntuacion <= 5):
            print("Error: La puntuación debe estar entre 1 y 5.")
            return False
            
        print(f"Viaje {viaje.id} calificado exitosamente con {puntuacion} estrellas.")
        return True