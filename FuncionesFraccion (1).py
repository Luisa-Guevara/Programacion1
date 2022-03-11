def M_C_D(p,q):
    """Función que permite hallar el Máximo Común Divisor entre dos números, utilizando el algoritmo de Euclides"""
    if p<q:
        p,q=q,p
    elif q==0:
        return "Error, no se puede dividir cuando el denominador es 0"
    resto= p%q
    if resto==0:
        return p//q
    while resto!=0:
        p=q
        q=resto
        resto=p%q
        return q

def simplificar(p,q):
    """Función que permite convertir dos números enteros a fracción y a la vez
    hallar su simplificacióm, usando la funcion de (M_C_D), la cuál fue definida anteriormente"""
    if q==0:
        return "Error, no se puede dividir cuando el denominador es 0"
    numerador= int(p/M_C_D(p,q))
    denominador= int(q/M_C_D(p,q))
    if denominador==1:
        return numerador
    elif numerador==denominador:
        return 1
    return print(numerador,"/",denominador)   

def sumaFraccion(n1,d1,n2,d2):
    """Función que permite sumar dos fracciones, utilizando el método de carita feliz"""
    if d1==0 or d2==0: 
        return "Error, no se puede dividir cuando el denominador es 0"
    elif d1*d2==1:
        return (n1*d2)+(d1*n2)
    return print((n1*d2)+(d1*n2),"/",(d1*d2))

def restaFraccion(n1,d1,n2,d2):
    """Función que permite restar dos fracciones, utilizando el método de carita feliz"""
    if d1==0 or d2==0:
        return "Error, no se puede dividir cuando el denominador es 0"
    elif d1*d2==1:
        return (n1*d2)-(d1*n2)
    return print(((n1*d2)-(d1*n2)),"/",(d1*d2))

def multiplicacionFraccion(n1,d1,n2,d2):
    """Función que permite multiplicar dos fracciones"""
    if d1==0 or d2==0: 
        return "Error, no se puede dividir cuando el denominador es 0"
    elif d1*d2==1:
        return (n1*n2)
    return print((n1*n2),"/",(d1*d2))

def divisionFraccion(n1,d1,n2,d2):
    """Función que permite dividir dos fracciones"""
    if d1==0 or d2==0 or d1*n2==0: 
        return "Error, no se puede dividir cuando el denominador es 0"
    elif d1*n2==1:
        return (n1*d2)
    return print((n1*d2),"/",(d1*n2))