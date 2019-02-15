from Mensajes import Mensajes as Me
from Materia import Materia as Ma
from Grupo import Grupo as Gr
from Matricula import Matricula as M
from Persona import Persona as Pe
from Profesor import Profesor as Pr
from Estudiante import Estudiante as Es
from Nota import Nota as No
from Operaciones import Operaciones as Op
from random import *
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
        # Materia
        if(len(Main.materias) == 0):
            Ma.registrar(
                Ma(1, "Programación Orientada a Objetos", 3), Main.materias)
        if(len(Main.materias) == 1):
            num = 2
            if(Ma.buscar_materia(Main.materias, 2)):
                num = 1
            Ma.registrar(Ma(num, "Calculo Diferencial", 4), Main.materias)
        mat1 = Main.materias[0]
        mat2 = Main.materias[1]
        # Administrador
        ad1 = Pe("Mark Zuckaritas", "198", "mark@unal.edu.co", "face")
        Pe.registrar(Main.estudiantes, Main.administradores,
                     Main.profesores, ad1)
        ad2 = Pe("Steve Jobs", "111", "job@unal.edu.co", "micro")
        Pe.registrar(Main.estudiantes, Main.administradores,
                     Main.profesores, ad2)
        # Profesor
        pr1 = Pr("Jose Gregorio Guardia", "123", "jgre@unal.edu.co", "hola")
        Pr.registrar(Main.estudiantes, Main.administradores,
                     Main.profesores, pr1)
        pr2 = Pr("Pablo Antoño Ortiz", "456", "pano@unal.edu.co", "chao")
        Pr.registrar(Main.estudiantes, Main.administradores,
                     Main.profesores, pr2)
        # Estudiante
        es1 = Es("Juan Pablo Moya Alarcón", "789",
                 "jmoya@unal.edu.co", "clave")
        Es.registrar(Main.estudiantes, Main.administradores,
                     Main.profesores, es1)
        es2 = Es("Julian Ospina Murguetio", "135",
                 "juospinam@unal.edu.co", "anime")
        Es.registrar(Main.estudiantes, Main.administradores,
                     Main.profesores, es2)
        es3 = Es("Juan Diego Marin Rogriguez", "246",
                 "jumarinr@unal.edu.co", "banano")
        Es.registrar(Main.estudiantes, Main.administradores,
                     Main.profesores, es3)
        es4 = Es("Juan Felipe Usuga Villegas",
                 "791", "jusugav@unal.edu.co", "1234")
        Es.registrar(Main.estudiantes, Main.administradores,
                     Main.profesores, es4)
        # Grupo
        gr1 = Gr("1", mat1, pr2)
        Gr.registrar(gr1, Main.grupos)
        gr2 = Gr("2", mat1, pr2)
        Gr.registrar(gr2, Main.grupos)
        gr3 = Gr("1", mat2, pr1)
        Gr.registrar(gr3, Main.grupos)
        # Matricula
        M.matricular(Main.matriculas, M(3, es1, gr1))
        M.matricular(Main.matriculas, M(2, es2, gr1))
        M.matricular(Main.matriculas, M(4, es3, gr2))
        M.matricular(Main.matriculas, M(3, es4, gr2))
        M.matricular(Main.matriculas, M(3, es1, gr3))
        M.matricular(Main.matriculas, M(2, es2, gr3))
        M.matricular(Main.matriculas, M(4, es3, gr3))
        # Nota
        n1 = No(33, 5, 1, es1, gr1)
        n2 = No(33, 4, 2, es1, gr1)
        n3 = No(34, 3, 3, es1, gr1)
        No.registrar(n1, Main.notas)
        No.registrar(n2, Main.notas)
        No.registrar(n3, Main.notas)
        n4 = No(33, 1.3, 1, es2, gr1)
        n5 = No(33, 3, 2, es2, gr1)
        n6 = No(34, 4.5, 3, es2, gr1)
        No.registrar(n4, Main.notas)
        No.registrar(n5, Main.notas)
        No.registrar(n6, Main.notas)
        n7 = No(33, 1.7, 1, es3, gr2)
        n8 = No(33, 4, 2, es3, gr2)
        n9 = No(34, 3.6, 3, es3, gr2)
        No.registrar(n7, Main.notas)
        No.registrar(n8, Main.notas)
        No.registrar(n9, Main.notas)

    @staticmethod
    def principal():
        while(True):
            op = int(input(Me.mensa["opc1"]))
            if(op == 1):
                usu = str(input(Me.mensa["ing Usu"]))
                con = str(input(Me.mensa["ing Con"]))
                tip_usuario = Pe.login(
                    Main.estudiantes, Main.administradores, Main.profesores, usu, con)
                if(tip_usuario != -1):
                    print(Me.mensa["bie"] + " " + Pe.buscar_persona(Main.estudiantes
                                                                    + Main.profesores + Main.administradores, usu).get_nombre())
                    if(tip_usuario == 0):
                        Main.menu_administrador()
                    elif(tip_usuario == 1):
                        Main.menu_estudiante(
                            Pe.buscar_persona(Main.estudiantes, usu))
                    elif(tip_usuario == 2):
                        Main.menu_profesor(Pe.buscar_persona(Main.estudiantes
                                                             + Main.profesores + Main.administradores, usu))
                else:
                    print(Me.mensa["err"])
            elif(op == 2):
                os._exit(0)
            elif(op == 3):

                Main.recuperar_contrasena()

    @staticmethod
    def recuperar_contrasena():
        usu = str(input(Me.mensa["ing Usu"]))
        usuario = Pe.buscar_persona(
            Main.administradores + Main.estudiantes + Main.profesores, usu)
        if(usuario):
            cod = ""
            for i in range(0, 4):

                cod += str(randrange(10)) + \
                    choice("qwertyuiopasdfghjklñzxcvbnm")
            Op.enviar_correo_electronico(
                usuario.get_correo(), Me.mensa["recu"], Me.mensa["codi"] + cod)
            codigo = input(Me.mensa["codi"])
            if(codigo == cod):
                contraseña = input(Me.mensa["nuecon"])
                print(usuario.set_clave(contraseña))
            else:
                print(Me.mensa["err"])
        else:
            print(Me.mensa["err"])

    @staticmethod
    def generar_reporte_en_excel():
        matt = Ma.buscar_materia(
            Main.materias, input(Me.mensa["ideMate"]))

        if matt:
            titulo = "Reporte de " + matt.get_nombre()
            cabecera = (
                "Materia", "Grupo", "Nombre del Estudiante", "Nota", "Porcentaje")
            registros = []
            nombreEXCEL = "Reporte de " + matt.get_nombre()

            notes_filter = list(filter(lambda nota: list(map(lambda grupo: grupo.get_numero(
            ) == nota.get_grupo().get_numero(), matt.get_grupos())), Main.notas))

            for nota in notes_filter:
                registros.append((matt.get_nombre(), nota.get_grupo().get_numero(), nota.get_estudiante(
                ).get_nombre(), nota.get_valor(), nota.get_porcentaje()))

            # Generación del excel
            Op.exportar_excel(
                titulo, cabecera, registros, nombreEXCEL)
            print(Me.mensa["reporte"])
        else:
            print(Me.mensa["noenc"])

    @staticmethod
    def menu_administrador():
        while True:
            opc = int(input(Me.mensa["opcAdmin"]))
            if(opc == 6):
                break
            elif(opc == 1):
                while True:
                    print(Me.mensa["CASEest"])
                    op = int(input())
                    if(op == 1):
                        nom = input(Me.mensa["nom"] + ": ")
                        ide = input(Me.mensa["ide"] + ": ")
                        cor = input(Me.mensa["cor"] + ": ")
                        con = input(Me.mensa["con"] + ": ")
                        est = Es(nom, ide, cor, con)
                        print(Es.registrar(Main.estudiantes,
                                           Main.administradores, Main.profesores, est))
                    elif(op == 2):
                        id = input(
                            Me.mensa["ide"] + " " + Me.mensa["o"] + " " + Me.mensa["cor"] + ": ")
                        est = Pe.buscar_persona(Main.estudiantes, id)
                        if(est):
                            print(est.to_string())
                        else:
                            print(Me.mensa["err"])
                    elif(op == 7):
                        break
                    elif(op == 3):
                        id = input(
                            Me.mensa["ide"] + " " + Me.mensa["o"] + " " + Me.mensa["cor"] + ": ")
                        est = Pe.buscar_persona(Main.estudiantes, id)
                        if(est):
                            print("1. " + Me.mensa["nom"] + "\n2. " + Me.mensa["ide"]
                                  + "\n3. " + Me.mensa["cor"] + "\n4. " + Me.mensa["con"])
                            o = int(input())
                            if(o == 1):
                                nom = input(Me.mensa["nom"] + ": ")
                                print(est.set_nombre(nom))
                            if(o == 2):
                                ide = input(Me.mensa["ide"] + ": ")
                                print(est.set_identificacion(
                                    ide, Main.administradores + Main.estudiantes + Main.profesores))
                            if(o == 3):
                                cor = input(Me.mensa["cor"] + ": ")
                                print(est.set_correo(
                                    cor, Main.administradores + Main.estudiantes + Main.profesores))
                            if(o == 4):
                                con = input(Me.mensa["con"] + ": ")
                                print(est.set_clave(con))
                        else:
                            print(Me.mensa["err"])
                    elif(op == 4):
                        id = input(
                            Me.mensa["ide"] + " " + Me.mensa["o"] + " " + Me.mensa["cor"] + ": ")
                        print(Es.eliminar(id, Main.estudiantes,
                                          Main.notas, Main.matriculas))
                    elif(op == 5):
                        for est in Main.estudiantes:
                            print(est.to_string())
                    elif(op == 6):
                        for i in Main.materias:
                            print("__________________________")
                            print(Me.mensa["ideMate"], i.get_id())
