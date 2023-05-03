
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