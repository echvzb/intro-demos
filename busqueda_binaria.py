def busqueda_binaria(x=25):
  min = 0
  max = x

  while(True):

    y = (max + min)/2

    dif = x - y * y

    if dif < 0:
      dif *= -1

    if dif <= 0.001:
      return y
    
    if y * y > x:
      max = y
    else:
      min = y
