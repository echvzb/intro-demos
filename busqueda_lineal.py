# Funcion Busqueda Lineal de Raiz Cuadrada Exacta	
# Entrada: valor por defecto de x igual a 25	
def busqueda_lineal_raiz_cuadrada_exacta(x = 25):	
  # Declaración de y igual a 0	
  y = 0	
  # Ciclo infinito hasta encontrar la raíz cuadrada	
  while True:	
    # Si y * y es igual a x, encontramos la raiz cuadrada de y	
    if y * y == x:	
      return y	
    	
    # De ser falsa la anterior proposicion, añadimos una unidad a y	
    y += 1