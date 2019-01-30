from Persona import Persona
from Matricula import Matricula
from Nota import Nota

class Estudiante(Persona):

    def __init__(self,nombre,identidicacion,correo,clave):
        super().__init__(nombre,identidicacion,correo,clave)
        self._materia = []
        self._nota = []
        self._matricula = []

    def set_materia(self,materia):
        self._materia = materia

    def get_materia(self):
        return self._materia

    def set_nota(self,nota):
        self._nota = nota

    def get_nota(self):
        return self._nota

    def set_matricula(self,matricula):
        self._matricula = matricula

    def get_matricula(self):
        return self._matricula

    @staticmethod
    def eliminar(estudiante,list_estu,list_notas,list_matri):
        Matricula.eliminar_por_estudiante(list_matri,estudiante)
        Nota.eliminar_por_estudiante(list_notas,estudiante)
        return Persona.eliminar(list_estu,estudiante)

    @staticmethod
    def registrar(list_estu,list_admin,list_profe,estudiante):
        return Persona.registrar(list_estu,list_admin,list_profe,estudiante,0)
