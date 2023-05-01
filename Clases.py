import datetime

#validarNum valida que un número ingresado por el usuario sea un número entre cierto rango pedido
def validarNum(tipoDato, min, max):
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
        print(listaUsuarios)
    while username in listaUsuarios:
        username = input("Este nombre de usuario ya existe. Ingrese otro: ")
    password = input("Ingrese una contraseña: ")
    with open("Usuarios.txt", 'a', encoding='utf-8') as archivo:
        archivo.write(f"\n{username}.{password}")
        print("Se creó el usuario con éxito")
        return True
class persona:
    def __init__(self,DNI,nombre,sexo,fecha_de_nacimiento,pais):
        self.DNI=DNI
        self.nombre=nombre
        self.sexo=sexo
        self.fecha_de_nacimiento=fecha_de_nacimiento
        self.pais=pais
        
    #chequear DNI: que sea un número de 8 digitos
    @staticmethod
    def check_DNI(DNI):
        while len(DNI)!=8 or DNI.isnumeric()==False:
            print('Error, el DNI debe ser un número de 8 dígitos.')
            DNI=input("Ingrese el DNI nuevamente: ")    
        return DNI

    #chequear nombre: que sea un string
    @staticmethod
    def check_nombre(nombre):
        while nombre.isnumeric()==True:
            print('Error, un nombre no tiene números.')
            nombre=input("Ingrese el nombre nuevamente: ")
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
    def check_fecha_de_nacimiento(fechaNacimiento):
        while fechaNacimiento > datetime.date.today():
            print('La fecha ingresada no es valida, debe ser antes que el día de hoy')
            fechaNacimiento=validarFecha()
        return fechaNacimiento
      
    #chequear pais: string y que pertenezca a un pais real del archivo correspondiente
    @staticmethod
    def check_pais(pais):
        archivo = open('Paises.txt', 'r')
        paises = archivo.read()
        archivo.close()

        while pais not in paises:
           print('El pais ingresado no es valido')
           pais=input("Ingrese el pais nuevamente:") 
        return pais 

class empleado(persona):
    def __init__(self,DNI,nombre,sexo,fecha_de_nacimiento,pais,legajo,sector):
        super().__init__(DNI,nombre,sexo,fecha_de_nacimiento,pais)
        self.legajo=legajo
        self.sector=sector
    
    #esPiloto pregunta si ese empleado es un piloto devolviendo un booleano
    def esPiloto(self):
        return self.sector == "piloto"

    def ActualizarEmpleado(DNI, PorCual, indice, lista_empleado):
        for empleado in lista_empleado:
            if empleado.DNI == DNI and (indice-1) < len(lista_empleado) and indice >= 1:
                lista_empleado[indice-1] = PorCual
        return lista_empleado

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


class avion:
    def __init__(self,nro_serie,modelo,fecha_alta,estado):
        self.nro_serie=nro_serie
        self.modelo=modelo
        self.fecha_alta=fecha_alta
        self.estado=estado
        print('Se creo bien')
    
    #dado un número de serie, elimina la instancia de la lista de aviones
    def eliminarAvion(nro_serie,matriz_aviones):
        for i in matriz_aviones:
            if i[0]==nro_serie:
                matriz_aviones.pop(i)
        return matriz_aviones
    
    #Chequea que el número de serie del avión sea un número de 10 dígitos
    @staticmethod
    def check_nro_serie(nro_serie):
        while(len(nro_serie)!=10 or nro_serie.isnumeric() is not True ):
            nro_serie=input('Ingrese nuevamente el nro de serie:    ')
        return nro_serie

    #Chequea si el estado ingresado es uno preexistente
    @staticmethod
    def check_estado(estado):    
        while(estado not in ['En servicio','Fuera de servicio']):
            estado=input('El estado del avion debe ser "En servicio" o "Fuera de servicio", Ingrese nuevamente:    ')
        return estado
    
class vuelo:
    def __init__(self,nro_vuelo,aeropuerto_salida,aeropuerto_llegada,nro_serie,legajo_piloto,precio):
        self.nro_vuelo=nro_vuelo
        self.aeropuerto_salida=aeropuerto_salida
        self.aeropuerto_llegada=aeropuerto_llegada
        self.nro_serie=nro_serie
        self.legajo_piloto=legajo_piloto
        self.precio=precio

    #Verifica que el vuelo sea un número de 4 dígitos
    @staticmethod
    def check_nro_vuelo(nro_vuelo):
        while len(nro_vuelo)!=4 or not nro_vuelo.isnumeric():
            nro_vuelo = input("Error, debe ingresar un número de 4 dígitos: ")
        return nro_vuelo
    
    #Chequea si el precio ingresado es un número positivo
    @staticmethod
    def check_precio_vuelo(precio):
        while int(precio) < 0 or not precio.isnumeric():
            precio = input("El precio tiene que ser un número positivo: ")
        return precio

    #Busca en la clase empleado si el legajo dado corresponde a un empleado, luego verifica si es un piloto
    @staticmethod
    def check_piloto(legajo_piloto,lista_empleado):  
        for empleado in lista_empleado:
            if empleado.legajo == legajo_piloto:
                piloto = empleado.esPiloto()
                while(piloto == False):
                    nuevo_legajo = ("Este empleado no es un piloto, ingrese nuevamente")
                    vuelo.check_piloto(nuevo_legajo, lista_empleado)
                break 
        return legajo_piloto

    #Verifica que el número de serie del avión sea de uno existente
    @staticmethod
    def check_nro_serie(nro_serie,lista_nro_serie):
            while True:
                for serie in lista_nro_serie:
                    if serie.nro_serie==nro_serie:
                        return avion.check_nro_serie(nro_serie)
                nro_serie = input("Error, el número de serie no existe. Intente de nuevo: ")
       
