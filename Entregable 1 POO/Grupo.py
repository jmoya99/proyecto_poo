from Mensajes import Mensajes
from Matricula import Matricula
from Nota import Nota


class Grupo:

    def __init__(self, numero, materia, profesor):
        self.set_numero(numero)
        self.set_materia(materia)
        self.set_profesor(profesor)
        self._notas = []
        self._matricula = []

    def set_numero(self, numero, materia=None, lista=None):
        if(not lista):
            lista = []
        if(numero):
            if(not Grupo.buscar_grupo(lista, numero, materia)):
                self._numero = numero
                return Mensajes.mensa["mod"]
        return Mensajes.mensa["err"]

    def get_numero(self):
        return self._numero

    def set_materia(self, materia):
        if(materia):
            self._materia = materia
            return Mensajes.mensa["mod"]
        self._materia = None
        return Mensajes.mensa["err"]

    def get_materia(self):
        return self._materia

    def set_profesor(self, profesor):
        if(profesor):
            self._profesor = profesor
            return Mensajes.mensa["mod"]
        self._profesor = None
        return Mensajes.mensa["err"]

    def get_profesor(self):
        return self._profesor

    def set_notas(self, notas):
        if(notas):
            self._notas = notas
            return Mensajes.mensa["mod"]
        return Mensajes.mensa["err"]

    def get_notas(self):
        return self._notas

    def set_matricula(self, matricula):
        if(matricula):
            self._materia = matricula
            return Mensajes.mensa["mod"]
        return Mensajes.mensa["err"]

    def get_matricula(self):
        return self._matricula

    def to_string(self, x=0):
        if(x != 0):
            return "{0}( {1}: {2}, {3}: {4}, {5}: {6})".format(Mensajes.mensa["gru"], Mensajes.mensa["num"], self.get_numero(), Mensajes.mensa["mat"], self.get_materia().to_string(1), Mensajes.mensa["pro"], self.get_profesor().get_nombre())
        return "{0}( {1}: {2}, {3}: {4}, {5}: {6})".format(Mensajes.mensa["gru"], Mensajes.mensa["num"], self.get_numero(), Mensajes.mensa["mat"], self.get_materia().to_string(1), Mensajes.mensa["pro"], self.get_profesor().to_string())

    @staticmethod
    def buscar_grupo(lista, num, id_materia):
        for gr in lista:
            if(gr.get_numero() == num and id_materia == gr.get_materia().get_id()):
                return gr
        return None

    @staticmethod
    def registrar(grupo, lista):
        if(Grupo.buscar_grupo(lista, grupo.get_numero(), grupo.get_materia().get_id()) or not(grupo.get_profesor())):
            return Mensajes.mensa["err"]
        else:
            lista.append(grupo)
            grupo.get_materia().get_grupos().append(grupo)
            grupo.get_profesor().get_grupos().append(grupo)
            return Mensajes.mensa["reg"]

    @staticmethod
    def eliminar(lista, num, id_materia, list_matricula, list_nota):
        grupo = Grupo.buscar_grupo(lista, num, id_materia)
        if(grupo):
            Nota.eliminar_por_grupo(list_nota, num, id_materia)
            Matricula.eliminar_por_grupo(list_matricula, num, id_materia)
            grupo.get_materia().get_grupos().remove(grupo)
            lista.remove(grupo)
            return Mensajes.mensa["eli"]
        else:
            return Mensajes.mensa["err"]

    @staticmethod
    def mostrar_grupos(lista, id_materia=-1):
        grupos = ""
        for gr in lista:
            if(id_materia == -1 or id_materia == gr.get_materia().get_id()):
                grupos += gr.to_string() + "\n"
        return grupos

    # Elimina todos los grupos relacionados a una materia
    @staticmethod
    def eliminar_por_materia(lista, id_materia, list_matricula, list_nota):
        borr = 0
        for i in range(0, len(lista)):
            if(lista[i - borr].get_materia().get_id() == id_materia):
                Grupo.eliminar(
                    lista, lista[i - borr].get_numero(), id_materia, list_matricula, list_nota)
                borr += 1
    @staticmethod
    def mejores_grupos(i):
        n = i.get_grupos()
        if(len(n)!=0):
            a={}
            for j in n:
                m=0
                if(len(j.get_notas())!=0):
                    for k in j.get_notas():
                        m+=k.get_valor()
                    a[m/len(j.get_notas())] = j
                else:
                    a[0]=j
            mayor =max(a.keys())
            if(mayor!=0):
                return Mensajes.mensa["ideMate"]+i.get_id()+"\n"+Mensajes.mensa["gru"]+": "+a[mayor].get_numero()+"\n __________________________"
            else:
                return Mensajes.mensa["ideMate"]+i.get_id()+"\n"+Mensajes.mensa["Nonotas"]+"\n __________________________"
        else:
            return Mensajes.mensa["ideMate"]+i.get_id()+"\n"+Mensajes.mensa["Nogrup"]+"\n __________________________"