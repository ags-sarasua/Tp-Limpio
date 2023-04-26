
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
        
    def agregarInicio(self,nodo:Nodo):
        if(self.len==0):
            self.head=nodo
        else:
            nodo.prox=self.head #El puntero tiene toda la data del proximo
            self.head=nodo
        self.len+=1
        
    def __str__(self):
        nodo=self.head
        cadena=''
        if(self.len==0):
            return 'La lista es vacia'
        else:
            while(nodo!=None):
                cadena+=str(nodo.dato)+'\t'
                nodo=nodo.prox
            return cadena    
    
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
        
    def pop(self,pos=None):
        
        if self.head is None:
            return None
        nodo=Nodo()
        nodo=self.head
        if self.head is None:
            return None
        if pos==0:
            self.head=nodo.prox
            nodo=None
        elif pos==None:
            final=self.len-2  #ultimo nodo
            for i in range(final):
                nodo=nodo.prox
            nodo.prox=None
        else:
            for i in  range(pos-1):
                nodo=nodo.prox
            nodo.prox=nodo.prox.prox
    
    def buscar(self,first_attribute=None):
        nodo=Nodo()
        nodo=self.head
        contador=0
        posicion=None
        while(nodo.prox!='None'):
            if nodo.dato[0]==first_attribute:
                posicion=contador
            contador+=1
            nodo=nodo.prox
        return posicion

if __name__=='__main__':
    lista=Lista()
    nodo1=Nodo(12)
    lista.agregarInicio(nodo1)
    nodo2=Nodo(21)
    lista.append(nodo2)
    print(lista.buscar(0))
    #print(lista)
    