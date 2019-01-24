from Persona import Persona

class Profesor(Persona):

    def __init__(self,nombre,identidicacion,correo,clave):
        super().__init__(nombre,identidicacion,correo,clave)
        self._grupos = []

    def setGrupos(self,grupos):
        self._grupos = grupos

    def getGrupos(self):
        return self._grupos

    @staticmethod
    def registrar(listEstu,listAdmin,listProfe,profesor):
        return Persona.registrar(listEstu,listAdmin,listProfe,profesor,1)

