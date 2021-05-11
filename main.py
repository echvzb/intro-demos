def busqueda_binaria(x=25):
  min = 0
  max = x

  while(True):

    y = (max + min)/2

    dif = x - y * y

    if dif < 0:
      dif *= -1

    print(f'y = {y}, y * y = {y * y}, min = {min}, max = {max}')
    if dif <= 0.00001:
      return y
    
    if y * y > x:
      max = y
    else:
      min = y

busqueda_binaria(256)