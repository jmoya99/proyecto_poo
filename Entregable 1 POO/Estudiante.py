from Persona import Persona
from Matricula import Matricula
from Nota import Nota
from Mensajes import Mensajes as Me


class Estudiante(Persona):

    def __init__(self, nombre, identificacion, correo, clave):
        super().__init__(nombre, identificacion, correo, clave)
        self._materia = []
        self._nota = []
        self._matricula = []

    def set_materia(self, materia):
        self._materia = materia

    def get_materia(self):
        return self._materia

    def set_nota(self, nota):
        self._nota = nota

    def get_nota(self):
        return self._nota

    def set_matricula(self, matricula):
        self._matricula = matricula

    def get_matricula(self):
        return self._matricula

    @staticmethod
    def eliminar(estudiante, list_estu, list_notas, list_matri):
        Matricula.eliminar_por_estudiante(list_matri, estudiante)
        Nota.eliminar_por_estudiante(list_notas, estudiante)
        return Persona.eliminar(list_estu, estudiante)

    @staticmethod
    def registrar(list_estu, list_admin, list_profe, estudiante):
        return Persona.registrar(list_estu, list_admin, list_profe, estudiante, 0)
    @staticmethod
    def van_perdiendo(k,j):
                    o = k.get_estudiante().get_nota()
                    if(len(o) != 0):
                        sum = 0
                        sum2 = 0
                        L=[]
                        for l in o:
                            if(l.get_grupo()==j):
                                sum += ((l.get_porcentaje() / 100) *
                                l.get_valor())
                                sum2 += (l.get_porcentaje() / 100)
                        if(sum2!=0 and sum!=0):
                            prom = sum / sum2
                        else:
                            prom=0
                        if(prom < 3 and prom!=0):
                            L.append(k.get_estudiante().get_identificacion()+" "+k.get_estudiante().get_nombre()+"\n"+"__________________________")
                        if(len(L)!=0):
                            return L
                        else:
                            return(Me.mensa["Ganosinno"]+"\n"+"__________________________")
                    else:
                       return(Me.mensa["Noestnot"]+"\n"+"__________________________")