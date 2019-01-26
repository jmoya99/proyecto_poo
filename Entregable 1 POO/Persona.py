from Mensajes import Mensajes

class Persona:

    def __init__(self,nombre,identidicacion,correo,clave):
        self.set_nombre(nombre)
        self.set_identificacion(identidicacion)
        self.set_correo(correo)
        self.set_clave(clave)

    def set_nombre(self,nombre):
        if(nombre):
            self._nombre = nombre
            return Mensajes.mensa["mod"]
        return Mensajes.mensa["err"]

    def get_nombre(self):
        return self._nombre

    def set_identificacion(self,identificacion,lista = None):
        if(not lista):
            lista = []
        if(identificacion):
            if(not Persona.buscar_persona(lista,identificacion)):
                self._identificacion = identificacion
                return Mensajes.mensa["mod"]
        return Mensajes.mensa["err"]

    def getIdentificacion(self):
        return self._identificacion

    def set_correo(self,correo,lista = None):
        if(not lista):
            lista = []
        if(correo):
            if(not Persona.buscar_persona(lista,correo)):
                self._correo = correo
                return Mensajes.mensa["mod"]
        return Mensajes.mensa["err"]

    def getCorreo(self):
        return self._correo

    def set_clave(self,clave):
        if(clave):
            self._clave = clave
            return Mensajes.mensa["mod"]
        return Mensajes.mensa["err"]

    def getClave(self):
        return self._clave

    def to_string(self):
        return "{0}({1}: {2},{3}: {4},{5}: {6},{7}: {8})".format(Mensajes.mensa["usu"],Mensajes.mensa["nom"],self.get_nombre(),Mensajes.mensa["ide"],self.getIdentificacion(),Mensajes.mensa["cor"],self.getCorreo(),Mensajes.mensa["con"],self.getClave())

    @staticmethod
    def buscar_persona(listPersonas,id):
        for p in listPersonas:
            if((p.getIdentificacion() == id or p.getCorreo() == id) and id):
                return p
        return None

    @staticmethod
    def registrar(listEstu,listAdmin,listProfe,persona,tip=-1):#tip se refiere al tipo de usuario que es
        if(Persona.buscar_persona(listAdmin+listEstu+listProfe,persona.getIdentificacion())):
            return Mensajes.mensa["err"]
        else:
            if(tip == 0):#estudiante
                listEstu.append(persona)
            elif(tip == 1):#profesor
                listProfe.append(persona)
            else:#administrador
                listAdmin.append(persona)
            return Mensajes.mensa["reg"]

    #devuelve 0 si es administrador, 1 si es estudiante, 2 si es profesor y -1 si no esta registrado
    @staticmethod
    def login(listEstu,listAdmin,listProfe,id,clave):
        for es in listAdmin:
            if((es.getIdentificacion() == id or es.getCorreo() == id) and es.getClave() == clave):
                return 0
        for es in listEstu:
            if((es.getIdentificacion() == id or es.getCorreo() == id) and es.getClave() == clave):
                return 1
        for pr in listProfe:
            if((pr.getIdentificacion() == id or pr.getCorreo() == id) and pr.getClave() == clave):
                return 2
        return -1

    @staticmethod
    def eliminar(lista,identificacion):
        per = Persona.buscar_persona(lista,identificacion)
        if(per):
            lista.remove(per)
            return Mensajes.mensa["eli"]
        else:
            return Mensajes.mensa["err"]

    @staticmethod
    def mostrar(lista):
        per = ""
        for i in lista:
            per += i.toString()+"\n"
        return per
