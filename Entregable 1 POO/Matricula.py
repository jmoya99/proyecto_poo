from Mensajes import Mensajes

class Matricula:

    def __init__(self,semestre,estudiante,grupo):
        self.setSemestre(semestre)
        self.setEstudiante(estudiante)
        self.setGrupo(grupo)
        self._notaFinal = 0.0

    def setNotaFinal(self,nota):
        self._notaFinal = nota

    def getNotaFinal(self):
        return self._notaFinal

    def setSemestre(self,semestre):
        self._semestre = semestre

    def getSemestre(self):
        return self._semestre

    def setEstudiante(self,estudiante):
        self._estudiante = estudiante

    def getEstudiante(self):
        return self._estudiante

    def setGrupo(self,grupo):
        self._grupo = grupo

    def getGrupo(self):
        return self._grupo

    @staticmethod
    def buscarMatricula(listMatricula,idEstudiante,IdMateria):
        for ma in listMatricula:
            gr = ma.getGrupo()
            if(ma.getEstudiante().getIdentificacion() == idEstudiante and gr.getMateria().getId()):
                return ma
        return None

    @staticmethod
    def matricular(listMatricula,matr):
        gr = matr.getGrupo()
        if(Matricula.buscarMatricula(listMatricula,matr.getEstudiante().getIdentificacion(),gr.getMateria().getId())):
            return Mensajes.mensa["err"]
        else:
            listMatricula.append(matr)
            matr.getGrupo().getMatricula().append(matr)
            matr.getEstudiante().getMatricula().append(matr)
            return Mensajes.mensa["reg"]

    @staticmethod
    def cancelar(listMatricula,idEstudiante,numGrupo,IdMateria):
        mat = Matricula.buscarMatricula(listMatricula,idEstudiante,numGrupo,IdMateria)
        if(mat):
            listMatricula.remove(mat)
            return Mensajes.mensa["eli"]
        else:
            return Mensajes.mensa["err"]

    @staticmethod
    def eliminarPorGrupo(lista,numGrupo,idMateria):
        borr = 0
        for i in range(0,len(lista)):
            if(lista[i-borr].getGrupo().getNumero() == numGrupo and lista[i-borr].getGrupo().getMateria().getId() == idMateria):
                Matricula.cancelar(lista,lista[idEstudiante-borr].getEstudiante().getIdentificacion(),numGrupo,idMateria)
                borr += 1

    @staticmethod
    def eliminarPorEstudiante(lista,estu):
        borr = 0
        for i in range(0,len(lista)):
            if(lista[i-borr].getEstudiante().getIdentificacion() == estu):
                gru = lista[i-borr].getGrupo()
                Matricula.cancelar(lista,estu,gru.set_numero(),gru.getMateria().getId())
                borr += 1