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
        Ma.cargar_materias(Main.materias)
        Main.crear_datos_ficticios()
        Main.principal()

    @staticmethod
    def crear_datos_ficticios():
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
                tip_usuario = Pe.login(Main.estudiantes,Main.administradores,Main.profesores,usu,con)
                if(tip_usuario != -1):
                    print(Me.mensa["bie"]+" "+Pe.buscar_persona(Main.estudiantes+Main.profesores+Main.administradores,usu).get_nombre())
                    if(tip_usuario == 0):
                        Main.menu_administrador()
                    elif(tip_usuario == 1):
                        Main.menu_estudiante()
                    elif(tip_usuario == 2):
                        Main.menu_profesor()
                else:
                    print(Me.mensa["err"])
            elif(op == 2):
                os._exit(0)

    @staticmethod
    def menu_administrador():
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
                        est = Pe.buscar_persona(Main.estudiantes,id)
                        if(est):
                            print(est.to_string())
                        else:
                            print(Me.mensa["err"])
                    elif(op == 6):
                        break
                    elif(op == 3):
                        id = input(Me.mensa["ide"]+" "+Me.mensa["o"]+" "+Me.mensa["cor"]+": ")
                        est = Pe.buscar_persona(Main.estudiantes,id)
                        if(est):
                            print("1. "+Me.mensa["nom"]+"\n2. "+Me.mensa["ide"]+"\n3. "+Me.mensa["cor"]+"\n4. "+Me.mensa["con"])
                            o = int(input())
                            if(o == 1):
                                nom = input(Me.mensa["nom"]+": ")
                                print(est.set_nombre(nom))
                            if(o == 2):
                                ide = input(Me.mensa["ide"]+": ")
                                print(est.set_identificacion(ide,Main.administradores+Main.estudiantes+Main.profesores))
                            if(o == 3):
                                cor = input(Me.mensa["cor"]+": ")
                                print(est.set_correo(cor,Main.administradores+Main.estudiantes+Main.profesores))
                            if(o == 4):
                                con = input(Me.mensa["con"]+": ")
                                print(est.set_clave(con))
                        else:
                            print(Me.mensa["err"])
                    elif(op == 4):
                        id = input(Me.mensa["ide"]+" "+Me.mensa["o"]+" "+Me.mensa["cor"]+": ")
                        print(Es.eliminar(id,Main.estudiantes,Main.notas,Main.matriculas))
                    elif(op == 5):
                        for est in Main.estudiantes:
                            print(est.to_string())
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
                        pro = Pe.buscar_persona(Main.profesores,id)
                        if(pro):
                            print(pro.to_string())
                        else:
                            print(Me.mensa["err"])
                    elif(op == 6):
                        break
                    elif(op == 3):
                        id = input(Me.mensa["ide"]+" "+Me.mensa["o"]+" "+Me.mensa["cor"]+": ")
                        pro = Pe.buscar_persona(Main.profesores,id)
                        if(pro):
                            print("1. "+Me.mensa["nom"]+"\n2. "+Me.mensa["ide"]+"\n3. "+Me.mensa["cor"]+"\n4. "+Me.mensa["con"])
                            o = int(input())
                            if(o == 1):
                                nom = input(Me.mensa["nom"]+": ")
                                print(pro.set_nombre(nom))
                            if(o == 2):
                                ide = input(Me.mensa["ide"]+": ")
                                print(pro.set_identificacion(ide,Main.administradores+Main.estudiantes+Main.profesores))
                            if(o == 3):
                                cor = input(Me.mensa["cor"]+": ")
                                print(pro.set_correo(cor,Main.administradores+Main.estudiantes+Main.profesores))
                            if(o == 4):
                                con = input(Me.mensa["con"]+": ")
                                print(pro.set_clave(con))
                        else:
                            print(Me.mensa["err"])
                    elif(op == 4):
                        id = input(Me.mensa["ide"]+" "+Me.mensa["o"]+" "+Me.mensa["cor"]+": ")
                        print(Pe.eliminar(Main.profesores,id))
                    elif(op == 5):
                        for pro in Main.profesores:
                            print(pro.to_string())
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
                        adm = Pe.buscar_persona(Main.administradores,id)
                        if(adm):
                            print(adm.to_string())
                        else:
                            print(Me.mensa["err"])
                    elif(op == 6):
                        break
                    elif(op == 3):
                        id = input(Me.mensa["ide"]+" "+Me.mensa["o"]+" "+Me.mensa["cor"]+": ")
                        adm = Pe.buscar_persona(Main.administradores,id)
                        if(adm):
                            print("1. "+Me.mensa["nom"]+"\n2. "+Me.mensa["ide"]+"\n3. "+Me.mensa["cor"]+"\n4. "+Me.mensa["con"])
                            o = int(input())
                            if(o == 1):
                                nom = input(Me.mensa["nom"]+": ")
                                print(adm.set_nombre(nom))
                            if(o == 2):
                                ide = input(Me.mensa["ide"]+": ")
                                print(adm.set_identificacion(ide,Main.administradores+Main.estudiantes+Main.profesores))
                            if(o == 3):
                                cor = input(Me.mensa["cor"]+": ")
                                print(adm.set_correo(cor,Main.administradores+Main.estudiantes+Main.profesores))
                            if(o == 4):
                                con = input(Me.mensa["con"]+": ")
                                print(adm.set_clave(con))
                        else:
                            print(Me.mensa["err"])
                    elif(op == 4):
                        id = input(Me.mensa["ide"]+" "+Me.mensa["o"]+" "+Me.mensa["cor"]+": ")
                        print(Pe.eliminar(Main.administradores,id))
                    elif(op == 5):
                        for adm in Main.administradores:
                            print(adm.to_string())
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
                        mat = Ma.buscar_materia(Main.materias,id)
                        if(mat):
                            print(mat.to_string())
                        else:
                            print(Me.mensa["err"])
                    elif(op == 3):
                        id = input(Me.mensa["id"]+": ")
                        mat = Ma.buscar_materia(Main.materias,id)
                        if(mat):
                            print("1. "+Me.mensa["id"]+"\n2. "+Me.mensa["nom"]+"\n3. "+Me.mensa["cre"])
                            o = int(input())
                            if(o == 1):
                                id = input(Me.mensa["id"]+": ")
                                print(mat.set_id(id,Main.materias))
                            elif(o == 2):
                                nom = input(Me.mensa["nom"]+": ")
                                print(mat.set_nombre(nom))
                            elif(o == 3):
                                cre = int(input(Me.mensa["cre"]+": "))
                                print(mat.set_creditos(cre))
                            Ma.guardar_cambios(Main.materias)
                        else:
                            print(Me.mensa["err"])
                    elif(op == 4):
                        id = input(Me.mensa["id"]+": ")
                        print(Ma.eliminar(id,Main.materias,Main.grupos,Main.matriculas,Main.notas))
                    elif(op == 5):
                        for mat in Main.materias:
                            print(mat.to_string())
                    elif(op == 6):
                        break
            elif(opc == 5):
                while(True):
                    print(Me.mensa["CASEGru"])
                    op = int(input())
                    if(op == 1):
                        num = input(Me.mensa["num"]+": ")
                        mat = Ma.buscar_materia(Main.materias,input(Me.mensa["id"]+" "+Me.mensa["mat"]+": "))
                        pro = pro = Pe.buscar_persona(Main.profesores,input(Me.mensa["idePro"]+": "))
                        gru = Gr(num,mat,pro)
                        print(Gr.registrar(gru,Main.grupos))
                    elif(op == 2):
                        num = input(Me.mensa["num"]+": ")
                        mat = input(Me.mensa["id"]+" "+Me.mensa["mat"]+": ")
                        gru = Gr.buscar_grupo(Main.grupos,num,mat)
                        if(gru):
                            print(gru.to_string())
                        else:
                            print(Me.mensa["err"])
                    elif(op == 3):
                        num = input(Me.mensa["num"]+": ")
                        mat = input(Me.mensa["id"]+" "+Me.mensa["mat"]+": ")
                        gru = Gr.buscar_grupo(Main.grupos,num,mat)
                        if(gru):
                            print("1. "+Me.mensa["num"]+"\n2. "+Me.mensa["mat"]+"\n3. "+Me.mensa["pro"])
                            o = int(input())
                            if(o == 1):
                                num = input(Me.mensa["num"]+": ")
                                print(gru.set_numero(num,mat,Main.grupos))
                            elif(o == 2):
                                mat = Ma.buscar_materia(Main.materias,input(Me.mensa["id"]+" "+Me.mensa["mat"]+": "))
                                print(gru.set_materia(mat))
                            elif(o == 3):
                                pro = Pe.buscar_persona(Main.profesores,input(Me.mensa["idePro"]+": "))
                                print(gru.set_profesor(pro))
                        else:
                            print(Me.mensa["err"])
                    elif(op == 4):
                        num = input(Me.mensa["num"]+": ")
                        mat = input(Me.mensa["id"]+" "+Me.mensa["mat"]+": ")
                        gru = Gr.buscar_grupo(Main.grupos,num,mat)
                        print(Gr.eliminar(Main.grupos,num,mat,Main.matriculas,Main.notas))
                    elif(op == 5):
                        for gru in Main.grupos:
                            print(gru.to_string())
                    elif(op == 6):
                        mat = input(Me.mensa["id"]+" "+Me.mensa["mat"]+": ")
                        for gru in Main.grupos:
                            if(gru.get_materia().get_id() == mat):
                                print(gru.to_string())
                    elif(op == 7):
                        break

    @staticmethod
    def menu_estudiante():
        None

    @staticmethod
    def menu_profesor():
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
