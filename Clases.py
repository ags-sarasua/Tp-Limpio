import datetime


#validarNum valida que un número ingresado por el usuario sea un número entre cierto rango pedido
def validarNum(tipoDato: str, min: int, max: int) -> int:
    ingresado = min - 1
    booleana = False
    while(booleana == False):
        try:
            ingresado = int(input("Ingrese "+ tipoDato +": "))
            if(ingresado < min or ingresado > max):
                print("Error, el número debe estar entre {} y {}".format(min, max))
            else:
                return ingresado    
        except:
            print("Error, tiene que ingresar un número. intente de nuevo")       

#validarFecha recibe año, mes y día para convertirlo en un dato del tipo datetime 
def validarFecha():
    meses_31dias = [1, 3, 5, 7, 8, 10, 12]
    meses_30dias = [4, 6, 9, 11]

    año = validarNum("año", 1900, 2100)
    mes = validarNum("mes", 1, 12)

    # Pedir el día (acotado según el mes)
    if mes in meses_31dias:
        dia = validarNum("dia", 1, 31)
    elif mes in meses_30dias:
        dia = validarNum("dia", 1, 30)
    elif mes == 2:
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            dia = validarNum("dia", 1, 29)
        else:
            dia = validarNum("dia", 1, 28)
    return(datetime.date(año, mes, dia))

#login recibe un usuario y una contraseña para chequear si está en el sistema. 
def login(username, password):
    with open("Usuarios.txt", 'r', encoding='utf-8') as archivo:
        listaUsuarios=[]
        passwordList=[]
        for linea in archivo:
            usu, contra = linea.strip().split(".")
            listaUsuarios.append(usu)
            passwordList.append(contra)
        while username not in listaUsuarios:
            username = input("El usuario ingresado no existe. Intente de nuevo: ")
        index = listaUsuarios.index(username)
        while passwordList[index] != password:
            password = input("Error, contraseña incorrecta. Ingresela nuevamente: ")
        return True

#registrarse escribe el archivo que tiene los usuarios y contraseñas para registrar un nuevo usuario
def registrarse(username):
    with open("Usuarios.txt", 'r', encoding='utf-8') as archivo:
        listaUsuarios=[]
        for linea in archivo:
            usu = linea.strip().split(".")[0]
            listaUsuarios.append(usu)
    while username in listaUsuarios:
        username = input("Este nombre de usuario ya existe. Ingrese otro: ")
    password = input("Ingrese una contraseña: ")
    with open("Usuarios.txt", 'a', encoding='utf-8') as archivo:
        archivo.write(f"\n{username}.{password}")
        return True
    
#actualizar para las listas fijas
def actualizar(lista, input_principal, atributo_principal, atributo_a_buscar, nuevo_input):
    for objeto in lista:
        if getattr(objeto,atributo_principal)==input_principal:
            setattr(objeto,atributo_a_buscar,nuevo_input)
            return True
    return False

