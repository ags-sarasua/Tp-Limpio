from Clases import *
from ListaObjetos import *
import matplotlib.pyplot as mlp



class Nodo():
    def __init__(self,dato=None,prox=None):
        self.dato=dato
        self.prox=prox
    def __str__(self) -> str:
        return str(self.dato) # Especificas como queres que se printee
    
class Lista():
    def __init__(self):
        self.head=None
        self.len=0
    def __str__(self):
        nodo = Nodo()
        nodo=self.head
        lista = []
        while nodo is not None:
            lista.append(str(nodo.dato.__dict__))
            nodo = nodo.prox
        return "\n".join(lista)
    
    def append(self,nodo:Nodo):
        if(self.len==0):
            self.head=nodo
        else:
            nodomov=Nodo()
            nodomov=self.head
            while(nodomov.prox!=None):
                nodomov=nodomov.prox
            nodomov.prox=nodo   #muy bueno
        self.len+=1
        
    def pop(self,input_principal,atributo_principal):  #INPUT PRINCIPAL: VARIABLE QUE INGRESA EL USUARIO   ATRIBUTO_PRINCIPAL "DNI"
        nodo=Nodo()
        nodo=self.head
        for i in range(self.len-1):
            if i==0 and getattr(nodo.dato,atributo_principal)==input_principal:
                self.head=nodo.prox
                self.len-=1
                return True
            elif getattr(nodo.prox.dato,atributo_principal)==input_principal:
                nodo.prox=nodo.prox.prox
                self.len-=1
                return True
            nodo=nodo.prox
        return False
    
    def buscar(self,input_principal, atributo_principal,atributo_a_buscar):
        nodo=Nodo()
        nodo=self.head
        for i in range(self.len):
            if getattr(nodo.dato,atributo_principal)==input_principal:
                return getattr(nodo.dato,atributo_a_buscar)
            nodo=nodo.prox
        return False

    def actualizar_le(self,input_principal, atributo_principal,atributo_a_buscar,nuevo_input):
        nodo=Nodo()
        nodo=self.head
        for i in range(self.len):
            
            if getattr(nodo.dato,atributo_principal)==input_principal:
                setattr(nodo.dato, atributo_a_buscar,nuevo_input)
        
                return True
            nodo=nodo.prox
        
        return False

    def lista_enlazada_txt(lista, archivo):
    # abrir el archivo para escritura
        with open(archivo, 'w') as archivo_salida:
            # recorrer la lista enlazada y escribir cada elemento en el archivo
            nodo_actual = lista.head
            while nodo_actual:
                archivo_salida.write(str(nodo_actual.dato.__dict__))
                nodo_actual = nodo_actual.prox
                #if nodo_actual:
                    #archivo_salida.write('\n')


    def crear_lista_enlazada_de_aviones_desde_diccionario(lista,clase,archivo):
        # abrir el archivo para lectura
        with open(archivo, 'r') as archivo_entrada:
            # recorrer cada línea del archivo
            for linea in archivo_entrada:
                # convertir la línea en un diccionario
                diccionario = eval(linea)
                # crear una instancia de la clase Avion a partir del diccionario
                avion = clase(**diccionario)
                # agregar el avión a la lista enlazada
                lista.append(avion)
        # retornar la lista enlazada
        return lista



