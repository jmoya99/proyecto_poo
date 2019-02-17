from Mensajes import Mensajes
from Operaciones import Operaciones


class Nota:

    def __init__(self, porcentaje, valor, id, estudiante, grupo):
        self.set_porcentaje(porcentaje)
        self.set_valor(valor)
        self.set_id(id)
        # el id es el numero de la nota, ejemplo: la nota #5 que
        # se saca en calculo diferencial
        self.set_estudiante(estudiante)
        self.set_grupo(grupo)

    def set_porcentaje(self, porcentaje):
        if(porcentaje):
            self._porcentaje = porcentaje
            return Mensajes.mensa["mod"]
        return Mensajes.mensa["err"]

    def get_porcentaje(self):
        return self._porcentaje

    def set_valor(self, valor):
        if(valor):
            self._valor = valor
            return Mensajes.mensa["mod"]
        return Mensajes.mensa["err"]

    def get_valor(self):
        return self._valor

    def set_id(self, id, lista=None):
        if(id):
            if(lista == None):
                self._id = id
                return Mensajes.mensa["mod"]
            elif(Nota.buscar_nota(lista, self.get_estudiante().get_identificacion(),
                                  self.get_grupo().get_materia().get_id(), self.get_grupo().get_numero(), id)):
                return Mensajes.mensa["err"]
            else:
                self._id = id
                return Mensajes.mensa["mod"]
        return Mensajes.mensa["err"]

    def get_id(self):
        return self._id

    def set_estudiante(self, estudiante, lista=None):
        if(estudiante):
            if(lista == None):
                self._estudiante = estudiante
                return Mensajes.mensa["mod"]
            elif(Nota.buscar_nota(lista, estudiante.get_identificacion(), self.get_grupo().get_materia().get_id(),
                                  self.get_grupo().get_numero(), self.get_id())):
                return Mensajes.mensa["err"]
            else:
                self._estudiante = estudiante
                return Mensajes.mensa["mod"]
        return Mensajes.mensa["err"]

    def get_estudiante(self):
        return self._estudiante

    def set_grupo(self, grupo, lista=None):
        if(grupo):
            if(lista == None):
                self._grupo = grupo
                return Mensajes.mensa["mod"]
            elif(Nota.buscar_nota(lista, self.get_estudiante().get_identificacion(), grupo.get_materia().get_id(),
                                  grupo, self.get_id())):
                return Mensajes.mensa["err"]
            else:
                self._grupo = grupo
                return Mensajes.mensa["mod"]
        return Mensajes.mensa["err"]

    def get_grupo(self):
        return self._grupo

    def to_string(self):
        return "{0}( {1}: {2}, {3}: {4}, Id: {5})".format(
            Mensajes.mensa["not"],
            Mensajes.mensa["por"],
            self.get_porcentaje(),
            Mensajes.mensa["val"],
            self.get_valor(),
            self.get_id()
        )

    @staticmethod
    def buscar_nota(lista, doc_estudiante, id_materia, num_grupo, id):
        for nota in lista:
            if(nota.get_estudiante().get_identificacion() == doc_estudiante
            and nota.get_grupo().get_numero() == num_grupo
            and nota.get_grupo().get_materia().get_id() == id_materia
               and int(nota.get_id()) == int(id)):
                return nota
        return None

    @staticmethod
    def registrar(nota, lista):
        if(Nota.buscar_nota(lista,
                            nota.get_estudiante(),
                            nota.get_grupo().get_materia().get_id(),
                            nota.get_grupo().get_numero(), nota.get_id())):
            return Mensajes.mensa["err"]
        else:
            lista.append(nota)
            nota.get_estudiante().get_nota().append(nota)
            nota.get_grupo().get_notas().append(nota)
            return Mensajes.mensa["reg"]

    @staticmethod
    def eliminar(lista, doc_estudiante, id_materia, num_grupo, id):
        nota = Nota.buscar_nota(lista, doc_estudiante,
                                id_materia, num_grupo, id)
        if(nota):
            nota.get_estudiante().get_nota().remove(nota)
            nota.get_grupo().get_notas().remove(nota)
            lista.remove(nota)
            return Mensajes.mensa["eli"]
        else:
            return Mensajes.mensa["err"]

    @staticmethod
    def mostrar_notas(lista, est=-1, gru=-1, mat=-1):
        notas = ""
        for no in lista:
            a = no.get_grupo()
            if((est == -1 or est == no.get_estudiante().get_identificacion())
               and (gru == -1 or (gru == a.get_numero() and
                              mat == a.get_materia().get_id()))):
                notas += no.toString() + "\n"
        return notas

    @staticmethod
    def eliminar_por_grupo(lista, num_grupo, id_materia):
        borr = 0
        for i in range(0, len(lista)):
            if(lista[i - borr].get_grupo().get_numero() == num_grupo and
               lista[i - borr].get_grupo().get_materia().get_id() == id_materia):
                Nota.eliminar(lista,
                              lista[idEstudiante
                                    - borr].get_estudiante().get_identificacion(),
                              id_materia, num_grupo)
                borr += 1

    @staticmethod
    def eliminar_por_estudiante(lista, estu):
        borr = 0
        for i in range(0, len(lista)):
            if(lista[i - borr].get_estudiante().get_identificacion() == estu):
                gru = lista[i - borr].get_grupo()
                Nota.eliminar(lista, estudiante, gru.get_numero(),
                              gru.get_materia().get_id())
                borr += 1

    @staticmethod
    def enviar_correo_actualizar_nota(opc, id, nota, porcentaje, estudiante, materia):
        correo_enviar = estudiante.get_correo()
        cuerpo = ""

        if (Mensajes.mensa[opc] == "borro" or Mensajes.mensa[opc] == "delete"):
            cuerpo = Mensajes.mensa["cuerpo_borro"] + id + \
                Mensajes.mensa["cuerpo_borro2"] + str(materia)
        else:
            cuerpo = Mensajes.mensa["cuerpo_resto"] + str(materia) + Mensajes.mensa["cuerpo_resto2"] + str(
                id) + Mensajes.mensa["cuerpo_resto3"] + str(nota) + Mensajes.mensa["cuerpo_resto4"] + str(porcentaje) + Mensajes.mensa["cuerpo_resto5"]
        asunto = Mensajes.mensa["asunto"] + Mensajes.mensa[opc] + Mensajes.mensa["asunto2"]
        Operaciones.enviar_correo_electronico(correo_enviar, asunto, cuerpo)

    @staticmethod
    def mejores_notas(lista_grupos, id_materia, id_grupo):
        for grupo in lista_grupos:
            if (grupo.get_materia().get_id() == id_materia):
                if(grupo.get_numero()== id_grupo):
                    lista_notas = grupo.get_notas()
                    lista_notas.sort(key=lambda x: x._valor, reverse=True)
                    if (len(lista_notas)<3 and len(lista_notas)>0):
                        print(Mensajes.mensa["mejores_notas1"] + str(len(lista_notas)) + Mensajes.mensa["mejores_notas2"])
                        contador = 0
                        for nota in lista_notas:
                            contador +=1
                            print(Mensajes.mensa[contador] + Mensajes.mensa["cuerpo_best"] +
                            str(lista_notas[contador-1].get_valor()) + Mensajes.mensa["cuerpo_best2"] + lista_notas[contador-1].get_estudiante().get_nombre())
                    elif(len(lista_notas)>=3):
                        print(Mensajes.mensa["mejores_notas"])
                        for nota in range(0,3):
                            print(Mensajes.mensa[nota+1] + Mensajes.mensa["cuerpo_best"] +
                            str(lista_notas[nota].get_valor()) + Mensajes.mensa["cuerpo_best2"] + lista_notas[nota].get_estudiante().get_nombre())
                    else:
                        print(Mensajes.mensa["No_estudiantes"])
    @staticmethod
    def porcentaje_diferente_100(materia, id_grupo, estudiante, porcentaje):
        grupos = materia.get_grupos()
        for grupo in grupos:
            if (grupo.get_numero() == id_grupo):
                sum = 0
                notas = grupo.get_notas()
                for nota in notas:
                    if (nota.get_estudiante().get_identificacion() == estudiante):
                        sum = sum + nota.get_porcentaje()
                total = sum + porcentaje
                print(total)
                if (total > 100):
                    return False
                else:
                    return True
