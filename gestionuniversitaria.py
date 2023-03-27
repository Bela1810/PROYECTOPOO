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