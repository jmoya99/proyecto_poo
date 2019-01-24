from Persona import Persona
from Matricula import Matricula
from Nota import Nota

class Estudiante(Persona):

    def __init__(self,nombre,identidicacion,correo,clave):
        super().__init__(nombre,identidicacion,correo,clave)
        self._materia = []
        self._nota = []
        self._matricula = []

    def setMateria(self,materia):
        self._materia = materia

    def getMateria(self):
        return self._materia

    def setNota(self,nota):
        self._nota = nota

    def getNota(self):
        return self._nota

    def setMatricula(self,matricula):
        self._matricula = matricula

    def getMatricula(self):
        return self._matricula

    @staticmethod
    def eliminar(estudiante,listEstu,listNotas,listMatri):
        Matricula.eliminarPorEstudiante(listMatri,estudiante)
        Nota.eliminarPorEstudiante(listEstu,estudiante)
        return Persona.eliminar(listEstu,estudiante)

    @staticmethod
    def registrar(listEstu,listAdmin,listProfe,estudiante):
        return Persona.registrar(listEstu,listAdmin,listProfe,estudiante,0)