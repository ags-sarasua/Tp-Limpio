
from Clases import *



def menu_clase(matriz_persona,matriz_empleado,matriz_avion,matriz_vuelo,matriz_viaje,matriz_reserva):
    print('1)Persona    2)Empleado    3)Avion    4)Vuelo  5)Viaje    6)Reserva    B)Volver')
    eleccion_clase=input('Ingrese su eleccion: ')
    if eleccion_clase==1:
        print('1)Visualizar matriz   2)Agregar persona  B)Volver')
        eleccion_metodo=input('Ingrese su eleccion: ')
        if eleccion_metodo==1:
            print(matriz_persona)
        if eleccion_metodo==2:
            print('1)DNI   2)Nombre   3)Sexo  4)Fecha de nacimiento   5)Pais')
            inputs=[]
            for i in range(5):
                user_input = str(input("Inroduzca {} :".format(i+1)))
                inputs.append(user_input)
                #Todos los checks
                matriz_persona.append(persona(inputs[0], inputs[1], inputs[2],inputs[3],inputs[4]))
            
        if eleccion_metodo=='B':
            menu_clase()
    
    if eleccion_clase==2:
        print('1)Visualizar matriz   2)Agregar empleado   3)Eliminar empleado   B)Volver')
        eleccion_metodo=input('Ingrese su eleccion: ')
        if eleccion_metodo==1:
            print(matriz_empleado)
        if eleccion_metodo==2:
            print('1)DNI   2)Nombre   3)Sexo  4)Fecha de nacimiento   5)Pais    6)Legajo    7)Sector')
            inputs=[]
            for i in range(7):
                user_input = str(input("Inroduzca {} :".format(i+1)))
                inputs.append(user_input)
                #Todos los checks
                matriz_empleado.append(empleado(inputs[0], inputs[1], inputs[2],inputs[3],inputs[4],inputs[5],inputs[6],inputs[7]))
        if eleccion_metodo==3:
            #Metodo marti
            pass
        if eleccion_metodo=='B':
            menu_clase()

    if eleccion_clase==3:
        print('1)Visualizar matriz   2)Agregar avion   3)Eliminar avion   B)Volver')
        eleccion_metodo=input('Ingrese su eleccion: ')
        if eleccion_metodo==1:
            print(matriz_avion)
        if eleccion_metodo==2:
            print('1)Nro serie   2)Modelo   3)Fecha alta  4)Vuelos actuales   5)Estado')
            inputs=[]
            for i in range(5):
                user_input = str(input("Inroduzca {} :".format(i+1)))
                inputs.append(user_input)
                #Todos los checks
                inputs[0]=avion.check_nro_serir(inputs[0]) #ESCRIBIRLO BIENNNN
                inputs[3]=avion.check_nro_vuelos_actuales(inputs[2])
                inputs[4]=avion.check_fecha_alta(inputs[4])  #LLAMAERLO CHECK_ESTADO
                #Append
                matriz_avion.append(avion(inputs[0], inputs[1], inputs[2],inputs[3],inputs[4]))
        if eleccion_metodo==3:
            #Metodo marti
            pass
        if eleccion_metodo=='B':
            menu_clase()
            
            
    if eleccion_clase==4:
        print('1)Visualizar matriz   2)Agregar vuelo  B)Volver')
        eleccion_metodo=input('Ingrese su eleccion: ')
        if eleccion_metodo==1:
            print(matriz_vuelo)
        if eleccion_metodo==2:
            print('1)Nro vuelo   2)Hora   3)Aeropuerto salida  4)Aeropuerto llegada   5)Nro de serie avion   6)Piolo   7)Precio') #Ojo con lo del :avion
            inputs=[]
            for i in range(7):
                user_input = str(input("Inroduzca {} :".format(i+1)))
                inputs.append(user_input)
                #Todos los checks
                matriz_vuelo.append(vuelo(inputs[0], inputs[1], inputs[2],inputs[3],inputs[4],inputs[5],inputs[6]))
        if eleccion_metodo=='B':
            menu_clase()
            
    if eleccion_clase==5:
        print('1)Visualizar matriz   2)Agregar reserva     3)Eleminar reserva  B)Volver')
        eleccion_metodo=input('Ingrese su eleccion: ')
        if eleccion_metodo==1:
            print(matriz_reserva)
        if eleccion_metodo==2:
            print('1)Nro viaje   2)Nro vuelo   3)Nro serie  4)Fecha')
            inputs=[]
            for i in range(4):
                user_input = str(input("Inroduzca {} :".format(i+1)))
                inputs.append(user_input)
                #Todos los checks
                matriz_reserva.append(reserva(inputs[0], inputs[1], inputs[2],inputs[3]))
        if eleccion_metodo==3:
            #Metodo marti
            pass
        if eleccion_metodo=='B':
            menu_clase()
            
            
    if eleccion_clase==6:
        print('1)Visualizar matriz   2)Agregar vuelo  B)Volver')
        eleccion_metodo=input('Ingrese su eleccion: ')
        if eleccion_metodo==1:
            print(matriz_reserva)
        if eleccion_metodo==2:
            print('1)Nro reserva   2)DNI cliente   3)L_Empleado  4)Nro viaje   5)Monto') #Ojo con lo del :avion
            inputs=[]
            for i in range(7):
                user_input = str(input("Inroduzca {} :".format(i+1)))
                inputs.append(user_input)
                #Todos los checks
                inputs[0]=reserva.check_nro_factura(inputs[0])
                inputs[1]=reserva.check_cliente(inputs[1],matriz_persona)
                inputs[2]=reserva.check_empleado(inputs[2],matriz_empleado)
                inputs[3]=reserva.check_viaje(inputs[3],matriz_viaje)
                inputs[4]=reserva.check_monto(inputs[4],...,matriz_viaje,matriz_vuelo) #ACA NO VA EL VIAJE CORREGIRLO
                #Append
                matriz_reserva.append(reserva(inputs[0], inputs[1], inputs[2],inputs[3],inputs[4],inputs[5],inputs[6]))
        if eleccion_metodo==3:
            #Metodo marti
            pass
        if eleccion_metodo=='B':
            menu_clase()
    
def menu():
    matriz_login=[]
    matriz_persona=[]
    matriz_empleado=[]
    matriz_avion=[]
    matriz_vuelo=[]
    matriz_viaje=[]
    matriz_reserva=[]
    print('     Ingreso    ')
    usuario=input('Usuario: ')
    contra=input('Contrasenia:  ')  
    #Faltan metodos de login

    #Una vez que entre
    menu_clase(matriz_persona,matriz_empleado,matriz_avion,matriz_vuelo,matriz_viaje,matriz_reserva)
    
        