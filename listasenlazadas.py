
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
    """   
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
    """
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
        
    def pop(self,input_principal,atributo_principal):
        nodo=Nodo()
        nodo=self.head
        for i in range(self.len-1):
            if i==0 and getattr(nodo.dato,atributo_principal)==input_principal:
                self.head=nodo.prox
                self.len-=1
                return True
            elif getattr(nodo.prox.dato,atributo_principal)==input_principal:
                nodo.prox=nodo.prox.prox
                print('AAA')
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
            
        '''
        while(nodo.prox!=None):
            if getattr(nodo.dato,atributo_principal)==input_principal:
                posicion=contador
                print('funciona')
                return posicion
            contador+=1
            nodo=nodo.prox
        '''
    
###
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
        
dog1 = Dog("Fido", "Golden Retriever", 4)
dog2 = Dog("Buddy", "Labrador Retriever", 6)
dog3 = Dog("Max", "German Shepherd", 3)

dog_list = Lista()
dog_list.append(Nodo(dog1))
dog_list.append(Nodo(dog2))
dog_list.append(Nodo(dog3))

###

if __name__=='__main__':
    lista=Lista()
    nodo1=Nodo(12)
    nodo2=Nodo(21)
    lista.append(nodo2)
    a=dog_list.pop("Max","name")
    if a==True:
        print('Banco') 
    
    print(dog_list.buscar("Max","name","age"))
    #print(lista)
    print(dog_list)