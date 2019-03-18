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
    print("La cantidad de vehiculos del modelo", modeloAutomovil, "que salen de la linea de ensamblado", lineaEnsamblado, "son", cantVehiculosTurno, "por turno y se ensamblan", cantVehiculosDia, "en un dia")
    print("Se ensambla un vehiculo completo del modelo", modeloAutomovil, "en la linea", lineaEnsamblado, "en", vehiculoTerminado, "horas")

    input("Presione enter para cerrar")


optimizarEnsamblado()

