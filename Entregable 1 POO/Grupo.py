from Mensajes import Mensajes
from Matricula import Matricula
from Nota import Nota

class Grupo:
    
    def __init__(self,numero,materia,profesor):
        self.set_numero(numero)
        self.set_materia(materia)
        self.set_profesor(profesor)
        self._notas = []
        self._matricula = []

    def set_numero(self,numero,materia = None,lista = None):
        if(not lista):
            lista = []
        if(numero):
            if(not Grupo.buscar_grupo(lista,numero,materia)):
                self._numero = numero
                return Mensajes.mensa["mod"]
        return Mensajes.mensa["err"] 

    def getNumero(self):
        return self._numero

    def set_materia(self,materia):
        if(materia):
            self._materia = materia
            return Mensajes.mensa["mod"]
        self._materia = None
        return Mensajes.mensa["err"]

    def getMateria(self):
        return self._materia

    def set_profesor(self,profesor):
        if(profesor):
            self._profesor = profesor
            return Mensajes.mensa["mod"]
        self._profesor = None
        return Mensajes.mensa["err"]

    def getProfesor(self):
        return self._profesor

    def setNotas(self,notas):
        if(notas):
            self._notas = notas
            return Mensajes.mensa["mod"]
        return Mensajes.mensa["err"]

    def getNotas(self):
        return self._notas

    def setMatricula(self,matricula):
        if(matricula):
            self._materia = matricula
            return Mensajes.mensa["mod"]
        return Mensajes.mensa["err"]

    def getMatricula(self):
        return self._matricula

    def to_string(self):
        return "{0}( {1}: {2}, {3}: {4}, {5}: {6})".format(Mensajes.mensa["gru"],Mensajes.mensa["num"],self.getNumero(),Mensajes.mensa["mat"],self.getMateria().to_string(1),Mensajes.mensa["pro"],self.getProfesor().to_string())
        
    @staticmethod
    def buscar_grupo(lista,num,IdMateria):
        for gr in lista:
            if(gr.getNumero() == num and IdMateria == gr.getMateria().getId()):
                return gr
        return None

    @staticmethod
    def registrar(grupo,lista):
        if(Grupo.buscar_grupo(lista,grupo.getNumero(),grupo.getMateria().getId()) or not(grupo.getProfesor())):
            return Mensajes.mensa["err"]
        else:
            lista.append(grupo)
            grupo.getMateria().getGrupos().append(grupo)
            return Mensajes.mensa["reg"]

    @staticmethod
    def eliminar(lista,num,idMateria,listMatricula,listNota):
         grupo = Grupo.buscar_grupo(lista,num,idMateria)
         if(grupo):
             Nota.eliminarPorGrupo(listNota,num,idMateria)
             Matricula.eliminarPorGrupo(listMatricula,num,idMateria)
             grupo.getMateria().getGrupos().remove(grupo)
             lista.remove(grupo)
             return Mensajes.mensa["eli"]
         else:
             return Mensajes.mensa["err"]

    @staticmethod
    def mostrarGrupos(lista,idMateria = -1):
        grupos = ""
        for gr in lista:
            if(idMateria == -1 or idMateria == gr.getMateria().getId()):
                grupos += gr.toString()+"\n"
        return grupos

    @staticmethod
    def eliminarPorMateria(lista,idMateria,listMatricula,listNota):
        borr = 0
        for i in range(0,len(lista)):
                if(lista[i-borr].getMateria().getId() == idMateria):
                    Grupo.eliminar(lista,lista[i-borr].getNumero(),idMateria,listMatricula,listNota)
                    borr += 1


