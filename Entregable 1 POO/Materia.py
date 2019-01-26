from Grupo import Grupo as G
from Mensajes import Mensajes

class Materia:

    def __init__(self,id,nombre,creditos):
        self.set_id(id)
        self.set_nombre(nombre)
        self.set_creditos(creditos)
        self._grupos = []

    def set_id(self,id,lista = None):
        if(not lista):
            lista = []
        if(id):
            if(not Materia.buscar_materia(lista,id)):
                self._id = id
                return Mensajes.mensa["mod"]
        return Mensajes.mensa["err"]

    def getId(self):
        return self._id

    def set_nombre(self,nombre):
        if(nombre):
            self._nombre = nombre
            return Mensajes.mensa["mod"]
        return Mensajes.mensa["err"]

    def getNombre(self):
        return self._nombre

    def set_creditos(self,creditos):
        if(creditos):
            self._creditos = creditos
            return Mensajes.mensa["mod"]
        return Mensajes.mensa["err"]

    def getCreditos(self):
        return self._creditos

    def setGrupos(self,grupos):
        if(grupos):
            self._grupos = grupos
            return Mensajes.mensa["mod"]
        return Mensajes.mensa["err"]

    def getGrupos(self):
        return self._grupos

    def to_string(self,tip = 0):
        if(tip == 0):
            grupos = ""
            for g in self.getGrupos():
                grupos += g.getNumero()+", "
            grupos = grupos[0:len(grupos)-2]
            return "{0}( {1}: {2}, {3}: {4}, {5}: {6}, {7}s: [{8}])".format(Mensajes.mensa["mat"],Mensajes.mensa["id"],self.getId(),Mensajes.mensa["nom"],self.getNombre(),Mensajes.mensa["cre"],self.getCreditos(),Mensajes.mensa["gru"],grupos)
        return "{0}( {1}: {2}, {3}: {4}, {5}: {6})".format(Mensajes.mensa["mat"],Mensajes.mensa["id"],self.getId(),Mensajes.mensa["nom"],self.getNombre(),Mensajes.mensa["cre"],self.getCreditos())

    @staticmethod
    def mostrarMaterias(lista):
        materias = ""
        for i in lista:
            materias += i.toString()+"\n"
        return materias

    @staticmethod
    def buscar_materia(lista,id):
        for m in lista:
            if(m.getId() == id or m.getNombre() == id):
                return m
        return None

    @staticmethod
    def mostrarGrupos(lista):
        gru = ""
        for g in lista:
            gru += g.toString()+"\n"
        return gru

    @staticmethod
    def eliminar(id,listMaterias,listGrupos,listMatricula,listNota):
        materia = Materia.buscar_materia(listMaterias,id)
        if(materia):
            id = materia.getId()
            G.eliminarPorMateria(listGrupos,id,listMatricula,listNota)
            listMaterias.remove(materia)
            Materia.guardar_cambios(listMaterias)
            return Mensajes.mensa["eli"]
        else:
            return Mensajes.mensa["err"]

    @staticmethod
    def cargar_materias(lista):
        inf = ""
        ini = 0
        fin = 0
        file = open("materia.txt")
        with file as f:
            inf += f.read()
        file.close()
        while(inf.find(">",fin+1) != -1 and fin < len(inf)-1):
            ini = inf.find("<",fin)
            fin = inf.find(">",ini)
            mat = inf[ini+1:fin].split(",")
            lista.append(Materia(mat[0],mat[1],mat[2]))

    @staticmethod
    def guardar_cambios(lista):
        file = open("materia.txt","w")
        file.write("")
        for i in lista:
            file.write("<{0},{1},{2}>".format(i.getId(),i.getNombre(),i.getCreditos()))
        file.close()
      
    @staticmethod
    def registrar(materia,lista):
        if(Materia.buscar_materia(lista,materia.getId())):
            return Mensajes.mensa["err"]
        else:
            lista.append(materia)
            Materia.guardar_cambios(lista)
            return Mensajes.mensa["reg"]

