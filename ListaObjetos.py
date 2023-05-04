import Clases
import datetime
from listasenlazadas import *

#Este archivo tiene instancias de objetos por defecto

lista_persona=Lista()


p1= Clases.persona("12345678", "Ana", "Fangio", "Femenino", datetime.date(1988, 4, 15), "España","ana@gmail.com","1111111111")
p2= Clases.persona("23456789", "Juan Bautista", "Alberdi", "Masculino", datetime.date(1995, 6, 27), "Argentina","juan@gmail.com","1234567890")
p3= Clases.persona("34567890", "Luisa", "Risso", "Femenino", datetime.date(1982, 8, 2), "México","luisa@gmail.com","2345678901")
p4= Clases.persona("45678901", "Pedro", "Abascal", "Masculino", datetime.date(1998, 10, 11), "Francia","pedro@gmail.com","3456789012")
p5= Clases.persona("56789012", "Lucía", "Nagatomo", "Femenino", datetime.date(1975, 12, 4), "Japón","lucia@gmail.com","4567890123")
p6 = Clases.persona("67899123", "Lucía", "Fernández", "Femenino", datetime.date(1993,3,25), "Brasil","lucia2@gmail.com","567801234")
p7= Clases.persona("67890123", "Sofía", "Venegas", "Femenino", datetime.date(1986, 2, 20), "Brasil","sofia@gmail.com","6789012345")
p8= Clases.persona("78901234", "Javier", "Ielim", "Masculino", datetime.date(1992, 7, 8), "Rusia","javier12@gmail.com","7890123456")
p9= Clases.persona("89012345", "Carla", "Yema", "Femenino", datetime.date(1978, 9, 18), "Canadá","carla@gamil.com","8901234567")
p10= Clases.persona("90123456", "Pablo", "Leuco", "Masculino", datetime.date(1980, 5, 29), "Australia","pablo@gmail.com","9012345678")

lista_persona.append(Nodo(p1))
lista_persona.append(Nodo(p2))
lista_persona.append(Nodo(p3))
lista_persona.append(Nodo(p4))
lista_persona.append(Nodo(p5))
lista_persona.append(Nodo(p6))
lista_persona.append(Nodo(p7))
lista_persona.append(Nodo(p8))
lista_persona.append(Nodo(p9))
lista_persona.append(Nodo(p10))

#empleado
lista_empleado=[]

e1=Clases.empleado('12775678', 'Juan', 'Perez', 'Masculino', datetime.date(1990, 5, 3).strftime('%d/%m/%Y'), 'Argentina', '1234', 'Administrativo')
e2=Clases.empleado('87611321', 'María', 'Gomez', 'Femenino', datetime.date(1995, 2, 15).strftime('%d/%m/%Y'), 'Argentina', '5678', 'Piloto')
e3=Clases.empleado('23422789', 'Pedro', 'Rodriguez', 'Masculino', datetime.date(1985, 11, 20).strftime('%d/%m/%Y'), 'España', '9012', 'Tecnico')
e4=Clases.empleado('98733432', 'Ana', 'Gonzalez', 'Femenino', datetime.date(1992, 7, 7).strftime('%d/%m/%Y'), 'México', '3456', 'Administrativo')
e5=Clases.empleado('34545890', 'Miguel', 'Fernández', 'Masculino', datetime.date(1980, 3, 12).strftime('%d/%m/%Y'), 'Argentina', '7890', 'Tecnico')
e6=Clases.empleado('01255567', 'Lucia',  'Martinez', 'Femenino', datetime.date(1998, 8, 18).strftime('%d/%m/%Y'), 'Argentina', '2345', 'Piloto')
e7=Clases.empleado('78966234', 'Gustavo', 'Suarez', 'Masculino', datetime.date(1987, 9, 25).strftime('%d/%m/%Y'), 'Uruguay', '3456', 'Administrativo')
e8=Clases.empleado('45677901', 'Julia', 'Fernández', 'Femenino', datetime.date(1991, 1, 1).strftime('%d/%m/%Y'), 'Argentina', '1235', 'Piloto')
e9=Clases.empleado('89088345', 'Andrés', 'Romero', 'Masculino', datetime.date(1982, 6, 10).strftime('%d/%m/%Y'), 'Colombia', '5679', 'Tecnico')
e10=Clases.empleado('54399109', 'Liliana', 'Díaz', 'Femenino', datetime.date(1993, 12, 24).strftime('%d/%m/%Y'), 'Argentina', '9013', 'Administrativo')

