#Escriba una función recursiva para calcular la operación de la potencia.

# se entiende que es una potencia de tipo x^n donde x es real y n es entero

def potencia_recursiva(x:float,n:int)-> float:
    x*x
    if n==0 and x==0:
        return "la potencia de 0 elevado 0 es indeterminada(según el contexto)"
    elif n==0:
        return 1
    else:
        n=n-1
        return potencia_recursiva(x,n)*x

if __name__=="__main__":
    x= float(input("introduzca una base x:"))
    n= int(input("introduzca un exponente n:"))
    pr=potencia_recursiva(x,n)
    print("la potencia de base",x,"y exponente",n,"es:",pr)