#persona
class persona: 
    def __init__(self,DNI,nombre,apellido,sexo,fecha_de_nacimiento,pais,mail,telefono):
        self.DNI=DNI
        self.nombre=nombre
        self.apellido=apellido
        self.sexo=sexo
        self.fecha_de_nacimiento=fecha_de_nacimiento
        self.pais=pais
        self.mail=mail
        self.telefono=telefono
        
    #chequear DNI: que sea un número de 8 digitos
    @staticmethod
    def check_DNI(DNI):
        while len(DNI)!=8 or DNI.isnumeric()==False:
            print('Error, el DNI debe ser un número de 8 dígitos.')
            DNI=input("Ingrese el DNI nuevamente: ")    
        return DNI

    #chequear nombre: que sea un string
    @staticmethod
    def check_nombre(nombre,tipo):
        while nombre.isnumeric()==True:
            print('El {} tiene números.'.format(tipo))
            nombre=input("Ingrese nuevamente: ")
        return nombre

    #chequear sexo: Femenino, Masculino u Otro
    @staticmethod
    def check_sexo(sexo):
        lista=["Femenino","Masculino","Otro"]
        while sexo not in lista:
            print('El sexo ingresado no es valido, debe ser "Femenino", "Masculino" u "Otro".')
            sexo=input("Ingrese el sexo nuevamente:")
        return sexo

    #chequear fechaNacimiento: datetime y que sea mas chica que la fecha de hoy
    @staticmethod
    def check_fecha(fecha):
        while fecha > datetime.date.today():
            print('La fecha ingresada no es valida, debe ser antes que el día de hoy')
            fecha=validarFecha()
        return fecha
      
    #chequear pais: string y que pertenezca a un pais real del archivo correspondiente
    @staticmethod
    def check_pais(pais):
        archivo = open('Paises.txt', 'r')
        paises = archivo.read()
        archivo.close()

        while pais not in paises:
           print('El pais ingresado no es valido, debe tener su primer letra en mayúscula')
           pais=input("Ingrese el pais nuevamente: ") 
        return pais
    
    @staticmethod    
    def check_existencia_DNI(DNI,lista_persona):        
        while lista_persona.buscar(DNI,"DNI","DNI"):
            DNI=input('Existe un usuario con su DNI, ingrese uno nuevo:   ')
            DNI=persona.check_DNI(DNI)
            DNI=persona.check_existencia_DNI(DNI,lista_persona)
            return DNI
        return DNI
    
    #check mail
    @staticmethod
    def check_sintaxis_mail(mail):
        while mail[-10:] !="@gmail.com" or len(mail)==10:
            mail=input('El mail fue ingresado incorrectamente:  ')
        return mail
    
    @staticmethod    
    def check_existencia_mail(mail,lista_persona):        
        while lista_persona.buscar(mail,"mail","mail"):
            mail=input('Existe un usuario con su mail, ingrese uno nuevo:   ')
            mail=persona.check_sintaxis_mail(mail)
            mail=persona.check_existencia_mail(mail,lista_persona)
            return mail
        return mail

    #check telefono
    @staticmethod
    def check_sintaxis_telefono(telefono):
        while len(telefono)!=10 or telefono.isnumeric()==False:
            print('Error, el telefono debe ser un número de 10 dígitos.')
            telefono=input("Ingrese el telefono nuevamente:  ")    
        return telefono

    @staticmethod    
    def check_existencia_telefono(telefono,lista_persona):        
        while lista_persona.buscar(telefono,"telefono","telefono"):
            telefono=input('Existe un usuario con su telefono, ingrese uno nuevo:   ')
            telefono=persona.check_sintaxis_telefono(telefono)
            telefono=persona.check_existencia_telefono(telefono,lista_persona)
            return telefono
        return telefono
    
#empleado
class empleado(persona):
    def __init__(self,DNI,nombre,apellido,sexo,fecha_de_nacimiento,pais,legajo,sector):
        super().__init__(DNI,nombre,apellido,sexo,fecha_de_nacimiento,pais,None,None)
        self.legajo=legajo
        self.sector=sector
    
    #esPiloto pregunta si ese empleado es un piloto devolviendo un booleano
    def esPiloto(self):
        return self.sector == "Piloto"


    def __str__(self):
        return "Empleado DNI {}, se llama {}, {}, sexo {}, nació el {}, oriundo de {}, legajo {}, trabaja como {}".format(self.DNI,self.nombre,self.apellido,self.sexo,self.fecha_de_nacimiento,self.pais,self.legajo,self.sector)

    @staticmethod
    def DNI_repetido_empleado(DNI,lista_empleado):
        for objeto in lista_empleado:
            if objeto.DNI==DNI:
                DNI=input('Ingreso un DNI de un empleado preexistente. Ingrese uno nuevo:  ')
                empleado.check_DNI(DNI)
                empleado.DNI_repetido_empleado(DNI,lista_empleado)
                return DNI
        return DNI
    
    
    #chequear legajo: que sea un numero de 4 digitos y que no esté repetido 
    @staticmethod
    def checklegajo(legajo, lista_empleado):
        if legajo.isnumeric()==False:
                print('El legajo debe ser un número')
                legajo=input("Ingrese el legajo nuevamente:")
                legajo=empleado.checklegajo(legajo, lista_empleado)
        elif(len(legajo) != 4):
            print('El legajo debe tener 4 caracteres')
            legajo=input("Ingrese el legajo nuevamente:")
            legajo = empleado.checklegajo(legajo, lista_empleado)
        else:        
            for e in lista_empleado:
                if(e.legajo == legajo):
                    print('El legajo ingresado ya existe')
                    legajo=input("Ingrese el legajo nuevamente:")
                    legajo = empleado.checklegajo(legajo, lista_empleado)
                    break                                
        return legajo    
                             
    #chequear sector: que sea un sector preexistente
    @staticmethod
    def checksector(sector):
        lista_sectores=["Piloto","Administrativo","Tecnico"]
        while sector not in lista_sectores:
            print('El sector debe ser preexistente')
            sector=input("Ingrese el sector nuevamente:")
        return sector