lista_empleado.append(e1)
lista_empleado.append(e2)
lista_empleado.append(e3)
lista_empleado.append(e4)
lista_empleado.append(e5)
lista_empleado.append(e6)
lista_empleado.append(e7)
lista_empleado.append(e8)
lista_empleado.append(e9)
lista_empleado.append(e10)

#avion

lista_avion=[]

avion1 = Clases.avion('1234567890', "Boeing 747", "2022-01-01", "Fuera de servicio")
avion2 = Clases.avion('2345678901', "Airbus A320", "2020-06-15", "En servicio")
avion3 = Clases.avion('3456789012', "Boeing 787", "2021-09-30", "Fuera de servicio")
avion4 = Clases.avion('4567890123', "Embraer E195", "2019-11-10", "En servicio")
avion5 = Clases.avion('5678901234', "Airbus A380", "2018-05-01", "Fuera de servicio")
avion6 = Clases.avion('6789012345', "Boeing 737", "2017-08-20", "En servicio")
avion7 = Clases.avion('7890123456', "Bombardier CS100", "2020-01-20", "Fuera de servicio")
avion8 = Clases.avion('8901234567', "Airbus A350", "2022-03-05","En servicio")
avion9 = Clases.avion('9012345678', "Boeing 777", "2016-12-31","Fuera de servicio")
avion10 = Clases.avion('1234567891', "Airbus A330", "2019-02-14","En servicio")

lista_avion.append(avion1)
lista_avion.append(avion2)
lista_avion.append(avion3)
lista_avion.append(avion4)
lista_avion.append(avion5)
lista_avion.append(avion6)
lista_avion.append(avion7)
lista_avion.append(avion8)
lista_avion.append(avion9)
lista_avion.append(avion10)

#vuelos
lista_vuelo=Lista()


vuelo1 = Clases.vuelo('1001',"JFK", "LAX",'5678' ,'1500')
vuelo2 = Clases.vuelo('1002',"SFO", "ORD", '2345','1800')
vuelo3 = Clases.vuelo('1003',"LHR", "CDG",'5678' ,'2200')
vuelo4 = Clases.vuelo('1004',"HND", "ICN",'5678' ,'1900')
vuelo5 = Clases.vuelo('1005',"PEK", "SYD",'2345' ,'2000')
vuelo6 = Clases.vuelo('1006',"DXB", "LHR",'1235' ,'2300')
vuelo7 = Clases.vuelo('1007',"ORD", "SFO",'2345' ,'2500')
vuelo8 = Clases.vuelo('1008',"CDG", "LHR",'1235' ,'2700')
vuelo9 = Clases.vuelo('1009',"ICN", "HND",'1235','1800')
vuelo10 = Clases.vuelo('1010',"EZE", "BDX",'1235','3000')

lista_vuelo.append(Nodo(vuelo1))
lista_vuelo.append(Nodo(vuelo2))
lista_vuelo.append(Nodo(vuelo3))
lista_vuelo.append(Nodo(vuelo4))
lista_vuelo.append(Nodo(vuelo5))
lista_vuelo.append(Nodo(vuelo6))
lista_vuelo.append(Nodo(vuelo7))
lista_vuelo.append(Nodo(vuelo8))
lista_vuelo.append(Nodo(vuelo9))
lista_vuelo.append(Nodo(vuelo10))

