from listasenlazadas import *
from Clases import *
from ListaObjetos import *
import matplotlib.pyplot as mlp

#----------------

#menu una vez ingresado 
def menu_clase(lista_persona,lista_empleado,lista_avion,lista_vuelo,lista_viaje,lista_reserva):
    while True:
        print('1)Persona    2)Empleado    3)Avion    4)Vuelo    5)Viaje      6)Reserva    S)Salir')
        
        eleccion_clase=input('Ingrese su eleccion: ')
#persona
        if eleccion_clase=='1':
            while True:  #Para que una vez hagas algun metodo puedas volver a este lugar
                print('1)Visualizar lista   2)Agregar persona   3)Actualizar Persona  4) Eliminar persona  B)Volver')
                eleccion_metodo=input('Ingrese su eleccion: ')
                if eleccion_metodo=='1':
                    print(lista_persona)
                if eleccion_metodo=='2':
                    print('1)DNI   2)Nombre   3)Apellido   4)Sexo  5)Fecha de nacimiento   6)Pais   7)Mail   8)Telefono')
                    print('\n \t Comentario')
                    print('DNI: 8 digitos numericos \nSexo: Masculino, Fenenino, Otro \nPais: en mayuscula y en ingles  \nMail: terminar en @gmail.com  \nTelefono: 10 digitos numericos \n')
                    listaComodin=[]
                    listaMenu = ['DNI', 'Nombre', 'Apellido','Sexo', 'Fecha de nacimiento', 'Pais','Mail','Telefono']
                    for i in range(8):
                        if i == 4:
                            print("Ahora a la fecha de nacimiento.")
                            listaComodin.append(validarFecha())    
                        else:
                            user_input = str(input("Inroduzca {} : ".format(listaMenu[i])))
                            listaComodin.append(user_input)
                    listaComodin[0]=persona.check_DNI(listaComodin[0])
                    listaComodin[0]=persona.check_existencia_DNI(listaComodin[0],lista_persona)
                    listaComodin[1]=persona.check_nombre(listaComodin[1],'nombre')
                    listaComodin[2]=persona.check_nombre(listaComodin[2],'apellido')
                    listaComodin[3]=persona.check_sexo(listaComodin[3])
                    listaComodin[4]=persona.check_fecha(listaComodin[4])
                    listaComodin[5]=persona.check_pais(listaComodin[5])
                    listaComodin[6]=persona.check_sintaxis_mail(listaComodin[6])
                    listaComodin[6]=persona.check_existencia_mail(listaComodin[6],lista_persona)
                    listaComodin[7]=persona.check_sintaxis_telefono(listaComodin[7])
                    listaComodin[7]=persona.check_existencia_telefono(listaComodin[7],lista_persona)
                    lista_persona.append(Nodo(persona(listaComodin[0], listaComodin[1], listaComodin[2],listaComodin[3],listaComodin[4],listaComodin[5],listaComodin[6],listaComodin[7])))

                if eleccion_metodo=='3':
                    print('1)DNI   2)Nombre     3)Apellido   4)Sexo  5)Fecha de nacimiento   6)Pais     7)Mail    8)Telefono')
                    print('\n \t Comentario')
                    print('DNI: 8 digitos numericos \nSexo: Masculino, Fenenino, Otro \nPais: en mayuscula y en ingles  \nMail: terminar en @gmail.com  \nTelefono: 10 digitos numericos \n')
                    input_principal=input("ingrese el DNI de la persona a actualizar:    ")
                    input_principal=persona.check_DNI(input_principal)
                    eleccion_actualizar=input("Ingrese numero de atributo a actualizar:   ")
                    
                    if eleccion_actualizar!="5" and eleccion_actualizar in ['1','2','3','4','6','7','8']:
                        nuevo_input=input("Ingrese el valor a actualizar:    ")
                        if eleccion_actualizar=="1":
                            nuevo_input=persona.check_DNI(nuevo_input) 
                            if lista_persona.actualizar_le(input_principal,"DNI","DNI",nuevo_input) == False:
                                print("El DNI ingresado no corresponde al de una persona existente. La información no ha sido actualizada con exito.")

                        elif eleccion_actualizar=="2":
                            nuevo_input=persona.check_nombre(nuevo_input,"nombre")
                            if lista_persona.actualizar_le(input_principal,"DNI","nombre",nuevo_input) == False:
                                print("El DNI ingresado no corresponde al de una persona existente. La información no ha sido actualizada con exito.")

                        elif eleccion_actualizar=="3":
                            nuevo_input=persona.check_nombre(nuevo_input,"apellido") 
                            if lista_persona.actualizar_le(input_principal,"DNI","apellido",nuevo_input) == False:
                                print("El DNI ingresado no corresponde al de un persona existente. La información no ha sido actualizada con exito.")

                        elif eleccion_actualizar=="4":
                            nuevo_input=persona.check_sexo(nuevo_input)
                            if lista_persona.actualizar_le(input_principal,"DNI","sexo",nuevo_input) == False:
                                print("El DNI ingresado no corresponde al de un persona existente. La información no ha sido actualizada con exito.")

                        
                        elif eleccion_actualizar=="6":
                            nuevo_input=persona.check_pais(nuevo_input)
                            if lista_persona.actualizar_le(input_principal,"DNI","pais",nuevo_input) == False:
                                print("El DNI ingresado no corresponde al de un persona existente. La información no ha sido actualizada con exito.")

                        elif eleccion_actualizar=="7":
                            nuevo_input=persona.check_sintaxis_mail(nuevo_input) 
                            if lista_persona.actualizar_le(input_principal,"DNI","mail",nuevo_input) == False:
                                print("El DNI ingresado no corresponde al de un persona existente. La información no ha sido actualizada con exito.")
                            

                        elif eleccion_actualizar=="8":
                            nuevo_input=persona.check_sintaxis_telefono(nuevo_input)
                            if lista_persona.actualizar_le(input_principal,"DNI","telefono",nuevo_input) == False:
                                print("El DNI ingresado no corresponde al de un persona existente. La información no ha sido actualizada con exito.")

                    elif eleccion_actualizar=="5":
                            nuevo_input=validarFecha()
                            nuevo_input=persona.check_fecha(nuevo_input)
                            if lista_persona.actualizar_le(input_principal,"DNI","fecha_de_nacimiento",nuevo_input) == False:
                                print("El DNI ingresado no corresponde al de un persona existente. La información no ha sido actualizada con exito.")
                    
                    else: print("Ingrese alguna de las opciones numéricas y vuelva a intentarlo")
                                            

                if eleccion_metodo=='4':
                    DNI=input("Ingrese el DNI de la persona que quiere eliminar: ")
                    if lista_persona.pop(DNI,"DNI"):
                        print("Se eliminó correctamente la persona indicada")
                    else:
                        print("No se puedo eliminar correctamente la persona indicada")


                if eleccion_metodo=='B' or eleccion_metodo =="b":
                    menu_clase(lista_persona,lista_empleado,lista_avion,lista_vuelo,lista_viaje,lista_reserva)
