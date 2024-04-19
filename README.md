# Reto 9 PDC Unal 2024-1

<div align='center'>
<figure> <img src="https://i.postimg.cc/HkMddSNw/error-418.png" alt="" width="300" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

## por: David Alejandro Montes Rodríguez

# 1. De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.

Para este punto decidí escoger una función de cada reto, es decir, una función del reto 6, otra del 7 y otra del 8, dado que cada ejercicio debe tener un programa propio, estas 3 funciones reescritas como lambdas se ejecutaran cada una después de la otra.

```python
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
```
# 2. De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).

Para este punto, al igual que en el punto anterior, escogí una función de cada reto anterior, sin embargo, en este punto son funciones diferentes. Aquí sucedio algo curioso y es que si bien, la idea de usar funciones con ``*args`` es que estas puedan hacer procesos con variables que no están definidas (lo cual sirve para el ejemplo de la clase de una sumatoria de 1 a 5 números), en las funciones que escogí para este punto, todas las variables están definidas, por lo cual el programa al ejecutarse arrojaba un error que se soluciono definiendo las variables dentro de las funciones a través de otras variables declaradas usando letras mayúsculas (lo cual tras consultar en el PEP 8 no parece estar uy mal, pero no está estrictamente bien).

```python
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
```

# 3. Escriba una función recursiva para calcular la operación de la potencia.

Aquí sucedio otro fenómeno curioso, y es que la función no operaba al colocar el valor ``float`` ``x``, en la operación de la multiplicación antes de la función. Se define un caso base, que sería donde ``x`` y ``n`` valen 0, en dónde el programa retorna la misma respuesta que en el reto 8, pero como este caso ocurre muy rara vez, su "caso base real", se da cuando ``n`` vale 0, por lo cual se detiene la recursividad, y la función deja de procesarse, retornando el último valor adquirido, el cual es la potencia real de ``x^n``.

```python
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
```

# 4. Utilice la siguiente plantilla de code para contar el tiempo:
```python import time

start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
end_time = time.time()

timer = end_time - start_time
print(timer)
```
# Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa. Importante: Revisar este hilo.

El código está bastante bien comentado, por lo cual no detallare mucho aquí.

```python
#Utilice la siguiente plantilla de code para contar el tiempo:
#Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa.


#Al final use lo que decía en stackoveflow de timeit, porque time no colaboraba mucho
import timeit
num = int(input("Ingrese numero: "))
def fibo(n : int )-> int:
  i : int = 1
  # caso base
  n1 : int = 0
  n2 : int = 1
  while(i <= n):
    # Condicion
    sumFibo = n1 + n2
    print(sumFibo)
    # Actualizacion
    n1 = n2
    n2 = sumFibo
    i += 1
  return sumFibo

def fiboRecursivo(n : int )-> int:
  if n <=1:
    # caso base
    return 1
  else:
    # condicion
    return fiboRecursivo(n-1)+fiboRecursivo(n-2)  

if __name__ == "__main__":
  start_time = timeit.default_timer()
  serieFibo = fibo(num)
  print("La serie de Fibonacci hasta " + str(num) + " es " + str(serieFibo))
  T1=(timeit.default_timer() - start_time)
  print("la función con iteración tarda:",T1)

  start_time = timeit.default_timer()
  serieFibo_R = fiboRecursivo(num)
  print("La serie de Fibonacci hasta " + str(num) + " es " + str(serieFibo_R))
  T2=(timeit.default_timer() - start_time)
  print("la función con recursividad tarda:",T2)

  print("la diferencia de tiempo de ejecución entre ambas funciones es de:",abs(T1-T2))

#se puede entender que una diferencia significativa ocurre cuando la diferencia entre ambas medidas es perceptible
# esto ocurre con el factorial de 35, cuando la diferencia de tiempo de ejecución supera 1 segundo
#nota chistosa: probé meter un 50 y ya lleva 3 minutos y medio ejecutandose el programa y aún no se detiene
#conclusión: usar la función recursiva funciona mejor para operaciones a escalas muy pequeñas
```
# 5. Crear cuenta en stackoverflow y adjuntar imagen en el repo

A continuación dejo el pantallazo respectivo:

[![perfil-Stackoverflow.png](https://i.postimg.cc/QtTMPSF3/perfil-Stackoverflow.png)](https://postimg.cc/LYmRgtkC)

# 6. Cosas de adultos....ir a linkedin y crear perfil....NO IMPORTA que estén iniciando, si tienen tiempo para redes poco útiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalón. Dejar enlace en el repo.

Aquí tuve la suerte de que una tarea del cole fue hacerse un perfil de LinkedIn, así que solo le actualicé un poco los datos.

El enlace a mi perfil de LinkedIn es el siguiente: [www.linkedin.com/in/david-alejandro-montes-rodríguez-57a293247](www.linkedin.com/in/david-alejandro-montes-rodríguez-57a293247)