#viajes
lista_viaje=Lista()

viaje1=Clases.viaje("1464", "1001", "2345678901", datetime.date(2022, 5, 23))
viaje2=Clases.viaje("2746", "1002", "4567890123", datetime.date(2022, 5, 23))
viaje3=Clases.viaje("3578", "1003", "2345678901", datetime.date(2023, 3, 5))
viaje4=Clases.viaje("4390", "1004", "8901234567", datetime.date(2023, 4, 17))
viaje5=Clases.viaje("4545", "1005", "6789012345", datetime.date(2023, 5, 9))
viaje6=Clases.viaje("2368", "1006", "2345678901", datetime.date(2024, 12, 11))
viaje7=Clases.viaje("2356", "1007", "4567890123", datetime.date(2023, 5, 13))
viaje8=Clases.viaje("8765", "1008", "2345678901", datetime.date(2023, 8, 15))
viaje9=Clases.viaje("3568", "1009", "1234567891", datetime.date(2023, 2, 17))
viaje10=Clases.viaje("0965","1010", "2345678901", datetime.date(2023, 5, 19))

lista_viaje.append(Nodo(viaje1))
lista_viaje.append(Nodo(viaje2))
lista_viaje.append(Nodo(viaje3))
lista_viaje.append(Nodo(viaje4))
lista_viaje.append(Nodo(viaje5))
lista_viaje.append(Nodo(viaje6))
lista_viaje.append(Nodo(viaje7))
lista_viaje.append(Nodo(viaje8))
lista_viaje.append(Nodo(viaje9))
lista_viaje.append(Nodo(viaje10))

#reserva
lista_reserva=Lista()

reserva1=Clases.reserva("1001", "12345678", "1234", "1464" , "1500")
reserva2=Clases.reserva("1002", "23456789", "3456", "2746" , "1800")
reserva3=Clases.reserva("1003", "34567890", "1234", "3578" , "2200")
reserva4=Clases.reserva("1004", "45678901", "3456", "4390" , "1900")
reserva5=Clases.reserva("1005", "56789012", "3456", "4545" , "2000")
reserva6=Clases.reserva("1006", "67890123", "1234", "2368" , "2300")
reserva7=Clases.reserva("1007", "78901234", "3456", "2356" , "2500")
reserva8=Clases.reserva("1008", "89012345", "9013", "8765" , "2700")
reserva9=Clases.reserva("1009", "90123456", "1234", "3568" , "1800")
reserva10=Clases.reserva("1010", "67899123", "9013", "0965" , "3000")

Clases.viaje.agregar_pasajero( "1464", "12345678",lista_viaje)
Clases.viaje.agregar_pasajero( "2746", "23456789",lista_viaje)
Clases.viaje.agregar_pasajero( "3578", "34567890",lista_viaje)
Clases.viaje.agregar_pasajero( "4390", "45678901",lista_viaje)
Clases.viaje.agregar_pasajero( "4545", "56789012",lista_viaje)
Clases.viaje.agregar_pasajero( "2368", "67890123",lista_viaje)
Clases.viaje.agregar_pasajero( "2356", "78901234",lista_viaje)
Clases.viaje.agregar_pasajero( "8765", "89012345",lista_viaje)
Clases.viaje.agregar_pasajero( "3568", "90123456",lista_viaje)
Clases.viaje.agregar_pasajero( "0965", "67899123",lista_viaje)

lista_reserva.append(Nodo(reserva1))
lista_reserva.append(Nodo(reserva2))
lista_reserva.append(Nodo(reserva3))
lista_reserva.append(Nodo(reserva4))
lista_reserva.append(Nodo(reserva5))
lista_reserva.append(Nodo(reserva6))
lista_reserva.append(Nodo(reserva7))
lista_reserva.append(Nodo(reserva8))
lista_reserva.append(Nodo(reserva9))
lista_reserva.append(Nodo(reserva10))





