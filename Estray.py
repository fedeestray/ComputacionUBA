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

def optimizarEnsamblado():
    #Ingresos por parte del usuario
    modeloAutomovil = input("Ingrese el modelo del vehiculo: ")
    lineaEnsamblado = input("Ingrese numero de linea de ensamblado: ")
    frecuenciaSalida = int(input("Ingrese frecuencia de salida de linea de ensamblado (en minutos): "))
    cantidadEstaciones = int(input("Ingrese cantidad de estaciones en la linea de ensamblado: "))

    #Calculo de vehiculos por turno

    cantVehiculosTurno = 480//(frecuenciaSalida*cantidadEstaciones)
    cantVehiculosDia = (cantVehiculosTurno*2)

    #Frecuencia de salida de la linea de ensamblado en horas
    tiempoHoras = float(frecuenciaSalida/60)

    #Calculo vehiculo completo en horas
    vehiculoTerminado = tiempoHoras*cantidadEstaciones
    print("La cantidad de vehiculos del modelo", modeloAutomovil, "que salen de la linea de ensamblado", lineaEnsamblado, "son",round(cantVehiculosTurno), "por turno y se ensamblan", cantVehiculosDia, "en un dia")
    print("Se ensambla un vehiculo completo del modelo", modeloAutomovil, "en la linea", lineaEnsamblado, "en", vehiculoTerminado, "horas")

    input("Presione enter para cerrar")


optimizarEnsamblado()
