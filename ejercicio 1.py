#De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.

#números con su respectivo cuadrado:
a:int=1
ga:int=6
go:int=7
po=1
if __name__=="__main__":
    print("números con su respectivo cuadrado: ")
    while (a<=100):
        cuadrado=(lambda a: a**2)(a)
        print("este es el número:",a," y su cuadrado es:",cuadrado)
        a=a+1
        
#potencias de 2 a la n:
n=int(input("introduzca el exponente n para saber su potencia de base 2:"))
p=(lambda n: 2**n)(n)
print("2 elevado a la potencia",n,"es:",p)
# suma de animales
nga=(int(input("introduzca el número de gallinas:")))
ngo=(int(input("introduzca el número de gallos:")))
npo=(int(input("introduzca el número de pollitos")))
t=(lambda ga,go,po,nga,ngo,npo: (ga*nga)+(go*ngo)+(po*npo) )(ga,go,po,nga,ngo,npo)
print("la cantidad de carne que tiene son:",t,"kilos de carne","con",nga,"gallinas",ngo,"gallos y",npo,"pollitos")         