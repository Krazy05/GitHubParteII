class Clientes:
    def __init__(self):
        pass

    def AltasDeClientes(self, nombres, apellidos, telefono):
        self._nombres = nombres
        self._apellidos = apellidos
        self._telefono = telefono 
        self._equipos = []
    
    def AgregarEquipo(self,equipo):
        self._equipos.append(equipo)
        
    def VerEquipos(self):
        for eq in self._equipos:
            print(eq)

    def __str__(self):
        return f"Nombres: {self._nombres} Apellidos: {self._apellidos}, Tel: {self._telefono}"

    @property
    def nombres(self):
        return self._nombres

    @nombres.setter
    def nombres(self, value):
        self._nombres = value

    @property
    def apellidos(self):
        return self._apellidos

    @apellidos.setter
    def apellidos(self, value):
        self._apellidos = value

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, value):
        self._telefono = value