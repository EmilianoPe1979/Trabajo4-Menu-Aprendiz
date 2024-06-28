from colorama import Fore,Back # Importo colorama para color fondo y fuente
print(Fore.BLACK + Back.RED)# Defino colores fondo y fuente 
from os import system as osystem # importo system para limpiar pantalla
from msvcrt import getch

studen_lists = []
student = ()



def create_student():
  nombre = input("Ingrese el nombre del aprendiz: ")
  documento = input("Ingrese el numero de documento: ")
  print("Señor usuario de la siguiente lista seleccione una opcion: ")
  print(get_card())
  curso = input("Digite el nombre de la ficha: ")
  print("Señor usuario de la siguiente lista seleccione una opcion: ")
  print(get_resultado())
  print("Señor usuario escoja entre las siguientes opciones A/APROBO - D/DESAPROBO: ")
  codigo = input("Digite la opcion de evaluacion: ")
  

  student = {
    "Nombre": nombre,
    "Documento": documento,
    "Curso": curso, 
    "Evaluacion": codigo
  }
  
  studen_lists.append(student)
 
  
def getStudentByCorse(code):

  for student in studen_lists:
    if student['Curso'] == code:
      for key, value in student.items():
        print(key,value) 
    print("****************************")    


def getStudentsByEvaluation(nota):

  for name in studen_lists:
    if name['Evaluacion'] == nota:
     for key, value in name.items():
        print(key,value) 
    print("******************************")  
def deleteStudentsbyDocument(document):

  for student in studen_lists:
    if student['Documento'] == document:
      studen_lists.remove(student)
  print("Se hab borrado el aprendiz con documeto : ",document) 

def updateStudentByDocument(dato_modificar):
  # dato_modificar=(input("Introduce el numero de documeto del aprendiz que va actualizar:"))
  for student in studen_lists:
    if student["Documento"] == dato_modificar:
      student["Nombre"]=input("Ingrese el nuevo nombre:")
      student["Curso"]=input("Ingrese el nombre del curso:")
      student["Evaluacion"]=input("Introduce la nueva evaluacion:")
      print("Contacto modificado")
      return

card = [
    { 
      "nombre":"ADSO",
      "codigo":"2877795"
    }, 
    {
      "nombre":"CONTABILIDAD",
      "codigo":"2866699"  
    },
    {
      "nombre":"COCINA",
      "codigo":"2855588"  
    }
  ]


resultado = [
    {
      "nombre":"APROBO",
      "codigo":"A"  
    },

    {
      "nombre":"DESAPROBO",
      "codigo":"D"  
    }
  
  ]

def get_card():
  for car in card:
      print(car['nombre'])

def get_resultado():
  for resul in resultado:
      print(resul['codigo'])

def getprintresults():
  for x in studen_lists:
      print("******************************")
      index = studen_lists.index(x)
      print("Los datos del estudiante ",index,":" )
      for clave,valor in x.items():
        print(clave,valor)


while True:
  print("-----------------------")
  print("Datos Aprendices:")
  print("1. Ingreses los datos del aprendiz")
  print("2. Mostrar estudiantes")
  print("3. lista por fichas")
  print("4. lista por evaluacion")
  print("5. Eliminar registro de aprendiz")
  print("6. Modidicar registro de aprendiz")
  print("7. Salir")
  print("-----------------------")
  opcion = int(input("Escoge una opcion: "))

  if opcion == 1:
    create_student()
  elif opcion== 2:
    getprintresults()
  elif opcion== 3:
    print("Señor usuario de la siguiente lista seleccione una ficha: ")
    print(get_card())
    curso = input("Digite el nombre de la ficha: ")
    getStudentByCorse(curso)
  elif opcion== 4:
    print("Señor usuario de la siguiente lista seleccione una opcion: ")
    print(get_resultado())
    print("Señor usuario escoja entre las siguientes opciones A/APROBO - D/DESAPROBO: ")
    codigo = input("Digite la opcion de evaluacion: ")
    getStudentsByEvaluation(codigo)
  elif opcion== 5:
    print("Digite el numero de documento que desea eliminar: ")
    getprintresults()
    document = input("Ingrese el documento: ")
    deleteStudentsbyDocument(document)
    getprintresults()
  elif opcion== 6:
    print("Digite el numero de documento del registro que desea moficar: ")
    getprintresults()
    document = input("Ingrese el documento: ")
    updateStudentByDocument(document)
    getprintresults()
  elif opcion== 7:
    print("Adios")
    break
  else:
    print("Opcion no valida")


  
  
