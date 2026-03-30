
class Libro :

    def __init__(self, titulo, autor, genero):
    
 
        self.titulo = titulo
        self.autor = autor
        self.genero = genero  

    def mostrar_info(self):
     print("Titulo:", self.titulo)
     print("Autor:", self.autor)
     print("Genero:", self.genero)
     print("------------------------")


biblioteca = []

# Menu
def mostrar_menu():
    print("\n---Menu---")
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Actualizar libro")
    print("4. Editar libro")
    print("5. Eliminar libro")
    print("6. Salir")

# Agregar libros

def agregar_libro():
    titulo = input("Ingrese el titulo: ")
    autor = input("Ingrese el autor:")
    genero = input("Ingrese el genero:")

    libro = Libro(titulo, autor, genero)
    biblioteca.append(libro)

    print("Libro agregado correctamente")

# mostrar libros

def mostrar_libros():
    if len(biblioteca) == 0:
        print("No hay libros registrados")
    else:

        for libro in biblioteca:
            libro.mostrar_info()

# Buscar libro

def Actualizar_libro():
    titulo_buscar = input("Ingrese el titulo a buscar:")

    for libro in biblioteca:
        if libro.titulo.lower() == titulo_buscar.lower():
            print("Libro encontrado:")
            libro.mostrar_info()
            return
    print("Libro no encontrado")

    # Editar

def editar_libro():
    titulo_buscar = input("Ingrese el titulo del libro a editar: ")

    for libro in biblioteca:
        if libro.titulo.lower() == titulo_buscar.lower():
            print("Libro encontrado, ingrese nuevos datos:")
            libro.titulo = input("Nuevo titulo: ")
            libro.autor = input("Nuevo autor: ")
            libro.genero = input("Nuevo genero: ")
            print("Libro actualizado correctamente")
            return

    print("Libro no encontrado")

    #Eliminar

def eliminar_libro():
    titulo_buscar = input("Ingrese el titulo del libro a eliminar: ")

    for libro in biblioteca:
        if libro.titulo.lower() == titulo_buscar.lower():
            biblioteca.remove(libro)
            print("Libro eliminado correctamente")
            return

    print("Libro no encontrado")

opcion = 0
while opcion != 6:
    mostrar_menu()
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        agregar_libro()
    elif opcion == 2:
        mostrar_libros()
    elif opcion == 3:
        Actualizar_libro()
    elif opcion == 4:
        editar_libro()
    elif opcion == 5:
        eliminar_libro()
    elif opcion == 6:
        print("Saliendo del sistema...")
    else:
        print("Opcion invalida")