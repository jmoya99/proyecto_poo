from Persona import Persona
from Operaciones import Operaciones
from Mensajes import Mensajes


class Profesor(Persona):

    def __init__(self, nombre, identificacion, correo, clave):
        super().__init__(nombre, identificacion, correo, clave)
        self._grupos = []

    def set_grupos(self, grupos):
        self._grupos = grupos

    def get_grupos(self):
        return self._grupos

    @staticmethod
    def eliminar(lista,identificacion):
        pro = Persona.buscar_persona(lista,identificacion)
        if(pro):
            if(len(pro.get_grupos()) > 0):
                return Mensajes.mensa["noSePuede"]
        return Persona.eliminar(lista, identificacion)

    @staticmethod
    def registrar(list_estu, list_admin, list_profe, profesor):
        return Persona.registrar(list_estu, list_admin, list_profe, profesor, 1)

    @staticmethod
    def encontrar_correos_y_enviar(lista, gru, asun, mat, fech, nom, det):
        for i in lista:
            if(i.get_numero() == gru and i.get_materia().get_id() == mat):
                for j in i.get_matricula():
                    corr = j.get_estudiante().get_correo()
                    Operaciones.enviar_correo_electronico(
                        corr, asun, nom + " \n" +Mensajes.mensa["ideMate"]+" "+mat + " \n" + Mensajes.mensa["gru"] + ": " + gru + " \n" + Mensajes.mensa["fech"] + ": " + fech + " \n" + det)
        return Mensajes.mensa["CorrE"]