#empleado     
        if eleccion_clase=='2':
            while True:
                print('1)Visualizar lista   2)Agregar empleado   3)Eliminar empleado  4)Actualizar empleado  5)Graficar   B)Volver')
                eleccion_metodo=input('Ingrese su eleccion: ')
                if eleccion_metodo=='1':
                    for empleado in lista_empleado:
                        print(empleado)
                if eleccion_metodo=='2':
                    print('1)DNI   2)Nombre  3)Apellido  4)Sexo  5)Fecha de nacimiento   6)Pais    7)Legajo    8)Sector')
                    print('\n \t Comentario')
                    print('DNI: 8 digitos numericos \nSexo: Masculino, Femenino, Otro \nPais: en mayuscula y en ingles  \nLegajo: 4 numeros \nSector: Piloto,Tecnico,Administrativo \n')
                    listaComodin=[]
                    listaMenu = ['DNI', 'Nombre','Apellido', 'Sexo', 'Fecha de nacimiento', 'Pais','Legajo','Sector']
                    for i in range(8):
                        if i == 4:
                            print("Ahora a la fecha de nacimiento.")
                            listaComodin.append(validarFecha())    
                        else:
                            user_input = str(input("Inroduzca {} : ".format(listaMenu[i])))
                            listaComodin.append(user_input)
                    listaComodin[0]=persona.check_DNI(listaComodin[0])
                    listaComodin[0]=Clases.empleado.DNI_repetido_empleado(listaComodin[0],lista_empleado)
                    listaComodin[1]=persona.check_nombre(listaComodin[1],'nombre')
                    listaComodin[2]=persona.check_nombre(listaComodin[2],'apellido')
                    listaComodin[3]=persona.check_sexo(listaComodin[3])
                    listaComodin[4]=persona.check_fecha(listaComodin[4])
                    listaComodin[5]=persona.check_pais(listaComodin[5])
                    listaComodin[6]=Clases.empleado.checklegajo(listaComodin[6], lista_empleado)
                    listaComodin[7]=Clases.empleado.checksector(listaComodin[7])
                    lista_empleado.append(Clases.empleado(listaComodin[0], listaComodin[1], listaComodin[2],listaComodin[3],listaComodin[4],listaComodin[5],listaComodin[6],listaComodin[7]))

                if eleccion_metodo=='3':
                    input_principal=input('Ingrese el DNI del empleado que desea eliminar: ')
                    flag=False
                    for empleado in lista_empleado:
                        if input_principal==empleado.DNI:
                            lista_empleado.remove(empleado)
                            flag=True
                            print('El empleado con el DNI {} se ha eliminado correctamente'.format(input_principal))
                    if flag==False:
                        print('El empleado ingresado no se encuentra en la base de datos')

                if eleccion_metodo=='4':
                    print('1)DNI   2)Nombre     3)Apellido   4)Sexo  5)Fecha de nacimiento   6)Pais    7)Legajo    8)Sector')
                    print('\n \t Comentario')
                    print('DNI: 8 digitos numericos \nSexo: Masculino, Femenino, Otro \nPais: en mayuscula y en ingles  \nLegajo: 4 numeros \nSector: Piloto,Tecnico,Administrativo \n')                    
                    input_principal=input("ingrese el DNI del empleado a actualizar:    ")
                    input_principal=persona.check_DNI(input_principal)
                    eleccion_actualizar=input("Ingrese numero de atributo a actualizar:   ")
                    

                    if eleccion_actualizar!="5" and eleccion_actualizar in ['1','2','3','4','6','7','8']:
                        nuevo_input=input("Ingrese el valor a actualizar:    ")
                        if eleccion_actualizar=="1":
                            nuevo_input=persona.check_DNI(nuevo_input)
                            if actualizar(lista_empleado,input_principal,"DNI","DNI",nuevo_input)==False:
                                print("El DNI ingresado no corresponde al de un empleado existente. La información no ha sido actualizada con exito.")

                        elif eleccion_actualizar=="2":
                            nuevo_input=persona.check_nombre(nuevo_input,"nombre")
                            if actualizar(lista_empleado,input_principal,"DNI","nombre",nuevo_input)==False:
                                print("El DNI ingresado no corresponde al de un empleado existente. La información no ha sido actualizada con exito.")
                                
                        elif eleccion_actualizar=="3":
                            nuevo_input=persona.check_nombre(nuevo_input,"apellido")
                            if actualizar(lista_empleado,input_principal,"DNI","apellido",nuevo_input)==False:
                                print("El DNI ingresado no corresponde al de un empleado existente. La información no ha sido actualizada con exito.")

                        elif eleccion_actualizar=="4":
                            nuevo_input=persona.check_sexo(nuevo_input)
                            if actualizar(lista_empleado,input_principal,"DNI","sexo",nuevo_input)==False:
                                print("El DNI ingresado no corresponde al de un empleado existente. La información no ha sido actualizada con exito.")
                        
                        elif eleccion_actualizar=="7":
                            nuevo_input=Clases.empleado.checklegajo(nuevo_input)
                            if actualizar(lista_empleado,input_principal,"DNI","legajo",nuevo_input)==False:
                                print("El DNI ingresado no corresponde al de un empleado existente. La información no ha sido actualizada con exito.") 

                        elif eleccion_actualizar=="6":
                            nuevo_input=persona.check_pais(nuevo_input)
                            if actualizar(lista_empleado,input_principal,"DNI","pais",nuevo_input)==False:
                                print("El DNI ingresado no corresponde al de un empleado existente. La información no ha sido actualizada con exito.")

                        elif eleccion_actualizar=="8":
                            nuevo_input=persona.check_sector(nuevo_input)
                            if actualizar(lista_empleado,input_principal,"DNI""sector",nuevo_input)==False:
                                print("El DNI ingresado no corresponde al de un empleado existente. La información no ha sido actualizada con exito.")

                    elif eleccion_actualizar=="5":
                            nuevo_input=validarFecha()
                            nuevo_input=persona.check_fecha_de_nacimiento(nuevo_input)
                            if actualizar(lista_empleado,input_principal,"DNI","fecha_de_nacimiento",nuevo_input)==False:
                                print(" El DNI ingresado no corresponde al de un empleado existente. La información no ha sido actualizada con exito.")
                    else: print("Ingrese alguna de las opciones numéricas y vuelva a intentarlo") 
            
                if eleccion_metodo=='5':
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
                                            
                if eleccion_metodo=='B' or eleccion_metodo =="b":
                    menu_clase(lista_persona,lista_empleado,lista_avion,lista_vuelo,lista_viaje,lista_reserva)
