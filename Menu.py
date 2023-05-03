from listasenlazadas import *
from Clases import *
from ListaObjetos import *
import matplotlib.pyplot as mlp
#----------------

def menu_clase(lista_persona,lista_empleado,lista_avion,lista_vuelo,lista_viaje,lista_reserva):
    while True:
        print('1)Persona    2)Empleado    3)Avion    4)Vuelo    5)Viaje      6)Reserva    S)Salir')
        
        eleccion_clase=input('Ingrese su eleccion: ')
        
        if eleccion_clase=='1':
            while True:  #Para que una vez hagas algun metodo puedas volver a este lugar
                print('1)Visualizar lista   2)Agregar persona   B)Volver')
                
                eleccion_metodo=input('Ingrese su eleccion: ')
                if eleccion_metodo=='1':
                    print(lista_persona)
                if eleccion_metodo=='2':
                    print('1)DNI   2)Nombre   3)Sexo  4)Fecha de nacimiento   5)Pais')
                    listaComodin=[]
                    listaMenu = ['DNI', 'Nombre', 'Sexo', 'Fecha de nacimiento', 'Pais']
                    for i in range(5):
                        if i == 3:
                            print("Ahora a la fecha de nacimiento.")
                            listaComodin.append(validarFecha())    
                        else:
                            user_input = str(input("Inroduzca {} : ".format(listaMenu[i])))
                            listaComodin.append(user_input)
                    listaComodin[0]=persona.check_DNI(listaComodin[0])
                    listaComodin[1]=persona.check_nombre(listaComodin[1])
                    listaComodin[2]=persona.check_sexo(listaComodin[2])
                    listaComodin[3]=persona.check_fecha(listaComodin[3])
                    listaComodin[4]=persona.check_pais(listaComodin[4])
                    lista_persona.append(Nodo(persona(listaComodin[0], listaComodin[1], listaComodin[2],listaComodin[3],listaComodin[4])))
                    
                if eleccion_metodo=='B':
                    menu_clase(lista_persona,lista_empleado,lista_avion,lista_vuelo,lista_viaje,lista_reserva)
        
        if eleccion_clase=='2':
            while True:
                print('1)Visualizar lista   2)Agregar empleado   3)Eliminar empleado    4)Graficar   B)Volver')
                eleccion_metodo=input('Ingrese su eleccion: ')
                if eleccion_metodo=='1':
                    print(lista_empleado)
                if eleccion_metodo=='2':
                    print('1)DNI   2)Nombre   3)Sexo  4)Fecha de nacimiento   5)Pais    6)Legajo    7)Sector')
                    listaComodin=[]
                    listaMenu = ['DNI', 'Nombre', 'Sexo', 'Fecha de nacimiento', 'Pais','Legajo','Sector']
                    for i in range(7):
                        if i == 3:
                            print("Ahora a la fecha de nacimiento.")
                            listaComodin.append(validarFecha())    
                        else:
                            user_input = str(input("Inroduzca {} : ".format(listaMenu[i])))
                            listaComodin.append(user_input)
                    listaComodin[0]=persona.check_DNI(listaComodin[0])
                    listaComodin[0]=persona.DNI_repetido(listaComodin[0],lista_persona)
                    listaComodin[1]=persona.check_nombre(listaComodin[1])
                    listaComodin[2]=persona.check_sexo(listaComodin[2])
                    listaComodin[3]=persona.check_fecha(listaComodin[3])
                    listaComodin[4]=persona.check_pais(listaComodin[4])
                    listaComodin[5]=empleado.checklegajo(listaComodin[5], lista_empleado)
                    listaComodin[6]=empleado.checksector(listaComodin[6])
                    lista_empleado.append(Nodo(empleado(listaComodin[0], listaComodin[1], listaComodin[2],listaComodin[3],listaComodin[4],listaComodin[5],listaComodin[6])))

                if eleccion_metodo=='3':
                    input_principal=input('Ingrese el DNI del empleado que desea eliminar: ')
                    if lista_viaje.pop(input_principal,"DNI"): print('El empleado con el DNI {} se ha eliminado correctamente'.format(input_principal))
                    else: print('El empleado ingresado no se encuentra en la base de datos')

                if eleccion_metodo=='4':
                    print('1)Cupo de genero   2)Distribuicion de roles')
                    eleccion_grafico=input('Ingrese su eleccion: ')
                    if eleccion_grafico=='1':
                        hombre=0
                        mujer=0
                        otro=0
                        for instancia in lista_empleado:
                            if instancia.sexo=='Masculino':hombre+=1
                            elif instancia.sexo=='Femenino': mujer+=1
                            elif instancia.sexo=='Otro':otro+=1
                        lista_cantidad=[hombre,mujer,otro]
                        lista_sexos=['Masculino','Femenino','Otro']
                        lista_colores=['#00CC99','#DA70D6','Grey']
                        mlp.bar(lista_sexos,lista_cantidad,color=lista_colores)
                        mlp.title("Cupo de genero")
                        mlp.xlabel("Generos")
                        mlp.ylabel("Cantidad")
                        mlp.show()

                    if eleccion_grafico=='2':
                        piloto=0
                        tecnico=0
                        administrativo=0
                        for instancia in lista_empleado:
                            if instancia.sector=='Administrativo':administrativo+=1
                            elif instancia.sector=='Tecnico': tecnico+=1
                            elif instancia.sector=='Piloto':piloto+=1
                        lista_cantidad=[administrativo,tecnico,piloto]
                        lista_roles=['Administrativo','Tecnico','Piloto']
                        mlp.bar(lista_roles,lista_cantidad, color="#FF69B4",width=0.5)
                        mlp.title("Distribuccion de roles")
                        mlp.xlabel("Roles")
                        mlp.ylabel("Cantidad")
                        mlp.show()
                                            
                if eleccion_metodo=='B':
                    menu_clase(lista_persona,lista_empleado,lista_avion,lista_vuelo,lista_viaje,lista_reserva)

        if eleccion_clase=='3':
            while True:
                print('1)Visualizar lista   2)Agregar avion   3)Eliminar avion   B)Volver')
                eleccion_metodo=input('Ingrese su eleccion: ')
                if eleccion_metodo=='1':
                    print(lista_avion)
                if eleccion_metodo=='2':
                    print('1)Nro serie   2)Modelo   3)Fecha alta  4)Estado')
                    listaComodin=[]
                    listaMenu=['Nro serie','Modelo','Fecha alta','Estado']
                    for i in range(4):
                        if i == 2:
                            print("Ahora a la fecha de alta.")
                            listaComodin.append(validarFecha())    
                        else:
                            user_input = str(input("Inroduzca {} : ".format(listaMenu[i])))
                            listaComodin.append(user_input)
                    #Todos los checks
                    listaComodin[0]=avion.check_nro_serie(listaComodin[0])
                    listaComodin[3]=avion.check_estado(listaComodin[3])
                    listaComodin[2]=persona.check_fecha(listaComodin[2])  
                    lista_avion.append(Nodo(avion(listaComodin[0], listaComodin[1], listaComodin[2],listaComodin[3])))
                
                if eleccion_metodo=='3':
                    input_principal=input('Ingrese el nro de viaje que desea eliminar: ')
                    if lista_avion.pop(input_principal,"nro_serie"): print('El avion con el nro de serie {} se ha eliminado correctamente'.format(input_principal))
                    else: ('El numero de serie ingresado no se encuentra en la base de datos')
                if eleccion_metodo=='B':
                    menu_clase(lista_persona,lista_empleado,lista_avion,lista_vuelo,lista_viaje,lista_reserva)
                
        if eleccion_clase=='4':
            while True:
                print('1)Visualizar lista   2)Agregar vuelo  B)Volver')
                eleccion_metodo=input('Ingrese su eleccion: ')
                if eleccion_metodo=='1':
                    print(lista_vuelo)
                if eleccion_metodo=='2':
                    print('1)Nro vuelo  2)Aeropuerto salida  3)Aeropuerto llegada   4)Legajo del piloto   5)Precio')
                    listaComodin=[]
                    listaMenu=['Nro vuelo'  ,'Aeropuerto salida' , 'Aeropuerto llegada'  ,'Legajo del piloto' ,  'Precio']
                    for i in range(5):
                        user_input = str(input("Inroduzca {} : ".format(listaMenu[i])))
                        listaComodin.append(user_input)
                        
                    #Todos los checks
                    listaComodin[0]=vuelo.check_nro_vuelo(listaComodin[0])
                    listaComodin[4]=vuelo.check_precio_vuelo(listaComodin[4])
                    listaComodin[3]=vuelo.check_piloto(listaComodin[3], lista_empleado)
                    lista_vuelo.append(Nodo(vuelo(listaComodin[0], listaComodin[1], listaComodin[2],listaComodin[3],listaComodin[4])))
                if eleccion_metodo=='B':
                    menu_clase(lista_persona,lista_empleado,lista_avion,lista_vuelo,lista_viaje,lista_reserva)
                
        if eleccion_clase=='5':
            while True:
                print('1)Visualizar lista   2)Agregar viaje     3)Eliminar viaje  B)Volver')
                eleccion_metodo=input('Ingrese su eleccion: ')
                if eleccion_metodo=='1':
                    print(lista_viaje)
                if eleccion_metodo=='2':
                    print('1)Nro viaje   2)Nro vuelo    3)Nro serie   4)Fecha')
                    listaComodin=[]
                    listaMenu=['Nro viaje' ,  'Nro vuelo'  ,  'Nro serie'  , 'Fecha']
                    for i in range(4):
                        if i == 3:
                            print("Ahora a la fecha del viaje.")
                            listaComodin.append(validarFecha())    
                        else:
                            user_input = str(input("Inroduzca {} : ".format(listaMenu[i])))
                            listaComodin.append(user_input)
                    #Todos los checks
                    listaComodin[0]=viaje.check_nro_viaje(listaComodin[0])
                    listaComodin[1]=viaje.check_vuelo(listaComodin[1], lista_vuelo)
                    listaComodin[2]=viaje.check_estado(listaComodin[2],lista_avion)
                    lista_viaje.append(Nodo(viaje(listaComodin[0], listaComodin[1], listaComodin[2],listaComodin[3])))
                if eleccion_metodo=='3':
                    input_principal=input('Ingrese el nro de viaje que desea eliminar: ')
                    if lista_viaje.pop(input_principal,"nro_viaje"): print('El viaje con el nro {} se ha eliminado correctamente'.format(input_principal))
                    else: print('El viaje ingresado no se encuentra en la base de datos')
                if eleccion_metodo=='B':
                    menu_clase(lista_persona,lista_empleado,lista_avion,lista_vuelo,lista_viaje,lista_reserva)
                
        if eleccion_clase=='6':
            while True:
                print('1)Visualizar lista   2)Agregar reserva   3)Eliminar reserva   B)Volver')
                eleccion_metodo=input('Ingrese su eleccion: ')
                if eleccion_metodo=='1':
                    print(lista_reserva)
                if eleccion_metodo=="2":
                    print('1)Nro reserva   2)DNI cliente   3)Legajo Empleado  4)Nro viaje   5)Monto')
                    listaComodin=[]
                    listaMenu=['Nro reserva' ,  'DNI cliente '  ,'Legajo Empleado' , 'Nro viaje ' , 'Monto']
                    for i in range(5):
                        user_input = str(input("Inroduzca {} :".format(listaMenu[i])))
                        listaComodin.append(user_input)
                    #Todos los checks
                    listaComodin[0]=reserva.check_nro_reserva(listaComodin[0])
                    listaComodin[1]=reserva.check_cliente(listaComodin[1],lista_persona)
                    listaComodin[2]=reserva.check_empleado(listaComodin[2],lista_empleado)
                    listaComodin[3]=reserva.check_viaje(listaComodin[3],lista_viaje)
                    listaComodin[4]=reserva.check_monto(listaComodin[4],listaComodin[3],lista_vuelo)
                    
                    if viaje.agregarpasajero(listaComodin[1], listaComodin[3],lista_viaje):
                        lista_reserva.append(Nodo(reserva(listaComodin[0], listaComodin[1], listaComodin[2],listaComodin[3],listaComodin[4])))
                    else:
                        print('Lamentablemente el vuelo está lleno ')
                if eleccion_metodo=='3':
                    input_principal=input('Ingrese la reserva que desea eliminar: ')
                    if lista_reserva.pop(input_principal,"nro_reserva"): print('La reserva nro {} se ha eliminado correctamente'.format(input_principal))
                    else: print('El viaje ingresado no se encuentra en la base de datos ')
                if eleccion_metodo=='B':
                    menu_clase(lista_persona,lista_empleado,lista_avion,lista_vuelo,lista_viaje,lista_reserva)


        if eleccion_clase=='S':
            menu()
def menu():
    while True:
        print("\033[1mBienvenido a aerolineas Mamba\033[0m")
        print("                                       |")
        print("                                       |")
        print("                                       |")
        print("                                     .-'-.")
        print("                                    ' ___ '")
        print("                          ---------'  .-.  '---------")
        print("          _________________________'  '-'  '_________________________")
        print("           ''''''-|---|--/    \==][^',_m_,'^][==/    \--|---|-''''''")
        print("                         \    /  ||/   H   \||  \    /")
        print("                          '--'   OO   O|O   OO   '--'")

        numero = input("\n Si se quiere registrar ingrese el número 1 si ya tiene una cuenta ingrese el número 2:   ")
        while numero != "1" and numero != "2": numero = input("Ingrese una opción válida:   ")
        if numero == "1":  
            us = input("Ingrese un usuario: ")
            if registrarse(us): print("Su usuario se creó con éxito")
        if numero == "2":
            us = input("Ingrese su usuario: ")
            con = input("Ingrese su contraseña: ")
            if login(us, con):
                menu_clase(lista_persona,lista_empleado,lista_avion,lista_vuelo,lista_viaje,lista_reserva)

menu()