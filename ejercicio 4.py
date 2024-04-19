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