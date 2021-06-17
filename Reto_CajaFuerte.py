class cajafuerte:
  def __init__ (self, matriz):
    self.matriz = matriz
    self.fila = 0
    self.columna = 0

  # Metodo para seguir el movimiento en cada casilla
  def movimiento (self):
    
    for fila in range (len (self.matriz)):
      for columna in range (len (self.matriz [0])):

        self.fila = fila
        self.columna = columna
        pasos = self.matriz [self.fila] [self.columna]
        trayecto = list ()

        while pasos != "F":

          trayecto.append ( self.matriz [self.fila] [self.columna] )

          if pasos [1] == "A":
            self.fila -= int (pasos [0])
            pasos = self.matriz [self.fila] [self.columna]
          elif pasos [1] == "B":
            self.fila += int (pasos [0])
            pasos = self.matriz [self.fila] [self.columna]
          elif pasos [1] == "D":
            self.columna += int (pasos [0])
            pasos = self.matriz [self.fila] [self.columna]
          else:
            self.columna -= int (pasos [0])
            pasos = self.matriz [self.fila] [self.columna]
        
        if len (trayecto) == ((len (self.matriz) * len (self.matriz [0])) - 1):
          #print (len (trayecto))
          #print (len (self.matriz) * len (self.matriz [0]))
          print (trayecto)
          print (self.matriz [fila] [columna])
          print ((fila, columna))
          break


          
        
        

