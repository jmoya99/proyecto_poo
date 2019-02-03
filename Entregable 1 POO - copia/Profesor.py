from Persona import Persona

class Profesor(Persona):

    def __init__(self,nombre,identificacion,correo,clave):
        super().__init__(nombre,identificacion,correo,clave)
        self._grupos = []

    def set_grupos(self,grupos):
        self._grupos = grupos

    def get_grupos(self):
        return self._grupos

    @staticmethod
    def registrar(list_estu,list_admin,list_profe,profesor):
        return Persona.registrar(list_estu,list_admin,list_profe,profesor,1)

