from Persona import Persona
from Operaciones import Operaciones

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
    @staticmethod
    def encontrar_correos(prof,gru,nom,fech,det):
        for i in prof.get_grupos():
            if(i.get_numero() == gru):
                for j in i.get_matricula():
                    corr=j.get_estudiante().get_correo()
                    Operaciones.enviar_correo_electronico(corr,nom,det+" "+fech)
