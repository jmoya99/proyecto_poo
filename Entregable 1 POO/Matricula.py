from Mensajes import Mensajes

class Matricula:

    def __init__(self,semestre,estudiante,grupo):
        self.set_semestre(semestre)
        self.set_estudiante(estudiante)
        self.set_grupo(grupo)
        self._nota_final = 0.0

    def set_nota_final(self,nota):
        if(nota):
            self._nota_final = nota
            return Mensajes.mensa["mod"]
        return Mensajes.mensa["err"]

    def get_notafinal(self):
        notas = self.get_grupo().get_notas()
        acu = 0
        for no in notas:
            if(no.get_estudiante() == self.get_estudiante()):
                acu += (no.get_valor()*no.get_porcentaje())/100
        self.set_nota_final(round(acu,1))
        return self._nota_final

    def set_semestre(self,semestre):
        if(semestre):
            self._semestre = semestre
            return Mensajes.mensa["mod"]
        return Mensajes.mensa["err"]

    def get_semestre(self):
        return self._semestre

    def set_estudiante(self,estudiante):
        if(estudiante):
            self._estudiante = estudiante
            return Mensajes.mensa["mod"]
        return Mensajes.mensa["err"]

    def get_estudiante(self):
        return self._estudiante

    def set_grupo(self,grupo):
        if(grupo):
            self._grupo = grupo
            return Mensajes.mensa["mod"]
        return Mensajes.mensa["err"]

    def get_grupo(self):
        return self._grupo

    def to_string(self):
        return "{0}: {1}, {2}: {3}, {4}{5}, {6}: {7}".format(Mensajes.mensa["sem"],self.get_semestre(),Mensajes.mensa["notFinal"],
                                                               self.get_notafinal(),Mensajes.mensa["numGrp"],self.get_grupo().get_numero(),
                                                               Mensajes.mensa["id"]+" "+Mensajes.mensa["mat"],self.get_grupo().get_materia().get_id())

    @staticmethod
    def buscar_matricula(list_matricula,id_estudiante,id_materia):
        for ma in list_matricula:
            gr = ma.get_grupo()
            if(ma.get_estudiante().get_identificacion() == id_estudiante and gr.get_materia().get_id()):
                return ma
        return None

    @staticmethod
    def matricular(list_matricula,matr):
        gr = matr.get_grupo()
        if(Matricula.buscar_matricula(list_matricula,matr.get_estudiante().get_identificacion(),gr.get_materia().get_id())):
            return Mensajes.mensa["err"]
        else:
            list_matricula.append(matr)
            matr.get_grupo().get_matricula().append(matr)
            matr.get_estudiante().get_matricula().append(matr)
            return Mensajes.mensa["reg"]

    @staticmethod
    def cancelar(list_matricula,id_estudiante,id_materia):
        mat = Matricula.buscar_matricula(list_matricula,id_estudiante,id_materia)
        if(mat):
            list_matricula.remove(mat)
            return Mensajes.mensa["eli"]
        else:
            return Mensajes.mensa["err"]

    @staticmethod
    def eliminar_por_grupo(lista,num_grupo,id_materia):
        borr = 0
        for i in range(0,len(lista)):
            if(lista[i-borr].get_grupo().get_numero() == num_grupo and lista[i-borr].get_grupo().get_materia().get_id() == id_materia):
                Matricula.cancelar(lista,lista[id_estudiante-borr].get_estudiante().get_identificacion(),num_grupo,id_materia)
                borr += 1

    @staticmethod
    def eliminar_por_estudiante(lista,estu):
        borr = 0
        for i in range(0,len(lista)):
            if(lista[i-borr].get_estudiante().get_identificacion() == estu):
                gru = lista[i-borr].get_grupo()
                Matricula.cancelar(lista,estu,gru.get_numero(),gru.get_materia().get_id())
                borr += 1
