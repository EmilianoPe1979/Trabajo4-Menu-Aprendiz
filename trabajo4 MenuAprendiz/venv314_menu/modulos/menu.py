# from os import system as osystem
# from msvcrt import getch
# from colorama import Fore,Back # Importo colorama para color fondo y fuente
# print(Fore.BLACK + Back.RED)# Defino colores fondo y fuente 


# while True:
#   print("-----------------------")
#   print("Datos Aprendices:")
#   print("1. Ingreses los datos del aprendiz")
#   print("2. Mostrar estudiantes")
#   print("3. lista por fichas")
#   print("4. lista por evaluacion")
#   print("5. Eliminar registro de aprendiz")
#   print("6. Modidicar registro de aprendiz")
#   print("7. Salir")
#   print("-----------------------")
  while True:
      try:
          opcion = float(input("Escoge una opción: "))
          break  # Salimos del bucle si se ingresa un número válido
      except ValueError:
          print("Opción inválida. Inténtalo nuevamente.")
    opcion = int(input("Escoge una opcion: ")) # El usuario escoge una opcion 

#   if opcion == 1:
#     create_student()
#   elif opcion== 2:
#     getprintresults()
#   elif opcion== 3:
#     print("Señor usuario de la siguiente lista seleccione una ficha: ")
#     print(get_card())
#     curso = input("Digite el nombre de la ficha: ")
#     getStudentByCorse(curso)
#   elif opcion== 4:
#     print("Señor usuario de la siguiente lista seleccione una opcion: ")
#     print(get_resultado())
#     print("Señor usuario escoja entre las siguientes opciones A/APROBO - D/DESAPROBO: ")
#     codigo = input("Digite la opcion de evaluacion: ")
#     getStudentsByEvaluation(codigo)
#   elif opcion== 5:
#     print("Digite el numero de documento que desea eliminar: ")
#     getprintresults()
#     document = input("Ingrese el documento: ")
#     deleteStudentsbyDocument(document)
#     getprintresults()
#   elif opcion== 6:
#     print("Digite el numero de documento del registro que desea moficar: ")
#     getprintresults()
#     document = input("Ingrese el documento: ")
#     updateStudentByDocument(document)
#     getprintresults()
#   elif opcion== 7:
#     print("Adios")
#     break
#   else:
#     print("Opcion no valida")
