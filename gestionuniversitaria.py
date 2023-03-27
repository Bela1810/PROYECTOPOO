import sys

class GestionApp:
    Estudiantes: list[str] = []


class Estudiante:
    def _init_(self):
        self.nombre = None
        self.apellidos = None
        self.facultad = None
        self.id = None
        self.contraseña = None
        self.conectado = False

    def registrar_estudiante(self):
        print("Bienvenido a la aplicacion de gestion universitaria, porfavor, introduzca sus datos:")
        print("______________________________")
        print("REGISTRARSE: ")
        print("______________________________")

        self.nombre = str(input("Introduzca su nombre:"))

        self.apellidos = str(input("Introduzca sus apellidos:"))

        self.facultad = str(input("Introduzca la facultad a la que pertenece: "))

        self.id = str(input("Introduzca su id:"))

        while True:
            if GestionApp.Estudiantes.__contains__(self.id):
                print("Ya estás registrado")

            else:
                GestionApp.Estudiantes.append(self.id)
                break

        self.contraseña = str(input("Introduzca su nueva contraseña:"))

        print(f"Se registró con exito el usuario, {self}")

        print("______________________________")
        print(f"INICIAR SESIÓN: ")
        print("______________________________")

    def iniciar_sesion(self, cont=4):

        Id = str(input("introduzca su id:"))

        while True:
            if not GestionApp.Usuarios._contains_(Id):
                print("La id no esta registrada, porfavor revisar")
                Id = str(input("introduzca la id del usuario:"))
            else:
                if self.id == Id:
                    contraseña = str(input("introduzca su contraseña:"))
                    while True:

                        if self.contraseña != contraseña:
                            cont -= 1
                            if cont > 0:
                                print(f"Contraseña incorrecta, le quedan {cont} intentos")
                                contraseña = str(input("introduzca su contraseña:"))

                            elif cont == 0:
                                print("Intentos agotados, la aplicacion se va a cerrar.")
                                break
                        else:
                            if self.id == Id and self.contraseña == contraseña:
                                print("Iniciaste sesion con exito!")
                                self.conectado = True
                                break
                break

    def cerrar_sesion(self):
        decision = str(input("Desea cerrar sesion?"))
        if decision == "Si":
            self.conectado = False
            sys.exit()
        else:
            print("La sesión continua")

    def _str_(self):
        return f"Nombre de usuario: {self.nombre}, Apellidos: {self.apellidos}, Facultad: {self.facultad}, id: {self.id}, "


app = GestionApp()
usuario_1 = Estudiante()
usuario_1.registrar_estudiante()
usuario_1.iniciar_sesion()
usuario_1.cerrar_sesion()