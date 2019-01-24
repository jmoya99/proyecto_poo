from Mensajes import Mensajes

class Nota:

    def __init__(self,porcentaje,valor,id,estudiante,grupo):
        self.setPorcentaje(porcentaje)
        self.setValor(valor)
        self.setId(id)#el id es el numero de la nota, ejemplo: la nota #5 que se saca en calculo diferencial
        self.setEstudiante(estudiante)
        self.setGrupo(grupo)

    def setPorcentaje(self,porcentaje):
        self._porcentaje = porcentaje

    def getPorcentaje(self):
        return self._porcentaje

    def setValor(self,valor):
        self._valor = valor

    def getValor(self):
        return self._valor

    def setId(self,id):
        self._id = id

    def getId(self):
        return self._id

    def setEstudiante(self,estudiante):
        self._estudiante = estudiante

    def getEstudiante(self):
        return self._estudiante

    def setGrupo(self,grupo):
        self._grupo = grupo

    def getGrupo(self):
        return self._grupo

    def toString(self):
        return "{0}( {1}: {2}, {3}: {4}, Id: {5})".format(Mensajes.mensa["not"],Mensajes.mensa["por"],self.getPorcentaje(),Mensajes.mensa["val"],self.getValor(),self.getId())

    @staticmethod
    def buscarNota(lista,docEstudiante,IdMateria,numGrupo):
        for nota in lista:
            if(nota.getEstudiante().getIdentificacion() == docEstudiante and nota.getGrupo().getNumero() == numGrupo and nota.getGrupo().getMateria().getId() == IdMateria):
                return nota
        return None

    @staticmethod
    def registrar(nota,lista):
        if(Nota.buscarNota(lista,nota.getEstudiante(),nota.getGrupo().getMateria().getId(),nota.getGrupo().getNumero())):
            return Mensajes.mensa["err"]
        elif(not(nota.getGrupo() in nota.getEstudiante().getMatricula())):
            return Mensajes.mensa["err"]
        else:
            lista.append(nota)
            nota.getEstudiante().getNota().append(nota)
            nota.getGrupo().getNotas().append(nota)
            return Mensajes.mensa["reg"]

    @staticmethod
    def eliminar(lista,docEstudiante,IdMateria,numGrupo):
         nota = Nota.buscarNota(lista,docEstudiante,IdMateria,numGrupo)
         if(nota):
             nota.getEstudiante().getNota().remove(nota)
             nota.getGrupo().getNotas().remove(nota)
             lista.remove(nota)
             return Mensajes.mensa["eli"]
         else:
             return Mensajes.mensa["err"]

    @staticmethod
    def mostrarNotas(lista,est = -1,gru = -1,mat = -1):
        notas = ""
        for no in lista:
            a = no.getGrupo()
            if((est == -1 or est == no.getEstudiante().getIdentificacion()) and (gru == -1 or (gru == a.getNumero() and mat == a.getMateria().getId()))):
                notas += no.toString()+"\n"
        return notas

    @staticmethod
    def eliminarPorGrupo(lista,numGrupo,idMateria):
        borr = 0
        for i in range(0,len(lista)):
            if(lista[i-borr].getGrupo().getNumero() == numGrupo and lista[i-borr].getGrupo().getMateria().getId() == idMateria):
                Nota.eliminar(lista,lista[idEstudiante-borr].getEstudiante().getIdentificacion(),idMateria,numGrupo)
                borr += 1

    @staticmethod
    def eliminarPorEstudiante(lista,estudiante):
        borr = 0
        for i in range(0,len(lista)):
            if(lista[i-borr].getEstudiante().getIdentificacion() == estu):
                gru = lista[i-borr].getGrupo()
                Nota.eliminar(lista,estudiante,gru.getNumero(),gru.getMateria().getId())
                borr += 1

