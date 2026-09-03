class Persona:

    def __init__(self, id, nombre, email, telefono):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def iniciarSesion(self):
        return True


    #Realizar este metodo para actualizar el telefono de la persona
    def actualizarTelefono(self, telefono):
        self.telefono = telefono

    def obtenerNombre(self):
        return self.nombre