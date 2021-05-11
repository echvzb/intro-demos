# Función metodo babilonico

def metodo_babilonico(x=25):
  y = int(x / 2)

  # Ciclo hasta encontrar la raíz cuadrada de x
  while(True):
    
    # Declaracion de la diferencia real de x y y al cuadrado
    dif = y * y - x

    if dif < 0:
      # Conversion de la diferencia real a absoluta
      dif *= -1

    if dif <= 0.001:
      #  Se encuentra la raíz cuadrada y se retorna el resultado (y)
      return y
    else:
      # De no ser verdadera la condional. Reemplazo de y para volver a repetir el ciclo
       y = (y + (x / y)) / 2