#avion
class avion:
    def __init__(self,nro_serie,modelo,fecha_alta,estado):
        self.nro_serie=nro_serie
        self.modelo=modelo
        self.fecha_alta=fecha_alta
        self.estado=estado
    
    def __str__(self):
        return 'Nro de serie: {}, modelo: {}, fecha de alta: {}, estado: {}'. format(self.nro_serie,self.modelo,self.fecha_alta,self.estado)
    
    #dado un número de serie, elimina la instancia de la lista de aviones
    def eliminarAvion(nro_serie,matriz_aviones):
        for i in matriz_aviones:
            if i[0]==nro_serie:
                matriz_aviones.pop(i)
        return matriz_aviones
    
    @staticmethod
    def nroSerie_repetido_empleado(nro_serie,lista_avion):    
        for objeto in lista_avion:
            if objeto.nro_serie==nro_serie:
                nro_serie=input('Ingrese un nro de serie nuevo:  ')
                nro_serie=avion.check_sintaxis_nro_serie(nro_serie)
                nro_serie=avion.nroSerie_repetido_empleado(nro_serie,lista_avion)
                return nro_serie
        return nro_serie
            
    #Chequea que el número de serie del avión sea un número de 10 dígitos
    @staticmethod
    def check_sintaxis_nro_serie(nro_serie):
        while(len(nro_serie)!=10 or nro_serie.isnumeric() is not True ):
            nro_serie=input('Ingrese nuevamente el nro de serie:    ')
        return nro_serie

    #Chequea si el estado ingresado es uno preexistente
    @staticmethod
    def check_estado(estado):    
        while(estado not in ['En servicio','Fuera de servicio']):
            estado=input('El estado del avion debe ser "En servicio" o "Fuera de servicio", Ingrese nuevamente:    ')
        return estado

