'''def lineaEnsamblado():
    #Ingreso de información por parte del usuario
    modeloAutomovil = input("Ingrese el modelo del automóvil: ")
    numeroLineaEnsamblado = input("Ingrese el numero de linea de ensamblado: ")
    frecuenciaSalida = int(input("Ingrese tiempo de ensamblaje en linea (en minutos): "))
    cantEstaciones = int(input("Ingrese cantidad de estaciones en la linea de ensamble: "))
    
    #Como los turnos son de 8 horas, en minutos son 480 minutos
    
    cantVehiculosturno1 = 0 #Cantidad de vehiculos que se ensamblaron en el primer turno
    cantVehiculosturno2 = 0 #Cantidad de vehiculos que se ensamblaron en el segundo turno
    minutosTranscurridos = 0
    whileminutosTranscurridos <= 960:
        if minutosTranscurridos <= 480:
            #Cantidad de vehiculos en el primer turno
            minutosTranscurridos = minutosTranscurridos + frecuenciaSalida    
            cantVehiculosturno1 = cantVehiculosturno1 + 1
            
        else:
            #Cantidad de vehiculos en el segundo turno
            minutosTranscurridos = minutosTranscurridos + frecuenciaSalida
            cantVehiculosturno2 = cantVehiculosturno2 + 1
            
    cantTotal = cantVehiculosturno1 + cantVehiculosturno2
    
    print("Cantidad de vehiculos del modelo ", modeloAutomovil, " ensamblados en la linea ",numeroLineaEnsamblado, " durante el primer turno: ", cantVehiculosturno1)     
    print("Cantidad de vehiculos del modelo ", modeloAutomovil, " ensamblados en la linea: ", numeroLineaEnsamblado, " durante el segundo turno: ", cantVehiculosturno2)
    print("En un dia se ensamblan ", cantTotal ," del modelo ", modeloAutomovil, " en la linea ", numeroLineaEnsamblado)
    horasTranscurridas = frecuenciaSalida/60 #Pasaje minutos a horas
    
    tiempoEnsambladoTotal = horasTranscurridas * cantEstaciones #Tiempo de ensamblado total
    print ("Se tardan ", float(round(tiempoEnsambladoTotal,2)), " horas en ensamblar un vehiculo completo.")
    input("Presiona alguna tecla para terminar.")
lineaEnsamblado()'''

def lineaEnsamblado():
    #Ingreso de información por parte del usuario
    modeloAutomovil = input("Ingrese el modelo del automóvil: ")
    numeroLineaEnsamblado = input("Ingrese el numero de linea de ensamblado: ")
    frecuenciaSalida = int(input("Ingrese tiempo de ensamblaje en linea (en minutos): "))
    cantEstaciones = int(input("Ingrese cantidad de estaciones en la linea de ensamble: "))    
    
    #Tiempo total de ensamblado completo de un vehiculo
    frecuenciaHoras = frecuenciaSalida/60
    tiempoTotal = frecuenciaHoras * cantEstaciones
    print ("Se tardan ", float(round(tiempoTotal,2)), " horas en ensamblar un vehiculo completo.")
    
    #Vehiculos ensamblados en la linea segun el turno
    #Turno es 480 minutos
    cantVehiculosturno1 = frecuenciaSalida/480
    cantVehiculosturno2 = frecuenciaSalida/480
    
    
lineaEnsamblado()
  
    

    