#avion
        if eleccion_clase=='3':
            while True:
                print('1)Visualizar lista   2)Agregar avion   3)Eliminar avion   4)Actualizar Avión   B)Volver')
                eleccion_metodo=input('Ingrese su eleccion: ')
                if eleccion_metodo=='1':
                    for avion in lista_avion:
                        print(avion)
                if eleccion_metodo=='2':
                    print('1)Nro serie   2)Modelo   3)Fecha alta  4)Estado')
                    print('\n \t Comentario')
                    print('Nro serie: 10 digitos numericos \nEstado: En servicio , Fuera de servicio \n')
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
                    listaComodin[0]=Clases.avion.check_sintaxis_nro_serie(listaComodin[0])
                    listaComodin[0]=Clases.avion.nroSerie_repetido_empleado(listaComodin[0],lista_avion)
                    listaComodin[3]=Clases.avion.check_estado(listaComodin[3])
                    listaComodin[2]=persona.check_fecha(listaComodin[2])  
                    lista_avion.append(Clases.avion(listaComodin[0], listaComodin[1], listaComodin[2],listaComodin[3]))
                
                if eleccion_metodo=='3':
                    input_principal=input('Ingrese el nro de serie del avión que desea eliminar: ')
                    flag=False
                    for avion in lista_avion:
                        if input_principal==avion.nro_serie:
                            lista_avion.remove(avion)
                            flag=True
                            print('El avión con el nro de serie {} se ha eliminado correctamente'.format(input_principal))
                    if flag==False:
                        print('El avión ingresado no se encuentra en la base de datos')                      
                
                if eleccion_metodo=='B' or eleccion_metodo =="b":
                    menu_clase(lista_persona,lista_empleado,lista_avion,lista_vuelo,lista_viaje,lista_reserva)

                if eleccion_metodo=='4':
                    print('1)Nro serie   2)Modelo   3)Fecha alta  4)Estado')
                    print('\n \t Comentario')
                    print('Nro serie: 10 digitos numericos \nEstado: En servicio , Fuera de servicio \n')
                    input_principal=input("ingrese el Nro de serie del avion a actualizar:    ")
                    input_principal=Clases.avion.check_sintaxis_nro_serie(input_principal)
                    eleccion_actualizar=input("Ingrese numero de atributo a actualizar:   ")
                    
                    if eleccion_actualizar!="3":
                        nuevo_input=input("Ingrese el valor a actualizar:    ")
                        
                        if eleccion_actualizar=="1":
                            nuevo_input=Clases.avion.check_nro_serie(nuevo_input)
                            if actualizar(lista_avion,input_principal,"nro_serie","nro_serie",nuevo_input) == False:
                                print("El número de serie ingresado no corresponde al de un avión existente. La información no ha sido actualizada con exito.")


                        elif eleccion_actualizar=="2":
                            nuevo_input=nuevo_input
                            if actualizar(lista_avion,input_principal,"nro_serie","modelo",nuevo_input) == False:
                                print("El número de serie ingresado no corresponde al de un avión existente. La información no ha sido actualizada con exito.")
                            
                        elif eleccion_actualizar=="4":
                            nuevo_input=Clases.avion.check_estado(nuevo_input)
                            if actualizar(lista_avion,input_principal,"nro_serie","fecha_alta",nuevo_input) == False:
                                print("El número de serie ingresado no corresponde al de un avión existente. La información no ha sido actualizada con exito.")

                    elif eleccion_actualizar=="3":
                        nuevo_input=validarFecha()
                        if actualizar(lista_avion,input_principal,"nro_serie","fecha_alta",nuevo_input) == False:
                            print("El número de serie ingresado no corresponde al de un avión existente. La información no ha sido actualizada con exito.")

                    else:
                        print("Ingrese una opción numérica válida y vuelva a intentarlo")