#vuelo
class vuelo:
    def __init__(self,nro_vuelo,aeropuerto_salida,aeropuerto_llegada,legajo_piloto,precio):
        self.nro_vuelo=nro_vuelo
        self.aeropuerto_salida=aeropuerto_salida
        self.aeropuerto_llegada=aeropuerto_llegada
        self.legajo_piloto=legajo_piloto
        self.precio=precio

    #Verifica que el vuelo sea un número de 4 dígitos
    @staticmethod
    def check_sintaxis_nro_vuelo(nro_vuelo):
        while len(nro_vuelo)!=4 or not nro_vuelo.isnumeric():
            nro_vuelo = input("Error, debe ingresar un número de 4 dígitos: ")
        return nro_vuelo
    
    @staticmethod
    def check_existencia_nro_vuelo(nro_vuelo,lista_vuelo):        
        while lista_vuelo.buscar(nro_vuelo,"nro_vuelo","nro_vuelo"):
            nro_vuelo=input('Existe un vuelo con ese nro de vuelo , ingrese uno nuevo:   ')
            nro_vuelo=vuelo.check_sintaxis_nro_vuelo(nro_vuelo)
            nro_vuelo=vuelo.check_existencia_nro_vuelo(nro_vuelo,lista_vuelo)
            return nro_vuelo
        return nro_vuelo
    
    #Chequea si el precio ingresado es un número positivo
    @staticmethod
    def check_precio_vuelo(precio):
        while not precio.isnumeric() or int(precio) < 0 :
            precio = input("El precio tiene que ser un número positivo: ")
        return precio

    #Busca en la clase empleado si el legajo dado corresponde a un empleado, luego verifica si es un piloto
    @staticmethod
    def check_piloto(legajo_piloto, lista_empleado):
        while True:
            empleado_encontrado = False
            for empleado in lista_empleado:
                if empleado.legajo == legajo_piloto:
                    empleado_encontrado = True
                    if empleado.esPiloto():
                        return legajo_piloto
                    else:
                        print("Este empleado no es un piloto.")
                        break
            if not empleado_encontrado:
                print("El legajo ingresado no existe.")
            legajo_piloto = input("Ingrese el legajo de un piloto: ")

#viaje   
class viaje:
    capacidad=5
    def __init__(self,nro_viaje,nro_vuelo,nro_serie,fecha):
        self.nro_viaje=nro_viaje
        self.nro_vuelo=nro_vuelo
        self.nro_serie=nro_serie
        self.fecha=fecha
        self.pasajeros=[]
        self.contador_pasajeros = 0
    
    def agregar_pasajero(nro_viaje, pasajero, lista_viaje):
        nodo_actual = lista_viaje.head
        while nodo_actual is not None:
            if nodo_actual.dato.nro_viaje == nro_viaje:
                if len(nodo_actual.dato.pasajeros) < 5:
                    if pasajero not in nodo_actual.dato.pasajeros:
                        nodo_actual.dato.pasajeros.append(pasajero)
                        nodo_actual.dato.contador_pasajeros += 1
                        return True
                    else:
                        print("El pasajero ya está en la lista.")
                        return False
                else:
                    print("El viaje ya está lleno.")
                    return False
            nodo_actual = nodo_actual.prox
        print("El número de viaje no fue encontrado.")
        return False
    def eliminar_pasajero(nro_viaje, pasajero, lista_viaje):
        nodo_actual = lista_viaje.head
        while nodo_actual is not None:
            if nodo_actual.dato.nro_viaje == nro_viaje:
                if pasajero in nodo_actual.dato.pasajeros:
                        nodo_actual.dato.pasajeros.remove(pasajero)
                        nodo_actual.dato.contador_pasajeros-=1
                        return True
                else:
                    print("El pasajero no está en el vuelo indicado")
                    return False
            nodo_actual = nodo_actual.prox
        print("El número de viaje no fue encontrado.")
        return False



    #Chequea que el vuelo existe en la clase Vuelo
    @staticmethod
    def check_vuelo(nro_vuelo,lista_vuelo):
        while True:
            if lista_vuelo.buscar(nro_vuelo,"nro_vuelo","nro_vuelo"):
                return nro_vuelo
            else:
                nro_vuelo = input("Error, el vuelo no existe. Intente de nuevo: ")


        #Verifica que el número de serie del avión sea de uno existente
    @staticmethod
    def check_nro_serie(nro_serie,lista_avion):
            while True:
                for serie in lista_avion:
                    if serie.nro_serie==nro_serie:
                        return nro_serie
                nro_serie = input("Error, el número de serie no existe. Intente de nuevo: ")
    #Verifica si el avión está en servicio activo
    @staticmethod
    def check_estado(nro_serie,lista_avion):
        while True:
            for avion in lista_avion:
                if avion.nro_serie==nro_serie:
                    if avion.estado!="En servicio":
                        nro_serie=input('Error. Debe ingresar un numero de serie de un avion en servicio ')
                    else:
                        return nro_serie
    
    #Pide que el número de viaje sea de 4 dígitos
    @staticmethod
    def check_sintaxis_nro_viaje(nro_viaje):
        while(nro_viaje.isnumeric()!=True or len(nro_viaje)!=4):
            nro_viaje=input('Error, el nro. de viaje tiene que ser un numero de 4 digitos. Ingrese nuevamente:    ')
        return nro_viaje
    @staticmethod
    def check_existencia_nro_viaje(nro_viaje,lista_viaje):        
        while lista_viaje.buscar(nro_viaje,"nro_viaje","nro_viaje"):
            nro_viaje=input('Existe un viaje con ese nro de viaje , ingrese uno nuevo:   ')
            nro_viaje=viaje.check_sintaxis_nro_viaje(nro_viaje)
            nro_viaje=viaje.check_existencia_nro_viaje(nro_viaje,lista_viaje)
            return nro_viaje
        return nro_viaje

