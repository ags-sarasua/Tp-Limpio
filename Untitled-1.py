
"""
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
"""

def actualizar(lista,input_principal, atributo_principal,atributo_a_buscar,nuevo_input):
    for objeto in lista:
        if objeto.atributo_principal==input_principal:
            #Todos los checks
            objeto.atributo_a_buscar==nuevo_input
    nodo=Nodo()
    nodo=self.head
    for i in range(self.len):
        if getattr(nodo.dato,atributo_principal)==input_principal:
            setattr(nodo.dato, atributo_a_buscar,nuevo_input)
            return True
        nodo=nodo.prox
    return False

#check mail
@staticmethod
def check_sintaxis_mail(mail):
    print('Aclaracion, el mail debe terminar en @gmail.com')
    while mail[-10:] !="@gmail.com" or len(mail)==10:
        mail=input('El mail fue ingresado incorrectamente')
    
@staticmethod    
def check_existencia_mail(mail,lista_persona):        
    while lista_persona.buscar(mail,"mail","mail"):
            mail=input('Existe un usuario con su mail, ingrese uno nuevo:   ')
            check_sintaxis_mail(mail)
            check_existencia_mail(mail,lista_persona)
            return mail
    return mail

#check telefono
@staticmethod
def check_sintaxis_telefono(telefono):
        while len(telefono)!=10 or telefono.isnumeric()==False:
            print('Error, el telefono debe ser un número de 10 dígitos.')
            telefono=input("Ingrese el telefono nuevamente: ")    
        return telefono
    
@staticmethod    
def check_existencia_telefono(telefono,lista_persona):        
    while lista_persona.buscar(telefono,"telefono","telefono"):
            telefono=input('Existe un usuario con su telefono, ingrese uno nuevo:   ')
            check_sintaxis_telefono(telefono)
            check_existencia_telefono(telefono,lista_persona)
            return telefono
    return telefono