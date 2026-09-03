from pasajero import Pasajero
from conductor import Conductor
from vehiculo import Vehiculo
from pago import Pago
import os
os.system ("cls")


def main():

    # Crear pasajeros#
    pasajero1 = Pasajero(1, "Benjamín munoz", "benja@gmail.com", "+56932435443", "Tarjeta")
    pasajero2 = Pasajero(2, "elpepe", "pepe@gmail.com", "+56912213245", "Efectivo")
    pasajero3 = Pasajero(3, "maikoll", "maikoll@gmail.com", "+56934546587", "Transferencia")

    # Crear vehículos#
    vehiculo1 = Vehiculo("pptt21", "Toyota", "Yaris", 1999, 4)
    vehiculo2 = Vehiculo("pttp", "Hyundai", "Accent", 2023, 4)


    # Crear conductores#
    conductor1 = Conductor(3, "juan", "juaa@email.com", "+56943556678", "Clase B", vehiculo1)
    conductor2 = Conductor(4, "bejota", "vkngo@email.com", "+569948584", "Clase B", vehiculo2)


    # Actualizar teléfono#
    pasajero1.actualizarTelefono("+56905050505")


    # Solicitar viaje
    viaje1 = pasajero1.solicitarViaje(
        "Plaza de Armas",
        "Universidad"
    )

    # Conductor acepta
    conductor1.aceptarViaje(viaje1)

    # Iniciar viaje
    viaje1.iniciar()

    # Finalizar viaje
    viaje1.finalizar()

    # Definir distancia
    viaje1.distancia = 5.0

    # Calcular tarifa
    viaje1.calcularTarifa()

    # Iniciar viaje
    viaje1.iniciar()
    
    

    # Finalizar viaje
    viaje1.finalizar



    # Mostrar información
    print("Estado:", viaje1.estado)
    print("Tarifa:", viaje1.tarifa)

    #Generar pago
    pago1 = Pago(
         1,
         viaje1.tarifa,
         pasajero1.metodoPago,
         "PAGADO"
     )

    print("Monto del pago:", pago1.obtenerMonto())

    pago1.generarComprobante()



    # Calificar viaje
    pasajero1.calificarViaje(viaje1, 5)



if __name__ == "__main__":
    main()