#reserva
class reserva: 
    def __init__(self,nro_reserva,DNI_cliente,legajo_empleado,nro_viaje,monto):
        self.nro_reserva=nro_reserva
        self.DNI_cliente=DNI_cliente
        self.empleado=legajo_empleado
        self.nro_viaje=nro_viaje
        self.monto=monto

    #Pide que el nro de reserva sea un numérico de 4 dígitos
    @staticmethod
    def check_sintaxis_nro_reserva(nro_reserva):
        while(nro_reserva.isnumeric()!=True or len(nro_reserva)!=4):
            nro_reserva=input('Error, el nro. de factura tiene que ser un numero de 4 digitos. Ingrese nuevamente:    ')
        return nro_reserva
    @staticmethod
    def check_existencia_nro_reserva(nro_reserva,lista_reserva):        
        while lista_reserva.buscar(nro_reserva,"nro_reserva","nro_reserva"):
            nro_reserva=input('Existe una reserva con ese nro de reserva , ingrese uno nuevo:   ')
            nro_reserva=reserva.check_sintaxis_nro_reserva(nro_reserva)
            nro_reserva=reserva.check_existencia_nro_reserva(nro_reserva,lista_reserva)
            return nro_reserva
        return nro_reserva
    
    #Verifica que el DNI  sea de un pasajero existente
    @staticmethod
    def check_cliente(DNI_pasajero,lista_pasajero):
        while(True):
            if lista_pasajero.buscar(DNI_pasajero,"DNI","DNI"):
                return DNI_pasajero
            else: 
                DNI_pasajero=input('Error, el DNI tiene que ser de un pasajero existente. Ingrese nuevamente:    ')
    
    #Verifica que el legajo del empleado sea de un empleado existente
    @staticmethod
    def check_empleado(legajo_empleado,lista_empleado):
        while(True):
            for empleado in lista_empleado:
                if empleado.legajo==legajo_empleado:
                    return legajo_empleado
            legajo_empleado=input('Error, no se encuentra empleado con ese legajo. Ingrese nuevamente:    ')
            
    #Verifica que el viaje ingresado en la reserva corresponda a uno existente
    @staticmethod
    def check_viaje(nro_viaje,lista_viaje):
        while(True):
            if lista_viaje.buscar(nro_viaje,"nro_viaje","nro_viaje"):
                return nro_viaje
            else: 
                nro_viaje=input('Error, el viaje ingresado no corresponde con uno existente. Ingrese nuevamente:    ') 
    
    #Chequea que el monto ingresado en la reserva sea el correspondiente
    @staticmethod
    def check_monto(precio,nro_viaje,lista_viaje,lista_vuelo):
        nro_vuelo=lista_viaje.buscar(nro_viaje,"nro_viaje","nro_vuelo")
        while True:
            if lista_vuelo.buscar(nro_vuelo,"nro_vuelo","precio")==precio:
                return precio
            else: 
                precio=input('Monto incorrecto, ingrese nuevamente su monto:    ')