from Mensajes import Mensajes as Me
from Materia import Materia as Ma
from Grupo import Grupo as Gr
from Matricula import Matricula as M
from Persona import Persona as Pe
from Profesor import Profesor as Pr
from Estudiante import Estudiante as Es
from Nota import Nota as No
import os

class Main:

    materias = []
    grupos = []
    matriculas = []
    estudiantes = []
    profesores = []
    administradores = []
    notas = []

    @staticmethod
    def run():
        Ma.cargarMaterias(Main.materias)
        Main.crearDatosFicticios()
        Main.principal()

    @staticmethod
    def crearDatosFicticios():
        #Materia
        if(len(Main.materias) == 0):
            Ma.registrar(Ma(1,"Programación Orientada a Objetos",3),Main.materias)
        if(len(Main.materias) == 1):
            Ma.registrar(Ma(2,"Calculo Diferencial",4),Main.materias)
        mat1 = Main.materias[0]
        mat2 = Main.materias[1]
        #Administrador
        ad1 = Pe("Mark Zuckaritas","198","mark@unal.edu.co","face")
        Pe.registrar(Main.estudiantes,Main.administradores,Main.profesores,ad1)
        ad2 = Pe("Steve Jobs","111","job@unal.edu.co","micro")
        Pe.registrar(Main.estudiantes,Main.administradores,Main.profesores,ad2)
        #Profesor
        pr1 = Pr("Jose Gregorio Guardia","123","jgre@unal.edu.co","hola")
        Pr.registrar(Main.estudiantes,Main.administradores,Main.profesores,pr1)
        pr2 = Pr("Pablo Antoño Ortiz","456","pano@unal.edu.co","chao")
        Pr.registrar(Main.estudiantes,Main.administradores,Main.profesores,pr2)
        #Estudiante
        es1 = Es("Juan Pablo Moya Alarcón","789","jmoya@unal.edu.co","clave")
        Es.registrar(Main.estudiantes,Main.administradores,Main.profesores,es1)
        es2 = Es("Julian Ospina Murguetio","135","jospm@unal.edu.co","anime")
        Es.registrar(Main.estudiantes,Main.administradores,Main.profesores,es2)
        es3 = Es("Juan Diego Marin Rogriguez","246","platano@unal.edu.co","banano")
        Es.registrar(Main.estudiantes,Main.administradores,Main.profesores,es3)
        es4 = Es("Juan Felipe Usuga Munera","791","jfusum@unal.edu.co","1234")
        Es.registrar(Main.estudiantes,Main.administradores,Main.profesores,es4)
        #Grupo
        gr1 = Gr("1",mat1,pr2)
        Gr.registrar(gr1,Main.grupos)
        gr2 = Gr("2",mat1,pr2)
        Gr.registrar(gr2,Main.grupos)
        gr3 = Gr("1",mat2,pr1)
        Gr.registrar(gr3,Main.grupos)
        #Matricula
        M.matricular(Main.matriculas,M(3,es1,gr1))
        M.matricular(Main.matriculas,M(2,es2,gr1))
        M.matricular(Main.matriculas,M(4,es3,gr2))
        M.matricular(Main.matriculas,M(3,es4,gr2))
        M.matricular(Main.matriculas,M(3,es1,gr3))
        M.matricular(Main.matriculas,M(2,es2,gr3))
        M.matricular(Main.matriculas,M(4,es3,gr3))
        #Nota
        n1 = No(33,5,1,es1,gr1)
        n2 = No(33,4,2,es1,gr1)
        n3 = No(34,3,3,es1,gr1)
        No.registrar(n1,Main.notas)
        No.registrar(n2,Main.notas)
        No.registrar(n3,Main.notas)
        n4 = No(33,1.3,1,es2,gr1)
        n5 = No(33,3,2,es2,gr1)
        n6 = No(34,4.5,3,es2,gr1)
        No.registrar(n4,Main.notas)
        No.registrar(n5,Main.notas)
        No.registrar(n6,Main.notas)
        n7 = No(33,1.7,1,es3,gr2)
        n8 = No(33,4,2,es3,gr2)
        n9 = No(34,3.6,3,es3,gr2)
        No.registrar(n7,Main.notas)
        No.registrar(n8,Main.notas)
        No.registrar(n9,Main.notas)
         
    @staticmethod
    def principal():
        while(True):
            op = int(input(Me.mensa["opc1"]))
            if(op == 1):
                usu = str(input(Me.mensa["ing Usu"]))
                con = str(input(Me.mensa["ing Con"]))
                tipUsuario = Pe.login(Main.estudiantes,Main.administradores,Main.profesores,usu,con)
                if(tipUsuario != -1):
                    print(Me.mensa["bie"]+" "+Pe.buscarPersona(Main.estudiantes+Main.profesores+Main.administradores,usu).getNombre())
                    if(tipUsuario == 0):
                        Main.menuAdministrador()
                    elif(tipUsuario == 1):
                        Main.menuEstudiante()
                    elif(tipUsuario == 2):
                        Main.menuProfesor()
                else:
                    print(Me.mensa["err"])
            elif(op == 2):
                os._exit(0)

    @staticmethod
    def menuAdministrador():
        while True:
            opc = int(input(Me.mensa["opcAdmin"]))
            if(opc == 6):
                break
            elif(opc == 1):
                while True:
                    print(Me.mensa["CASE"])
                    op = int(input())
                    if(op == 1):
                        nom = input(Me.mensa["nom"]+": ")
                        ide = input(Me.mensa["ide"]+": ")
                        cor = input(Me.mensa["cor"]+": ")
                        con = input(Me.mensa["con"]+": ")
                        est = Es(nom,ide,cor,con)
                        print(Es.registrar(Main.estudiantes,Main.administradores,Main.profesores,est))
                    elif(op == 2):
                        id = input(Me.mensa["ide"]+" "+Me.mensa["o"]+" "+Me.mensa["cor"]+": ")
                        est = Pe.buscarPersona(Main.estudiantes,id)
                        if(est):
                            print(est.toString())
                        else:
                            print(Me.mensa["err"])
                    elif(op == 6):
                        break
                    elif(op == 3):
                        id = input(Me.mensa["ide"]+" "+Me.mensa["o"]+" "+Me.mensa["cor"]+": ")
                        est = Pe.buscarPersona(Main.estudiantes,id)
                        if(est):
                            print("1. "+Me.mensa["nom"]+"\n2. "+Me.mensa["ide"]+"\n3. "+Me.mensa["cor"]+"\n4. "+Me.mensa["con"])
                            o = int(input())
                            if(o == 1):
                                nom = input(Me.mensa["nom"]+": ")
                                print(est.setNombre(nom))
                            if(o == 2):
                                ide = input(Me.mensa["ide"]+": ")
                                print(est.setIdentificacion(ide,Main.administradores+Main.estudiantes+Main.profesores))
                            if(o == 3):
                                cor = input(Me.mensa["cor"]+": ")
                                print(est.setCorreo(cor,Main.administradores+Main.estudiantes+Main.profesores))
                            if(o == 4):
                                con = input(Me.mensa["con"]+": ")
                                print(est.setClave(con))
                        else:
                            print(Me.mensa["err"])
                    elif(op == 4):
                        id = input(Me.mensa["ide"]+" "+Me.mensa["o"]+" "+Me.mensa["cor"]+": ")
                        print(Es.eliminar(id,Main.estudiantes,Main.notas,Main.matriculas))
                    elif(op == 5):
                        for est in Main.estudiantes:
                            print(est.toString())
            elif(opc == 2):
                while True:
                    print(Me.mensa["CASE"])
                    op = int(input())
                    if(op == 1):
                        nom = input(Me.mensa["nom"]+": ")
                        ide = input(Me.mensa["ide"]+": ")
                        cor = input(Me.mensa["cor"]+": ")
                        con = input(Me.mensa["con"]+": ")
                        pro = Pr(nom,ide,cor,con)
                        print(Pr.registrar(Main.estudiantes,Main.administradores,Main.profesores,pro))
                    elif(op == 2):
                        id = input(Me.mensa["ide"]+" "+Me.mensa["o"]+" "+Me.mensa["cor"]+": ")
                        pro = Pe.buscarPersona(Main.profesores,id)
                        if(pro):
                            print(pro.toString())
                        else:
                            print(Me.mensa["err"])
                    elif(op == 6):
                        break
                    elif(op == 3):
                        id = input(Me.mensa["ide"]+" "+Me.mensa["o"]+" "+Me.mensa["cor"]+": ")
                        pro = Pe.buscarPersona(Main.profesores,id)
                        if(pro):
                            print("1. "+Me.mensa["nom"]+"\n2. "+Me.mensa["ide"]+"\n3. "+Me.mensa["cor"]+"\n4. "+Me.mensa["con"])
                            o = int(input())
                            if(o == 1):
                                nom = input(Me.mensa["nom"]+": ")
                                print(pro.setNombre(nom))
                            if(o == 2):
                                ide = input(Me.mensa["ide"]+": ")
                                print(pro.setIdentificacion(ide,Main.administradores+Main.estudiantes+Main.profesores))
                            if(o == 3):
                                cor = input(Me.mensa["cor"]+": ")
                                print(pro.setCorreo(cor,Main.administradores+Main.estudiantes+Main.profesores))
                            if(o == 4):
                                con = input(Me.mensa["con"]+": ")
                                print(pro.setClave(con))
                        else:
                            print(Me.mensa["err"])
                    elif(op == 4):
                        id = input(Me.mensa["ide"]+" "+Me.mensa["o"]+" "+Me.mensa["cor"]+": ")
                        print(Pe.eliminar(Main.profesores,id))
                    elif(op == 5):
                        for pro in Main.profesores:
                            print(pro.toString())
            elif(opc == 3):
                while(True):
                    print(Me.mensa["CASE"])
                    op = int(input())
                    if(op == 1):
                        nom = input(Me.mensa["nom"]+": ")
                        ide = input(Me.mensa["ide"]+": ")
                        cor = input(Me.mensa["cor"]+": ")
                        con = input(Me.mensa["con"]+": ")
                        adm = Pe(nom,ide,cor,con)
                        print(Pe.registrar(Main.estudiantes,Main.administradores,Main.profesores,adm))
                    elif(op == 2):
                        id = input(Me.mensa["ide"]+" "+Me.mensa["o"]+" "+Me.mensa["cor"]+": ")
                        adm = Pe.buscarPersona(Main.administradores,id)
                        if(adm):
                            print(adm.toString())
                        else:
                            print(Me.mensa["err"])
                    elif(op == 6):
                        break
                    elif(op == 3):
                        id = input(Me.mensa["ide"]+" "+Me.mensa["o"]+" "+Me.mensa["cor"]+": ")
                        adm = Pe.buscarPersona(Main.administradores,id)
                        if(adm):
                            print("1. "+Me.mensa["nom"]+"\n2. "+Me.mensa["ide"]+"\n3. "+Me.mensa["cor"]+"\n4. "+Me.mensa["con"])
                            o = int(input())
                            if(o == 1):
                                nom = input(Me.mensa["nom"]+": ")
                                print(adm.setNombre(nom))
                            if(o == 2):
                                ide = input(Me.mensa["ide"]+": ")
                                print(adm.setIdentificacion(ide,Main.administradores+Main.estudiantes+Main.profesores))
                            if(o == 3):
                                cor = input(Me.mensa["cor"]+": ")
                                print(adm.setCorreo(cor,Main.administradores+Main.estudiantes+Main.profesores))
                            if(o == 4):
                                con = input(Me.mensa["con"]+": ")
                                print(adm.setClave(con))
                        else:
                            print(Me.mensa["err"])
                    elif(op == 4):
                        id = input(Me.mensa["ide"]+" "+Me.mensa["o"]+" "+Me.mensa["cor"]+": ")
                        print(Pe.eliminar(Main.administradores,id))
                    elif(op == 5):
                        for adm in Main.administradores:
                            print(adm.toString())
            elif(opc == 4):
                while(True):
                    print(Me.mensa["CASE"])
                    op = int(input())
                    if(op == 1):
                        id = input(Me.mensa["id"]+": ")
                        nom = input(Me.mensa["nom"]+": ")
                        cre = int(input(Me.mensa["cre"]+": "))
                        mat = Ma(id,nom,cre)
                        print(Ma.registrar(mat,Main.materias))
                    elif(op == 2):
                        id = input(Me.mensa["id"]+": ")
                        mat = Ma.buscarMateria(Main.materias,id)
                        if(mat):
                            print(mat.toString())
                        else:
                            print(Me.mensa["err"])
                    elif(op == 3):
                        id = input(Me.mensa["id"]+": ")
                        mat = Ma.buscarMateria(Main.materias,id)
                        if(mat):
                            print("1. "+Me.mensa["id"]+"\n2. "+Me.mensa["nom"]+"\n3. "+Me.mensa["cre"])
                            o = int(input())
                            if(o == 1):
                                id = input(Me.mensa["id"]+": ")
                                print(mat.setId(id,Main.materias))
                            elif(o == 2):
                                nom = input(Me.mensa["nom"]+": ")
                                print(mat.setNombre(nom))
                            elif(o == 3):
                                cre = int(input(Me.mensa["cre"]+": "))
                                print(mat.setCreditos(cre))
                            Ma.guardarCambios(Main.materias)
                        else:
                            print(Me.mensa["err"])
                    elif(op == 4):
                        id = input(Me.mensa["id"]+": ")
                        print(Ma.eliminar(id,Main.materias,Main.grupos,Main.matriculas,Main.notas))
                    elif(op == 5):
                        for mat in Main.materias:
                            print(mat.toString())
                    elif(op == 6):
                        break
            elif(opc == 5):
                while(True):
                    print(Me.mensa["CASEGru"])
                    op = int(input())
                    if(op == 1):
                        num = input(Me.mensa["num"]+": ")
                        mat = Ma.buscarMateria(Main.materias,input(Me.mensa["id"]+" "+Me.mensa["mat"]+": "))
                        pro = pro = Pe.buscarPersona(Main.profesores,input(Me.mensa["idePro"]+": "))
                        gru = Gr(num,mat,pro)
                        print(Gr.registrar(gru,Main.grupos))
                    elif(op == 2):
                        num = input(Gr.mensa["num"]+": ")
                        mat = input(Me.mensa["id"]+" "+Me.mensa["mat"]+": ")
                        gru = Gr.buscarGrupo(Main.grupos,num,mat)
                        if(gru):
                            print(gru.toString())
                        else:
                            print(Me.mensa["err"])
                    elif(op == 3):
                        num = input(Me.mensa["num"]+": ")
                        mat = input(Me.mensa["id"]+" "+Me.mensa["mat"]+": ")
                        gru = Gr.buscarGrupo(Main.grupos,num,mat)
                        if(gru):
                            print("1. "+Me.mensa["num"]+"\n2. "+Me.mensa["mat"]+"\n3. "+Me.mensa["pro"])
                            o = int(input())
                            if(o == 1):
                                num = input(Me.mensa["num"]+": ")
                                print(gru.setNumero(num,mat,Main.grupos))
                            elif(o == 2):
                                mat = Ma.buscarMateria(Main.materias,input(Me.mensa["id"]+" "+Me.mensa["mat"]+": "))
                                print(gru.setMateria(mat))
                            elif(o == 3):
                                pro = Pe.buscarPersona(Main.profesores,input(Me.mensa["idePro"]+": "))
                                print(gru.setProfesor(pro))
                        else:
                            print(Me.mensa["err"])
                    elif(op == 4):
                        num = input(Gr.mensa["num"]+": ")
                        mat = input(Me.mensa["id"]+" "+Me.mensa["mat"]+": ")
                        gru = Gr.buscarGrupo(Main.grupos,num,mat)
                        print(Gr.eliminar(Main.grupos,num,mat,Main.matriculas,Main.notas))
                    elif(op == 5):
                        for gru in Main.grupos:
                            print(gru.toString())
                    elif(op == 6):
                        mat = input(Me.mensa["id"]+" "+Me.mensa["mat"]+": ")
                        for gru in Main.grupos:
                            if(gru.getMateria().getId() == mat):
                                print(gru.toString())
                    elif(op == 7):
                        break

    @staticmethod
    def menuEstudiante():
        None

    @staticmethod
    def menuProfesor():
        None


if __name__ == "__main__":
    print(Me.esp["idi"])
    print(Me.ing["idi"])
    idi = input()
    if(idi == "1"):
        Me.mensa = Me.esp
    else:
        Me.mensa = Me.ing
    Main.run()