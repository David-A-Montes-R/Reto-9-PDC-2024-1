#De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).
def vueltas(*args):
    precio_pan= P*300
    precio_leche=M*3300
    precio_huevos= H*350
    return B - precio_pan - precio_leche - precio_huevos

def x_elevado_n(*args):
    b=be
    c=ce
    n=ene
    if b==0 and n==0:
        return "La potencia de 0 elevado a la 0 es indeterminada (aunque dependiendo del contexto puede considerarse como 1)"
    if n==0 and not(b==0):
        return "1.0"
    else:
        for n in range(0,n-1):
            b=b*c
        return b

def factorial_casero(*args):
    n=N
    m=n
    if n==0:
        return 1
    elif (n>0):
        while(n>1):
            n=n-1
            m=m*n
    return m
if __name__=="__main__":
    P=int(input("introduzca la cantidad de panes que toca comprar:"))
    M=int(input("introduzca la cantidad de bolsas de leche que toca comprar"))
    H=int(input("introduzca la cantidad de huevos que toca comprar"))
    B=int(input("introduzca la cantidad de dinero que le dio su querida mamá para ir a hacer la compra:"))
    vueltas_o_deuda= vueltas(P,M,H,B)
    if (vueltas_o_deuda >= 0):
        print("La cantidad de vueltas que le deben entregar es:", vueltas_o_deuda)
    else:
        print("Usted debe:",-1*(vueltas_o_deuda))

# número x elevado a n
be=float(input("Introduzca la base:"))
ce:float=be
ene=int(input("introduzca el exponente:"))
x=x_elevado_n(be,ce,ene)
print("el valor de",be,"elevado a la potencia de",ene,"es:")
print(x)

#factorial casero con while
N=int(input("introduzca un numero n, para conocer su factorial n!:"))
n=n
f=factorial_casero(n)
if n>=0:
    print("el factorial del número",N,"es:",f)
else:
    print("no es posible calcular el factorial de un número negativo")