#Vuelo
        if eleccion_clase=='4':
            while True:
                print('1)Visualizar lista   2)Agregar vuelo   3)Actualizar Vuelo  4) Eliminar vuelo     B)Volver')
                eleccion_metodo=input('Ingrese su eleccion: ')
                if eleccion_metodo=='1':
                    print(lista_vuelo)
                if eleccion_metodo=='2':
                    print('1)Nro vuelo  2)Aeropuerto salida  3)Aeropuerto llegada   4)Legajo del piloto   5)Precio')
                    print('\n \t Comentario')
                    print('Nro vuelo: 4 digitos numericos \n')
                    listaComodin=[]
                    listaMenu=['Nro vuelo'  ,'Aeropuerto salida' , 'Aeropuerto llegada'  ,'Legajo del piloto' ,  'Precio']
                    for i in range(5):
                        user_input = str(input("Inroduzca {} : ".format(listaMenu[i])))
                        listaComodin.append(user_input)
                        
                    #Todos los checks
                    listaComodin[0]=Clases.vuelo.check_sintaxis_nro_vuelo(listaComodin[0])
                    listaComodin[0]=Clases.vuelo.check_existencia_nro_vuelo(listaComodin[0],lista_vuelo)
                    listaComodin[4]=Clases.vuelo.check_precio_vuelo(listaComodin[4])
                    listaComodin[3]=Clases.vuelo.check_piloto(listaComodin[3], lista_empleado)
                    lista_vuelo.append(Nodo(Clases.vuelo(listaComodin[0], listaComodin[1], listaComodin[2],listaComodin[3],listaComodin[4])))
                    
                if eleccion_metodo=='3':
                    print('1)Nro vuelo  2)Aeropuerto salida  3)Aeropuerto llegada    4)Legajo del piloto   5)Precio')
                    print('\n \t Comentario')
                    print('Nro vuelo: 4 digitos numericos \n')
                    input_principal=input("ingrese el Nro de vuelo del vuelo a actualizar:    ")
                    input_principal=Clases.vuelo.check_sintaxis_nro_vuelo(input_principal)
                    eleccion_actualizar=input("Ingrese numero de atributo a actualizar:   ")
                    nuevo_input=input("Ingrese el valor a actualizar:    ")

                    if eleccion_actualizar in ['1','2','3','4','5']:
                        if eleccion_actualizar=="1":
                            nuevo_input=Clases.vuelo.check_sintaxis_nro_vuelo(nuevo_input)
                            if lista_vuelo.actualizar_le(input_principal,"nro_vuelo","nro_vuelo",nuevo_input) == False:
                                print("El número de vuelo ingresado no corresponde al de un vuelo existente. La información no ha sido actualizada con exito.")
                        if eleccion_actualizar=="2":
                            if lista_vuelo.actualizar_le(input_principal,"nro_vuelo","aeropuerto_salida",nuevo_input) == False:
                                print("El número de vuelo ingresado no corresponde al de un vuelo existente. La información no ha sido actualizada con exito.")

                        if eleccion_actualizar=="3":
                            if lista_vuelo.actualizar_le(input_principal,"nro_vuelo","aeropuerto_llegada",nuevo_input) == False:
                                print("El número de vuelo ingresado no corresponde al de un vuelo existente. La información no ha sido actualizada con exito.")

                        if eleccion_actualizar=="4":
                            nuevo_input=Clases.vuelo.check_piloto(nuevo_input,lista_empleado) 
                            if lista_vuelo.actualizar_le(input_principal,"nro_vuelo","legajo_piloto",nuevo_input) == False:
                                print("El número de vuelo ingresado no corresponde al de un vuelo existente. La información no ha sido actualizada con exito.")

                        if eleccion_actualizar=="5":
                            nuevo_input=Clases.vuelo.check_precio_vuelo(nuevo_input)
                            if lista_vuelo.actualizar_le(input_principal,"nro_vuelo","precio",nuevo_input)  == False:
                                print("El número de vuelo ingresado no corresponde al de un vuelo existente. La información no ha sido actualizada con exito.")                

                    else:
                        print("Ingrese alguna de las opciones numéricas y vuelva a intentarlo")
                
                
                if eleccion_metodo=='4':
                    Clases.vuelo=input("Ingrese el número de vuelo que quiere eliminar: ")
                    if lista_vuelo.pop(Clases.vuelo,"nro_vuelo"):
                        print("Se eliminó correctamente el vuelo indicado")
                    else:
                        print("No se puedo eliminar correctamente el vuelo indicado")                

                if eleccion_metodo=='B' or eleccion_metodo =="b":
                    menu_clase(lista_persona,lista_empleado,lista_avion,lista_vuelo,lista_viaje,lista_reserva)           