class viaje:
    capacidad=5
    def __init__(self,nro_viaje,nro_vuelo,nro_serie,fecha):
        self.nro_viaje=nro_viaje
        self.nro_vuelo=nro_vuelo
        self.nro_avion=nro_serie
        self.fecha=fecha
        self.pasajeros=[]
        self.contador_pasajeros = 0
    
    def eliminarViaje(nro_viaje,lista_viaje):
        for viaje in lista_viaje:
            if viaje.nro_viaje==nro_viaje:
                lista_viaje.pop(viaje)
        return lista_viaje
    
    def agregarpasajero(self, nroViaje, pasajero, listaViaje):
        for viaje in listaViaje:
            if viaje.nro_viaje == nroViaje:
                if self.contador_pasajeros < viaje.capacidad :
                    self.pasajeros.append(pasajero)
                    self.contador_pasajeros+=1
                    return True
                else:
                    return False

    def eliminarpasajero(self,pasajero):
        for i in self.pasajeros:
            if i==pasajero:
                self.pasajeros.pop(pasajero)
                self.contador_pasajeros-=1

    #Chequea que el vuelo existe en la clase Vuelo
    @staticmethod
    def check_vuelo(nro_vuelo,lista_vuelo):
        while True:
            for vuelo in lista_vuelo:
                if vuelo.nro_vuelo == nro_vuelo:
                    return nro_vuelo
            nro_vuelo = input("Error, el vuelo no existe. Intente de nuevo: ")

    #Verifica si el avión está en servicio activo
    @staticmethod
    def check_disponibilidad(self,nro_serie):
        if self.nro_serie==nro_serie:
            if self.estado=='Fuera de servicio':
                return False
            else:
                return True 

class reserva: 
    def __init__(self,nro_reserva,DNI_cliente,legajo_empleado,nro_viaje,monto):
        self.nro_reserva=nro_reserva
        self.DNI_cliente=DNI_cliente
        self.empleado=legajo_empleado
        self.nro_viaje=nro_viaje
        self.monto=monto
        print('Se ejecuto bien')
    
    def eliminarReserva(nro_reserva,lista_reserva):
        for reserva in lista_reserva:
            if reserva.nro_reserva==nro_reserva:
                lista_reserva.pop(reserva)
                print('Se ha eliminado la reserva nro {}'.format(reserva.nro_reserva))

    def buscarPasajero(self, nro_reserva, lista_reserva):
        for reserva in lista_reserva:
            if reserva.nro_reserva == nro_reserva:
                return reserva.DNI_cliente

    #Pide que el nro de reserva sea un numérico de 4 dígitos
    @staticmethod
    def check_nro_reserva(nro_reserva):
        while(nro_reserva.isnumeric()!=True or len(nro_reserva)!=4):
            nro_reserva=input('Error, el nro. de factura tiene que ser un numero de 4 digitos. Ingrese nuevamente:    ')
        return nro_reserva
    
    #Verifica que el DNI  sea de un pasajero existente
    @staticmethod
    def check_cliente(DNI_pasajero,lista_pasajero):
        while(True):
            for pasajero in lista_pasajero:
                if pasajero.DNI==DNI_pasajero:
                    return DNI_pasajero    
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
            for viaje in lista_viaje:
                if viaje.nro_viaje==nro_viaje:
                    return nro_viaje
            nro_viaje=input('Error, el viaje ingresado no corresponde con uno existente. Ingrese nuevamente:    ') 
    
    #Chequea que el monto ingresado en la reserva sea el correspondiente
    @staticmethod
    def check_monto(monto,nro_viaje,lista_viaje,lista_vuelo):
        for viaje in lista_viaje:
            if viaje.nro_viaje==nro_viaje:
                for vuelo in lista_vuelo:
                    if viaje.nro_vuelo==vuelo.nro_vuelo:
                        while(True):
                            if vuelo.monto==monto:
                                return monto
                            else:
                                monto=input('Monto incorrecto, ingrese nuevamente su monto:    ')

    
        