<<<<<<< HEAD
                            print(van_perdiendo(i))
=======
                            n = i.get_grupos()
                            if(len(n) != 0):
                                for j in n:
                                    m = j.get_matricula()
                                    if(len(m) != 0):
                                        for k in m:
                                            o = k.get_estudiante().get_nota()
                                            if(len(o) != 0):
                                                sum = 0
                                                sum2 = 0
                                                for l in o:
                                                    sum += ((l.get_porcentaje() / 100) *
                                                            l.get_valor())
                                                    sum2 += (l.get_porcentaje() / 100)
                                                prom = sum / sum2
                                                if(prom < 3):
                                                    print(k.get_estudiante().get_identificacion(
                                                    ), k.get_estudiante().get_nombre())
                                            else:
                                                print(Me.mensa["Noestnot"])
                                                print(
                                                    "__________________________")
                                    else:
                                        print(Me.mensa["Nomatric"])
                                        print("__________________________")
                            else:
                                print(Me.mensa["Nogrup"])
                                print("__________________________")
>>>>>>> 4c2f28583f5905a6c96e945006ff977613b40fdc

            elif(opc == 2):
                while True:
                    print(Me.mensa["CASE"])
                    op = int(input())
                    if(op == 1):
                        nom = input(Me.mensa["nom"] + ": ")
                        ide = input(Me.mensa["ide"] + ": ")
                        cor = input(Me.mensa["cor"] + ": ")
                        con = input(Me.mensa["con"] + ": ")
                        pro = Pr(nom, ide, cor, con)
                        print(Pr.registrar(Main.estudiantes,
                                           Main.administradores, Main.profesores, pro))
                    elif(op == 2):
                        id = input(
                            Me.mensa["ide"] + " " + Me.mensa["o"] + " " + Me.mensa["cor"] + ": ")
                        pro = Pe.buscar_persona(Main.profesores, id)
                        if(pro):
                            print(pro.to_string())
                        else:
                            print(Me.mensa["err"])
                    elif(op == 6):
                        break
                    elif(op == 3):
                        id = input(
                            Me.mensa["ide"] + " " + Me.mensa["o"] + " " + Me.mensa["cor"] + ": ")
                        pro = Pe.buscar_persona(Main.profesores, id)
                        if(pro):
                            print("1. " + Me.mensa["nom"] + "\n2. " + Me.mensa["ide"]
                                  + "\n3. " + Me.mensa["cor"] + "\n4. " + Me.mensa["con"])
                            o = int(input())
                            if(o == 1):
                                nom = input(Me.mensa["nom"] + ": ")
                                print(pro.set_nombre(nom))
                            if(o == 2):
                                ide = input(Me.mensa["ide"] + ": ")
                                print(pro.set_identificacion(
                                    ide, Main.administradores + Main.estudiantes + Main.profesores))
                            if(o == 3):
                                cor = input(Me.mensa["cor"] + ": ")
                                print(pro.set_correo(
                                    cor, Main.administradores + Main.estudiantes + Main.profesores))
                            if(o == 4):
                                con = input(Me.mensa["con"] + ": ")
                                print(pro.set_clave(con))
                        else:
                            print(Me.mensa["err"])
                    elif(op == 4):
                        id = input(
                            Me.mensa["ide"] + " " + Me.mensa["o"] + " " + Me.mensa["cor"] + ": ")
                        print(Pe.eliminar(Main.profesores, id))
                    elif(op == 5):
                        for pro in Main.profesores:
                            print(pro.to_string())
            elif(opc == 3):
                while(True):
                    print(Me.mensa["CASE"])
                    op = int(input())
                    if(op == 1):
                        nom = input(Me.mensa["nom"] + ": ")
                        ide = input(Me.mensa["ide"] + ": ")
                        cor = input(Me.mensa["cor"] + ": ")
                        con = input(Me.mensa["con"] + ": ")
                        adm = Pe(nom, ide, cor, con)
                        print(Pe.registrar(Main.estudiantes,
                                           Main.administradores, Main.profesores, adm))
                    elif(op == 2):
                        id = input(
                            Me.mensa["ide"] + " " + Me.mensa["o"] + " " + Me.mensa["cor"] + ": ")
                        adm = Pe.buscar_persona(Main.administradores, id)
                        if(adm):
                            print(adm.to_string())
                        else:
                            print(Me.mensa["err"])
                    elif(op == 6):
                        break
                    elif(op == 3):
                        id = input(
                            Me.mensa["ide"] + " " + Me.mensa["o"] + " " + Me.mensa["cor"] + ": ")
                        adm = Pe.buscar_persona(Main.administradores, id)
                        if(adm):
                            print("1. " + Me.mensa["nom"] + "\n2. " + Me.mensa["ide"]
                                  + "\n3. " + Me.mensa["cor"] + "\n4. " + Me.mensa["con"])
                            o = int(input())
                            if(o == 1):
                                nom = input(Me.mensa["nom"] + ": ")
                                print(adm.set_nombre(nom))
                            if(o == 2):
                                ide = input(Me.mensa["ide"] + ": ")
                                print(adm.set_identificacion(
                                    ide, Main.administradores + Main.estudiantes + Main.profesores))
                            if(o == 3):
                                cor = input(Me.mensa["cor"] + ": ")
                                print(adm.set_correo(
                                    cor, Main.administradores + Main.estudiantes + Main.profesores))
                            if(o == 4):
                                con = input(Me.mensa["con"] + ": ")
                                print(adm.set_clave(con))
                        else:
                            print(Me.mensa["err"])
                    elif(op == 4):
                        id = input(
                            Me.mensa["ide"] + " " + Me.mensa["o"] + " " + Me.mensa["cor"] + ": ")
                        print(Pe.eliminar(Main.administradores, id))
                    elif(op == 5):
                        for adm in Main.administradores:
                            print(adm.to_string())
            elif(opc == 4):
                while(True):
                    print(Me.mensa["CASE"])
                    op = int(input())
                    if(op == 1):
                        id = input(Me.mensa["id"] + ": ")
                        nom = input(Me.mensa["nom"] + ": ")
                        cre = int(input(Me.mensa["cre"] + ": "))
                        mat = Ma(id, nom, cre)
                        print(Ma.registrar(mat, Main.materias))
                    elif(op == 2):
                        id = input(Me.mensa["id"] + ": ")
                        mat = Ma.buscar_materia(Main.materias, id)
                        if(mat):
                            print(mat.to_string())
                        else:
                            print(Me.mensa["err"])
                    elif(op == 3):
                        id = input(Me.mensa["id"] + ": ")
                        mat = Ma.buscar_materia(Main.materias, id)
                        if(mat):
                            print(
                                "1. " + Me.mensa["id"] + "\n2. " + Me.mensa["nom"] + "\n3. " + Me.mensa["cre"])
                            o = int(input())
                            if(o == 1):
                                id = input(Me.mensa["id"] + ": ")
                                print(mat.set_id(id, Main.materias))
                            elif(o == 2):
                                nom = input(Me.mensa["nom"] + ": ")
                                print(mat.set_nombre(nom))
                            elif(o == 3):
                                cre = int(input(Me.mensa["cre"] + ": "))
                                print(mat.set_creditos(cre))
                            Ma.guardar_cambios(Main.materias)
                        else:
                            print(Me.mensa["err"])
                    elif(op == 4):
                        id = input(Me.mensa["id"] + ": ")
                        print(Ma.eliminar(id, Main.materias,
                                          Main.grupos, Main.matriculas, Main.notas))
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
                        num = input(Me.mensa["num"] + ": ")
                        mat = Ma.buscar_materia(Main.materias, input(
                            Me.mensa["id"] + " " + Me.mensa["mat"] + ": "))
                        pro = pro = Pe.buscar_persona(
                            Main.profesores, input(Me.mensa["idePro"] + ": "))
                        gru = Gr(num, mat, pro)
                        print(Gr.registrar(gru, Main.grupos))
                    elif(op == 2):
                        num = input(Me.mensa["num"] + ": ")
                        mat = input(Me.mensa["id"] + " "
                                    + Me.mensa["mat"] + ": ")
                        gru = Gr.buscar_grupo(Main.grupos, num, mat)
                        if(gru):
                            print(gru.to_string())
                        else:
                            print(Me.mensa["err"])
                    elif(op == 3):
                        num = input(Me.mensa["num"] + ": ")
                        mat = input(Me.mensa["id"] + " "
                                    + Me.mensa["mat"] + ": ")
                        gru = Gr.buscar_grupo(Main.grupos, num, mat)
                        if(gru):
                            print(
                                "1. " + Me.mensa["num"] + "\n2. " + Me.mensa["mat"] + "\n3. " + Me.mensa["pro"])
                            o = int(input())
                            if(o == 1):
                                num = input(Me.mensa["num"] + ": ")
                                print(gru.set_numero(num, mat, Main.grupos))
                            elif(o == 2):
                                mat = Ma.buscar_materia(Main.materias, input(
                                    Me.mensa["id"] + " " + Me.mensa["mat"] + ": "))
                                print(gru.set_materia(mat))
                            elif(o == 3):
                                pro = Pe.buscar_persona(
                                    Main.profesores, input(Me.mensa["idePro"] + ": "))
                                print(gru.set_profesor(pro))
                        else:
                            print(Me.mensa["err"])
                    elif(op == 4):
                        num = input(Me.mensa["num"] + ": ")
                        mat = input(Me.mensa["id"] + " "
                                    + Me.mensa["mat"] + ": ")
                        gru = Gr.buscar_grupo(Main.grupos, num, mat)
                        print(Gr.eliminar(Main.grupos, num,
                                          mat, Main.matriculas, Main.notas))
                    elif(op == 5):
                        for gru in Main.grupos:
                            print(gru.to_string())
                    elif(op == 6):
                        mat = input(Me.mensa["id"] + " "
                                    + Me.mensa["mat"] + ": ")
                        for gru in Main.grupos:
                            if(gru.get_materia().get_id() == mat):
                                print(gru.to_string())
                    elif(op == 7):
                        for i in Main.materias:
                            print(Gr.mejores_grupos(i))
                    elif(op == 8):
                        break

    @staticmethod
    def menu_estudiante(estu):
        while True:
            op = int(input(Me.mensa["menuEstu"]))
            if op == 1:
                # Notas: buscar
                mat = input(Me.mensa["id"] + " " + Me.mensa["mat"] + ": ")
                gru = input(Me.mensa["numGrp"])
                grupo = Gr.buscar_grupo(Main.grupos, gru, mat)
                for no in Main.notas:
                    if(no.get_grupo() == grupo and no.get_estudiante() == estu):
                        print(no.to_string())
            elif op == 2:
                # Matricula: CASE
                while True:
                    o = int(input(Me.mensa["CASE"]))
                    if(o == 1):
                        sem = input(Me.mensa["sem"] + ": ")
                        mat = input(Me.mensa["id"] + " "
                                    + Me.mensa["mat"] + ": ")
                        gru = input(Me.mensa["numGrp"])
                        grupo = Gr.buscar_grupo(Main.grupos, gru, mat)
                        if(grupo):
                            matri = M(semestre, estu, grupo)
                            print(M.matricular(Main.matriculas, matri))
                        else:
                            print(Me.mensa["err"])
                    elif(o == 2):
                        mat = input(Me.mensa["id"] + " "
                                    + Me.mensa["mat"] + ": ")
                        matr = M.buscar_matricula(
                            Main.matriculas, estu.get_identificacion(), mat)
                        if(matr):
                            print(matr.to_string())
                        else:
                            print(Me.mensa["err"])
                    elif(o == 3):
                        mat = input(Me.mensa["id"] + " "
                                    + Me.mensa["mat"] + ": ")
                        matr = M.buscar_matricula(
                            Main.matriculas, estu.get_identificacion(), mat)
                        if(matr):
                            sem = input(Me.mensa["nuSem"] + ": ")
                            print(matr.set_semestre(sem))
                        else:
                            print(Me.mensa["err"])
                    elif(o == 4):
                        mat = input(Me.mensa["id"] + " "
                                    + Me.mensa["mat"] + ": ")
                        matr = M.buscar_matricula(
                            Main.matriculas, estu.get_identificacion(), mat)
                        print(M.cancelar(Main.matriculas,
                                         estu.get_identificacion(), mat))
                    elif(o == 5):
                        for matr in Main.matriculas:
                            print(matr.to_string())
                    elif(o == 6):
                        break
            elif op == 3:
                # Grupo
                mat = input(Me.mensa["id"] + " " + Me.mensa["mat"] + ": ")
                gru = input(Me.mensa["numGrp"])
                grupo = Gr.buscar_grupo(Main.grupos, gru, mat)
                if(grupo):
                    print(grupo.to_string(1))
                else:
                    print(Me.mensa["err"])
            elif op == 4:
                # Materia
                mat = input(Me.mensa["id"] + " " + Me.mensa["mat"] + ": ")
                materia = Ma.buscar_materia(Main.materias, mat)
                if(materia):
                    print(materia.to_string())
                else:
                    print(Me.mensa["err"])
            elif op == 5:
                while True:
                    print(Me.mensa["modi"])
                    o = int(input(Me.mensa["opUsu"]))
                    if(o == 1):
                        nom = input(Me.mensa["nom"] + ": ")
                        print(estu.set_nombre(nom))
                    elif(o == 2):
                        cla = input(Me.mensa["con"] + ": ")
                        print(estu.set_clave(cla))
                    elif(o == 3):
                        break
            elif op == 6:
                # Salir
                break

    @staticmethod
    def menu_profesor(profesor):
        while True:

            op = int(input(Me.mensa["opcProf"]))
            if op == 1:
                # Nota

                while True:
                    opc = int(input(Me.mensa["opnot"]))
                    if opc == 1:
                        # buscar estudiante
                        es = Es.buscar_persona(
                            Main.estudiantes, input(Me.mensa["ideEstu"]))
                        if es:
                            print(Me.mensa["enc"])
                            # buscar grupo
                            numGrp = input(Me.mensa["numGrp"])
                            ideMate = input(Me.mensa["ideMate"])
                            grp = Gr.buscar_grupo(Main.grupos, numGrp, ideMate)
                            if grp:
                                print(Me.mensa["enc"])
                                por = float(input(Me.mensa["por"] + ": "))
                                val = float(input(
                                    Me.mensa["val"] + ": "))
                                id = input(
                                    Me.mensa["ideNot"])
                                materia = Ma.buscar_materia(
                                    Main.materias, ideMate).get_nombre()
                                n1 = No(por, val, id, es, grp)
                                print(No.registrar(n1, Main.notas))
                                No.enviar_correo_actualizar_nota(
                                    "registro", id, val, por, es, materia)
                                print(Me.mensa["emailSatisfactory"])

                            else:
                                print(Me.mensa["noenc"])

                        else:
                            print(Me.mensa["noenc"])

                    elif opc == 2:
                        id = input(Me.mensa["ideNot"])
                        es = input(Me.mensa["ideEstu"])
                        ideMate = input(Me.mensa["ideMate"])
                        numgrup = input(Me.mensa["numGrp"])

                        n1 = No.buscar_nota(
                            Main.notas, es, ideMate, numgrup, id)

                        if n1:
                            val = float(input(Me.mensa["val"] + ": "))
                            por = float(input(Me.mensa["por"] + ": "))
                            materia = Ma.buscar_materia(
                                Main.materias, ideMate).get_nombre()
                            index = Main.notas.index(n1)
                            Main.notas[index].set_valor(
                                n1.get_valor() if val == "" else val)
                            Main.notas[index].set_porcentaje(n1.get_porcentaje()
                                                             if por == "" else por)
                            print(Me.mensa["mod"])
                            es = Es.buscar_persona(Main.estudiantes, es)
                            No.enviar_correo_actualizar_nota(
                                "modifico", id, val, por, es, materia)
                            print(Me.mensa["emailSatisfactory"])

                        else:
                            print(Me.mensa["noenc"])
                    elif opc == 3:
                        es = input(Me.mensa["ideEstu"])
                        id = input(Me.mensa["ideNot"])
                        idemate = input(Me.mensa["ideMate"])
                        num_grupo = input(Me.mensa["numGrp"])
                        no = No.buscar_nota(
                            Main.notas, es, idemate, num_grupo, id)
                        print(No.eliminar(Main.notas, es,
                                          idemate, num_grupo, id))
                        es = Es.buscar_persona(Main.estudiantes, es)
                        materia = Ma.buscar_materia(
                            Main.materias, idemate).get_nombre()
                        No.enviar_correo_actualizar_nota(
                            "borro", id, no.get_valor(), no.get_porcentaje(), es, materia)
                        print(Me.mensa["emailSatisfactory"])

                    elif opc == 4:
                        n1 = No.buscar_nota(Main.notas, input(Me.mensa["ideEstu"]), input(
                            Me.mensa["ideMate"]), input(Me.mensa["numGrp"]), input(Me.mensa["ideNot"]))
                        if n1:
                            print(n1.to_string())
                        else:
                            print(Me.mensa["noenc"])

                    elif opc == 5:
                        break

            elif op == 2:
                # Grupo
                while True:
                    opc = int(input(Me.mensa["busgrp"]))
                    if opc == 1:
                        grp = Gr.buscar_grupo(Main.grupos, input(
                            Me.mensa["numGrp"]), input(Me.mensa["ideMate"]))

                        if grp:
                            print(grp.to_string())
                        else:
                            print(Me.mensa["noenc"])

                    elif opc == 2:
                        break

            elif op == 3:
                # Materia
                while True:
                    opc = int(input(Me.mensa["menuMatt"]))

                    if opc == 1:
                        matt = Ma.buscar_materia(
                            Main.materias, input(Me.mensa["ideMate"]))

                        if matt:
                            print(matt.to_string())
                        else:
                            print(Me.mensa["noenc"])

                    elif opc == 2:
                        Main.generar_reporte_en_excel()

                    elif opc == 3:
                        break
            elif op == 4:
                # nuevo evento
                asun = input(Me.mensa["nom"] + ": ")
                fech = input(Me.mensa["fech"] + ": ")
                det = input(Me.mensa["det"] + ": ")
                mat = input(Me.mensa["ideMate"])
                gru = input(Me.mensa["numGrp"])
                print(Pr.encontrar_correos_y_enviar(Main.grupos, gru,
                                                    asun, mat, fech, profesor.get_nombre(), det))
            elif op == 5:
                id_materia = input(Me.mensa["ideMate"])
                id_grupo = input(Me.mensa["numGrp"])
                lista_grupos = Main.grupos
                No.mejores_notas(lista_grupos, id_materia, id_grupo)

            elif op == 6:
                # cambiar contraseña
                profesor.set_clave(input(Me.mensa["cambContr"]))
                pass

            elif op == 7:
                # cambiar nombre
                profesor.set_nombre(input(Me.mensa["cambNombre"]))
                pass

            elif op == 8:
                # salir
                break


if __name__ == "__main__":
    print(Me.esp["idi"])
    print(Me.ing["idi"])
    idi = input()
    if(idi == "1"):
        Me.mensa = Me.esp
    else:
        Me.mensa = Me.ing
    Main.run()