#viaje
        if eleccion_clase=='5':
            while True:
                print('1)Visualizar lista   2)Agregar viaje     3)Eliminar viaje  4)Actualizar Viaje    B)Volver')
                eleccion_metodo=input('Ingrese su eleccion: ')
                if eleccion_metodo=='1':
                    print(lista_viaje)
                if eleccion_metodo=='2':
                    print('1)Nro viaje   2)Nro vuelo    3)Nro serie   4)Fecha')
                    print('\n \t Comentario')
                    print('Nro viaje: 4 digitos numericos \nNro vuelo: 4 digitos numericos \n')
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
                    listaComodin[0]=viaje.check_sintaxis_nro_viaje(listaComodin[0])
                    listaComodin[0]=viaje.check_existencia_nro_viaje(listaComodin[0],lista_viaje)
                    listaComodin[1]=viaje.check_vuelo(listaComodin[1], lista_vuelo)
                    listaComodin[2]=viaje.check_nro_serie(listaComodin[2],lista_avion)
                    listaComodin[2]=viaje.check_estado(listaComodin[2],lista_avion)
                    lista_viaje.append(Nodo(viaje(listaComodin[0], listaComodin[1], listaComodin[2],listaComodin[3])))
                if eleccion_metodo=='3':
                    input_principal=input('Ingrese el nro de viaje que desea eliminar: ')
                    if lista_viaje.pop(input_principal,"nro_viaje"): print('El viaje con el nro {} se ha eliminado correctamente'.format(input_principal))
                    else: print('El viaje ingresado no se encuentra en la base de datos')

                if eleccion_metodo=='4':
                    print('1)Nro viaje   2)Nro vuelo    3)Nro serie   4)Fecha')
                    print('\n \t Comentario')
                    print('Nro viaje: 4 digitos numericos \nNro vuelo: 4 digitos numericos \n')
                    input_principal=input("ingrese el Nro de viaje del viaje a actualizar:    ")
                    input_principal=Clases.viaje.check_sintaxis_nro_viaje(input_principal)
                    eleccion_actualizar=input("Ingrese numero de atributo a actualizar:   ")
                    
                    if eleccion_actualizar!="4" and eleccion_actualizar in ['1','2','3']:
                        nuevo_input=input("Ingrese el valor a actualizar:    ")

                
                        if eleccion_actualizar=="1":
                            nuevo_input=Clases.viaje.check_sintaxis_nro_viaje(nuevo_input)
                            if lista_viaje.actualizar_le(input_principal,"nro_viaje","nro_viaje",nuevo_input) == False:
                                print("El número de viaje ingresado no corresponde al de un viaje existente. La información no ha sido actualizada con exito.")
                        elif eleccion_actualizar=="2":
                            nuevo_input=Clases.vuelo.check_sintaxis_nro_vuelo(nuevo_input)
                            if lista_viaje.actualizar_le(input_principal,"nro_viaje","nro_vuelo",nuevo_input) == False:
                                print("El número de viaje ingresado no corresponde al de un viaje existente. La información no ha sido actualizada con exito.")

                        elif eleccion_actualizar=="3":
                            nuevo_input=Clases.avion.check_sintaxis_nro_serie(nuevo_input)
                            if lista_viaje.actualizar_le(input_principal,"nro_viaje","nro_serie",nuevo_input) == False:
                                print("El número de viaje ingresado no corresponde al de un viaje existente. La información no ha sido actualizada con exito.")
                    elif eleccion_actualizar=="4":
                        nuevo_input=validarFecha()
                        if lista_viaje.actualizar_le(input_principal,"nro_viaje","fecha",nuevo_input) == False:             
                            print("El número de viaje ingresado no corresponde al de un viaje existente. La información no ha sido actualizada con exito.")
                    
                    else: print("Ingrese alguna de las opciones númericas y vuelva a intentarlo")
                
                
                
                if eleccion_metodo=='B' or eleccion_metodo =="b":
                    menu_clase(lista_persona,lista_empleado,lista_avion,lista_vuelo,lista_viaje,lista_reserva)
