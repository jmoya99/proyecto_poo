from Mensajes import Mensajes

class Nota:

    def __init__(self,porcentaje,valor,id,estudiante,grupo):

        self.set_porcentaje(porcentaje)
        self.set_valor(valor)
        self.set_id(id)
        #el id es el numero de la nota, ejemplo: la nota #5 que
         #se saca en calculo diferencial
        self.set_estudiante(estudiante)
        self.set_grupo(grupo)

    def set_porcentaje(self,porcentaje):
        self._porcentaje = porcentaje

    def get_porcentaje(self):
        return self._porcentaje

    def set_valor(self,valor):
        self._valor = valor

    def get_valor(self):
        return self._valor

    def set_id(self,id):
        self._id = id

    def get_id(self):
        return self._id

    def set_estudiante(self,estudiante):
        self._estudiante = estudiante

    def get_estudiante(self):
        return self._estudiante

    def set_grupo(self,grupo):
        self._grupo = grupo

    def get_grupo(self):
        return self._grupo

    def to_string(self):
        return "{0}( {1}: {2}, {3}: {4}, Id: {5})".format(
            Mensajes.mensa["not"],
            Mensajes.mensa["por"],
            self.get_porcentaje(),
            Mensajes.mensa["val"],
            self.getValor(),
            self.get_id()
        )

    @staticmethod
    def buscar_nota(lista,doc_estudiante,id_materia,num_grupo):
        for nota in lista:
            if(nota.get_estudiante().get_identificacion() == doc_estudiante
            and nota.get_grupo().get_numero() == num_grupo
            and nota.get_grupo().get_materia().get_id() == id_materia):
                return nota
        return None

    @staticmethod
    def registrar(nota,lista):
        if(Nota.buscar_nota(lista,
        nota.get_estudiante(),
        nota.get_grupo().get_materia().get_id(),
        nota.get_grupo().get_numero())):
            return Mensajes.mensa["err"]
        # elif(not(nota.get_grupo() in nota.get_estudiante().get_matricula())):
        #     return Mensajes.mensa["err"]
        else:
            lista.append(nota)
            nota.get_estudiante().get_nota().append(nota)
            nota.get_grupo().get_notas().append(nota)
            return Mensajes.mensa["reg"]

    @staticmethod
    def eliminar(lista,doc_estudiante,id_materia,num_grupo):
         nota = Nota.buscar_nota(lista,doc_estudiante,id_materia,num_grupo)
         if(nota):
             nota.get_estudiante().get_nota().remove(nota)
             nota.get_grupo().get_notas().remove(nota)
             lista.remove(nota)
             return Mensajes.mensa["eli"]
         else:
             return Mensajes.mensa["err"]

    @staticmethod
    def mostrar_notas(lista,est = -1,gru = -1,mat = -1):
        notas = ""
        for no in lista:
            a = no.get_grupo()
            if((est == -1 or est == no.get_estudiante().get_identificacion())
            and (gru == -1 or (gru == a.get_numero()
            and mat == a.get_materia().get_id()))):
                notas += no.toString()+"\n"
        return notas

    @staticmethod
    def eliminar_por_grupo(lista,num_grupo,id_materia):
        borr = 0
        for i in range(0,len(lista)):
            if(lista[i-borr].get_grupo().get_numero() == num_grupo
            and lista[i-borr].get_grupo().get_materia().get_id() == id_materia):
                Nota.eliminar(lista,
                lista[idEstudiante-borr].get_estudiante().get_identificacion(),
                id_materia,num_grupo)
                borr += 1

    @staticmethod
    def eliminar_por_estudiante(lista,estu):
        borr = 0
        for i in range(0,len(lista)):
            if(lista[i-borr].get_estudiante().get_identificacion() == estu):
                gru = lista[i-borr].get_grupo()
                Nota.eliminar(lista,estudiante,gru.get_numero(),gru.get_materia().get_id())
                borr += 1
