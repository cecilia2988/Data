# """
# function crearClaseEmprendedor() {
#   class Emprendedor {
#       constructor(nombre, apellido, libros, mascotas) {
#           // El constructor de la clase Emprendedor recibe nombre (string), apellido (string), libros (array de objetos), mascotas (array de strings)
#           // Inicializar las propiedades del emprendedor con los valores recibidos como argumento

#           // Tu código aca:
#       }

#       addMascota(mascota) {
#         // este método debe agregar una mascota (mascota) al arreglo de mascotas del emprendedor.
#         // no debe retornar nada.

#         // Tu código aca:
        

def CrearEmprendedor():
    class Emprendedor:
        nombre=str
        apellido=str
        libros= list[Book]
        mascotas= list[str]

        def __init__(self,nombre,apellido,libros,mascotas) -> None:
            self.nombre=nombre
            self.apellido=apellido
            self.libros=libros
            self.mascotas=mascotas
                    
        def addMascota(self,mascota):
            self.mascotas.append(mascota)
                    

        def getMascotas(self):
            largo=len(self.mascotas)
            return largo
                            

        def addBook(self,book, autor):
            b= Book(book,autor)
            self.libros.append(b)

        
        def  getBooks(self):
            array=[]
            for l in self.libros:
                array.append(l.titulo)
            return array

        
        def getFullName(self):
            nombreyapellido=''
            nombreyapellido=self.nombre + " " + self.apellido
            return nombreyapellido
    return Emprendedor



class Book:
        def __init__(self,titulo,autor) -> None:
            self.titulo=titulo
            self.autor=autor
    


def run():
    Emp=CrearEmprendedor()
    milibro=Book("titulo1","autor1")
    mascota=["Betty","Rosy","Miro"]
    miemprendedor=Emp("Pepe","Pepin",[milibro],mascota)
    miemprendedor.addBook("libro2","autor2")
    miemprendedor.addBook("libro3","autor3")
    miemprendedor.addMascota("Morena")
    print(miemprendedor.getBooks())
    print(miemprendedor.getMascotas())



if __name__=='__main__':
    run()
