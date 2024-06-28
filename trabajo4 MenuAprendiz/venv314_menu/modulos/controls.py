

def control_letras(prompt):   # Control para validar que el usuario solo digite letras en en el input 
    while True:
      entrada = input(prompt) # El while condiciona la entrada con isalpha 
      if (entrada.replace("", "").isalpha()):
        break  # Declaracion para finalizar el bucle while 
      else:     # Si el usuario digita numeros o caractes diferentes a isalpha envia un mensaje 
        print("Solo digite caracteres alfabeticos") # Mensaje por que se digito caracteres diferentes a isalpha 
    return entrada # despues de mostrar el mensaje de la linea anterior retorna al inicio de la entrada 


def control_numeros(prompt): # Control para validar que el usuario solo digite numeros en en el input 
    while True:   # El while condiciona la entrada con isnumeric 
        entrada = input(prompt)
        if (entrada.replace("", "").isnumeric()):  # Si el usuario digita numeros o caractes diferentes a isnumeric envia un mensaje 
          break  # Declaracion para finalizar el bucle while 
        else:    # Mensaje por que se digito caracteres diferentes a caracteres numericos 
             print ("Solo digite caracteres numericos")
    return entrada # despues de mostrar el mensaje de la linea anterior retorna al inicio de la entrada 


def control_numeros_letras(prompt): # Control para validar que el usuario solo digite numeros o letras 
    while True: # El while condiciona la entrada con isalnum
        entrada = input(prompt)
        if (entrada.replace("",  "").isalnum()): 
            break # Declaracion para finalizar el bucle while 
        else:  # Si el usuario digita numeros o caractes diferentes a isalnum envia un mensaje 
            print("Solo digite caracteres alfabéticos y números")
    return entrada # despues de mostrar el mensaje de la linea anterior retorna al inicio de la entrada 