#reserva              
        if eleccion_clase=='6':
            while True:
                print('1)Visualizar lista   2)Agregar reserva   3)Eliminar reserva    4)Actualizar Reserva   B)Volver')
                eleccion_metodo=input('Ingrese su eleccion: ')
                if eleccion_metodo=='1':
                    print(lista_reserva)
                if eleccion_metodo=="2":
                    print('1)Nro reserva   2)DNI cliente   3)Legajo Empleado  4)Nro viaje   5)Monto')
                    print('\n \t Comentario')
                    print('Nro reserva: 4 digitos numericos  \nDNI: 8 digitos numericos   \nLegajo: 4 digitos numericos   \nNro viaje: 4 numeros \n')
                    listaComodin=[]
                    listaMenu=['Nro reserva' ,  'DNI cliente '  ,'Legajo Empleado' , 'Nro viaje ' , 'Monto']
                    for i in range(5):
                        user_input = str(input("Inroduzca {} :".format(listaMenu[i])))
                        listaComodin.append(user_input)
                    #Todos los checks
                    listaComodin[0]=reserva.check_sintaxis_nro_reserva(listaComodin[0])
                    listaComodin[0]=reserva.check_existencia_nro_reserva(listaComodin[0],lista_reserva)
                    listaComodin[1]=reserva.check_cliente(listaComodin[1],lista_persona)
                    listaComodin[2]=reserva.check_empleado(listaComodin[2],lista_empleado)
                    listaComodin[3]=reserva.check_viaje(listaComodin[3],lista_viaje)
                    listaComodin[4]=reserva.check_monto(listaComodin[4],listaComodin[3],lista_viaje, lista_vuelo)
                    
                    if viaje.agregar_pasajero(listaComodin[3], listaComodin[1],lista_viaje): 
                        lista_reserva.append(Nodo(reserva(listaComodin[0], listaComodin[1], listaComodin[2],listaComodin[3],listaComodin[4])))
                if eleccion_metodo=='3':
                    input_principal=input('Ingrese la reserva que desea eliminar: ')
                    dni_ingresado=input("Ingrese el dni del pasajero: ")
                    viaje_ingresado=input("Ingrese el número de viaje del cual desea eliminar al pasajero: ")

                    if viaje.eliminar_pasajero(viaje_ingresado,dni_ingresado,lista_viaje): 
                        if lista_reserva.pop(input_principal,"nro_reserva"):
                            print('La reserva nro {} se ha eliminado correctamente'.format(input_principal))
                    
                if eleccion_metodo=='4':
                    print('1)Nro reserva   2)DNI cliente   3)Legajo Empleado  4)Nro viaje')
                    print('\n \t Comentario')
                    print('Nro reserva: 4 digitos numericos  \nDNI: 8 digitos numericos   \nLegajo: 4 digitos numericos   \nNro viaje: 4 numeros \n')
                    input_principal=input("ingrese el Nro de reserva de la reserva a actualizar:    ")
                    input_principal=Clases.reserva.check_sintaxis_nro_reserva(input_principal)
                    eleccion_actualizar=input("Ingrese numero del atributo a actualizar:   ")
                    nuevo_input=input("Ingrese el valor a actualizar:    ")

                    if eleccion_actualizar in ['1','2','3','4']:
                        if eleccion_actualizar=="1":
                            nuevo_input=Clases.reserva.check_sintaxis_nro_reserva(nuevo_input)
                            if lista_reserva.actualizar_le(input_principal,"nro_reserva","nro_reserva",nuevo_input) == False:
                                print("El número de reserva ingresado no corresponde al de un reserva existente. La información no ha sido actualizada con exito.")
                        if eleccion_actualizar=="2":
                            nuevo_input=Clases.persona.check_DNI(nuevo_input)
                            if lista_reserva.actualizar_le(input_principal,"nro_reserva","DNI_cliente",nuevo_input) == False:
                                print("El número de reserva ingresado no corresponde al de un reserva existente. La información no ha sido actualizada con exito.")
                        if eleccion_actualizar=="3":
                            nuevo_input=Clases.empleado.check_legajo_existente(nuevo_input, lista_empleado)
                            if lista_reserva.actualizar_le(input_principal,"nro_reserva","empleado",nuevo_input) == False:
                                print("El número de reserva ingresado no corresponde al de un reserva existente. La información no ha sido actualizada con exito.")
                        if eleccion_actualizar=="4":
                            
                            nuevo_input=Clases.viaje.check_sintaxis_nro_viaje(nuevo_input,lista_viaje)
                            if lista_reserva.actualizar_le(input_principal,"nro_reserva","nro_viaje",nuevo_input) == False:
                                print("El número de reserva ingresado no corresponde al de un reserva existente. La información no ha sido actualizada con exito.")

                        
                    else:
                        print("Ingrese alguna de las opciones numéricas y vuelva a intentarlo")




                if eleccion_metodo=='B' or eleccion_metodo =="b":
                    menu_clase(lista_persona,lista_empleado,lista_avion,lista_vuelo,lista_viaje,lista_reserva)
#salir
        if eleccion_clase=='S' or eleccion_clase =="s":
            menu()

#Menu de ingreso
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