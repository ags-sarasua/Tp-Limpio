def actualizar(lista, input_principal, atributo_principal, atributo_a_buscar, nuevo_input):
    for objeto in lista:
        if getattr(objeto,atributo_principal)==input_principal:
            setattr(objeto,atributo_a_buscar,nuevo_input)
            return True
    return False

