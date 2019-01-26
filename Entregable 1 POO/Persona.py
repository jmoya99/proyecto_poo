from Mensajes import Mensajes

class Persona:

    def __init__(self,nombre,identificacion,correo,clave):
        self.set_nombre(nombre)
        self.set_identificacion(identificacion)
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

    def get_identificacion(self):
        return self._identificacion

    def set_correo(self,correo,lista = None):
        if(not lista):
            lista = []
        if(correo):
            if(not Persona.buscar_persona(lista,correo)):
                self._correo = correo
                return Mensajes.mensa["mod"]
        return Mensajes.mensa["err"]

    def get_correo(self):
        return self._correo

    def set_clave(self,clave):
        if(clave):
            self._clave = clave
            return Mensajes.mensa["mod"]
        return Mensajes.mensa["err"]

    def get_clave(self):
        return self._clave

    def to_string(self):
        return "{0}({1}: {2},{3}: {4},{5}: {6},{7}: {8})".format(
        Mensajes.mensa["usu"],
        Mensajes.mensa["nom"],
        self.get_nombre(),
        Mensajes.mensa["ide"],
        self.get_identificacion(),
        Mensajes.mensa["cor"],
        self.get_correo(),
        Mensajes.mensa["con"],
        self.get_clave())

    @staticmethod
    def buscar_persona(list_personas,id):
        for p in list_personas:
            if((p.get_identificacion() == id or p.get_correo() == id) and id):
                return p
        return None

    @staticmethod
    def registrar(list_estu,list_admin,list_profe,persona,tip=-1):
        #tip se refiere al tipo de usuario que es
        if(Persona.buscar_persona(list_admin+list_estu+list_profe,
        persona.get_identificacion())):
            return Mensajes.mensa["err"]
        else:
            if(tip == 0):#estudiante
                list_estu.append(persona)
            elif(tip == 1):#profesor
                list_profe.append(persona)
            else:#administrador
                list_admin.append(persona)
            return Mensajes.mensa["reg"]

    '''
    devuelve 0 si es administrador, 1 si es estudiante,
    2 si es profesor y -1 si no esta registrado
    '''
    @staticmethod
    def login(list_estu,list_admin,list_profe,id,clave):
        for es in list_admin:
            if((es.get_identificacion() == id or es.get_correo() == id)
            and es.get_clave() == clave):
                return 0
        for es in list_estu:
            if((es.get_identificacion() == id or es.get_correo() == id)
            and es.get_clave() == clave):
                return 1
        for pr in list_profe:
            if((pr.get_identificacion() == id or pr.get_correo() == id)
            and pr.get_clave() == clave):
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
