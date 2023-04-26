
import datetime
from listasenlazadas import *
from Clases import *

#----------------

def menu_clase(lista_persona,lista_empleado,lista_avion,lista_vuelo,lista_viaje,lista_reserva):
    print('1)Persona    2)Empleado    3)Avion    4)Vuelo    5)Viaje      6)Reserva    B)Volver')
    eleccion_clase=input('Ingrese su eleccion: ')
    
    if eleccion_clase=='1':
        while True:  #Para que una vez hagas algun metodo puedas volver a este lugar
            print('1)Visualizar matriz   2)Agregar persona   B)Volver')
            
            eleccion_metodo=input('Ingrese su eleccion: ')
            if eleccion_metodo=='1':
                print(lista_persona)
            if eleccion_metodo=='2':
                print('1)DNI   2)Nombre   3)Sexo  4)Fecha de nacimiento   5)Pais')
                inputs=[]
                for i in range(5):
                    user_input = str(input("Inroduzca {} :".format(i+1)))
                    inputs.append(user_input)
                input[0]=persona.check_DNI(input[0])
                input[1]=persona.check_nombre(input[1])
                input[2]=persona.check_sexo(input[2])
                input[3]=persona.check_fecha_de_nacimiento(input[3])
                input[4]=persona.check_pais(input[4])
                lista_persona.append(persona(inputs[0], inputs[1], inputs[2],inputs[3],inputs[4]))
                
            if eleccion_metodo=='B':
                menu_clase()
    
    if eleccion_clase=='2':
        while True:
            print('1)Visualizar matriz   2)Agregar empleado   3)Eliminar empleado   B)Volver')
            eleccion_metodo=input('Ingrese su eleccion: ')
            if eleccion_metodo=='1':
                print(lista_empleado)
            if eleccion_metodo=='2':
                print('1)DNI   2)Nombre   3)Sexo  4)Fecha de nacimiento   5)Pais    6)Legajo    7)Sector')
                inputs=[]
                for i in range(7):
                    user_input = str(input("Inroduzca {} :".format(i+1)))
                    inputs.append(user_input)
                    #Todos los checks
                input[0]=persona.check_DNI(input[0])
                input[1]=persona.check_nombre(input[1])
                input[2]=persona.check_sexo(input[2])
                input[3]=persona.check_fecha_de_nacimiento(input[3])
                input[4]=persona.check_pais(input[4])
                input[5]=empleado.checklegajo(input[5])
                input[6]=empleado.checksector(input[6])
                lista_empleado.append(empleado(inputs[0], inputs[1], inputs[2],inputs[3],inputs[4],inputs[5],inputs[6],inputs[7]))
            if eleccion_metodo=='3':
                first_attribute=input('Ingrese el DNI del empleado que desea eliminar: ')
                posicion=lista_empleado.buscar(first_attribute)
                if posicion:
                    lista_empleado.pop(posicion)
                    print('El empleado con el DNI {} se ha eliminado correctamente').format(first_attribute)
                print('El empleado ingresado no se encuentra en la base de datos')
            
            if eleccion_metodo=='B':
                menu_clase()

    if eleccion_clase=='3':
        while True:
            print('1)Visualizar matriz   2)Agregar avion   3)Eliminar avion   B)Volver')
            eleccion_metodo=input('Ingrese su eleccion: ')
            if eleccion_metodo=='1':
                print(lista_avion)
            if eleccion_metodo=='2':
                print('1)Nro serie   2)Modelo   3)Fecha alta  4)Vuelos actuales   5)Estado')
                inputs=[]
                for i in range(5):
                    user_input = str(input("Inroduzca {} :".format(i+1)))
                    inputs.append(user_input)
                #Todos los checks
                inputs[0]=avion.check_nro_serie(inputs[0])
                inputs[4]=avion.check_estado(inputs[4])
                inputs[2]=validarFecha(inputs[2])  #Mirar esto
                lista_avion.append(avion(inputs[0], inputs[1], inputs[2],inputs[3],inputs[4]))
            
            if eleccion_metodo=='3':
                first_attribute=input('Ingrese el Nro serie del avion que desea eliminar: ')
                posicion=lista_empleado.buscar(first_attribute)
                if posicion:
                    lista_empleado.pop(posicion)
                    print('El avion con el nro de serie {} se ha eliminado correctamente').format(first_attribute)
                print('El numero de serie ingresado no se encuentra en la base de datos')
            if eleccion_metodo=='B':
                menu_clase()
            
    if eleccion_clase=='4':
        while True:
            print('1)Visualizar matriz   2)Agregar vuelo  B)Volver')
            eleccion_metodo=input('Ingrese su eleccion: ')
            if eleccion_metodo=='1':
                print(lista_vuelo)
            if eleccion_metodo=='2':
                print('1)Nro vuelo   2)Hora   3)Aeropuerto salida  4)Aeropuerto llegada   5)Nro de serie avion   6)Piloto   7)Precio') #Ojo con lo del :avion
                inputs=[]
                for i in range(7):
                    user_input = str(input("Inroduzca {} :".format(i+1)))
                    inputs.append(user_input)
                    
                #Todos los checks
                inputs[0]=vuelo.check_nro_vuelo(inputs[0])
                inputs[6]=vuelo.check_precio_vuelo(inputs[6])
                inputs[5]=vuelo.check_piloto(inputs[5])
                inputs[4]=vuelo.check_nro_serie(inputs[4]) #Esto es nuevo
                lista_vuelo.append(vuelo(inputs[0], inputs[1], inputs[2],inputs[3],inputs[4],inputs[5],inputs[6]))
            if eleccion_metodo=='B':
                menu_clase()
            
    if eleccion_clase=='5':
        while True:
            print('1)Visualizar matriz   2)Agregar viaje     3)Eleminar viaje  B)Volver')
            eleccion_metodo=input('Ingrese su eleccion: ')
            if eleccion_metodo=='1':
                print(lista_viaje)
            if eleccion_metodo=='2':
                print('1)Nro viaje   2)Nro vuelo   3)Fecha')
                inputs=[]
                for i in range(4):
                    user_input = str(input("Inroduzca {} :".format(i+1)))
                    inputs.append(user_input)
                    #Todos los checks
                input[0]=viaje.check_nro_viaje(input[0])   #HACERLA
                input[1]=viaje.check_vuelo(input[1])
                input[3]=validarFecha(input[3])
                lista_reserva.append(reserva(inputs[0], inputs[1], inputs[2],inputs[3]))
            if eleccion_metodo=='3':
                first_attribute=input('Ingrese el nro de viaje que desea eliminar: ')
                posicion=lista_empleado.buscar(first_attribute)
                if posicion:
                    lista_empleado.pop(posicion)
                    print('El viaje con el nro {} se ha eliminado correctamente').format(first_attribute)
                print('El viaje ingresado no se encuentra en la base de datos')
                pass
            if eleccion_metodo=='B':
                menu_clase()
            
    if eleccion_clase=='6':
        while True:
            print('1)Visualizar matriz   2)Agregar reserva   3)Eliminar reserva     B)Volver')
            eleccion_metodo=input('Ingrese su eleccion: ')
            if eleccion_metodo=='1':
                print(lista_reserva)
            if eleccion_metodo==2:
                print('1)Nro reserva   2)DNI cliente   3)L_Empleado  4)Nro viaje   5)Monto') #Ojo con lo del :avion
                inputs=[]
                for i in range(7):
                    user_input = str(input("Inroduzca {} :".format(i+1)))
                    inputs.append(user_input)
                    #Todos los checks
                inputs[0]=reserva.check_nro_reserva(inputs[0])
                inputs[1]=reserva.check_cliente(inputs[1],lista_persona)
                inputs[2]=reserva.check_empleado(inputs[2],lista_empleado)
                inputs[3]=reserva.check_viaje(inputs[3],lista_viaje)
                inputs[4]=reserva.check_monto(inputs[4],...,lista_viaje,lista_vuelo) #ACA NO VA EL VIAJE CORREGIRLO
                
                if viaje.agregarpasajero(inputs[3]):
                    lista_reserva.append(reserva(inputs[0], inputs[1], inputs[2],inputs[3],inputs[4],inputs[5],inputs[6]))
                else:
                    print('Lamentablemente el vuelo esta lleno')
            if eleccion_metodo=='3':
                first_attribute=input('Ingrese el nro de la reserva que desea eliminar: ')
                posicion=lista_empleado.buscar(first_attribute)
                if posicion:
                    lista_empleado.pop(posicion)
                    print('La reserva con el numero {} se ha eliminado correctamente').format(first_attribute)
                print('La reserva ingresada no se encuentra en la base de datos')
            if eleccion_metodo=='B':
                menu_clase()

def menu():
    lista_persona=Lista()
    lista_empleado=Lista()
    lista_avion=Lista()
    lista_vuelo=Lista()
    lista_viaje=Lista()
    lista_reserva=Lista()
    while True:
        numero = input("Bienvenido a Aerolineas Mamba. Si se quiere registrar ingrese el número 1 si ya tiene una cuenta ingrese el número 2: ")
        while numero != "1" and numero != "2": numero = input("Ingrese una opción válida: ")
        if numero == "1":  
            us, con = input("Ingrese un usuario y una contraseña: ").split()
            if registrarse(us, con): print("Su usuario se creó con éxito")
        if numero == "2":
            us, con = input("Ingrese su usuario y contraseña: ").split()
            if login(us, con):
                menu_clase(lista_persona,lista_empleado,lista_avion,lista_vuelo,lista_viaje,lista_reserva)

menu()