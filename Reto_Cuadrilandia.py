import copy
class cuadrilandia:

  def __init__(self, matriz) -> None:

    self.matriz = matriz
    self.matriz_copia = copy.deepcopy (matriz)
    self.size = len (matriz) - 1
    self.fila_inicial = 0
    self.cuadro = 0
    print (id (self))

  def laterales_90 (self):

    columna_lateral_subida = self.fila_inicial
    columna_lateral_bajada = self.size

    fila_siguiente = self.fila_inicial
    fila_actual_subida = fila_siguiente 
    fila_actual_bajada = fila_siguiente
 

    while fila_siguiente <= self.size:

      dato_matriz_subida = self.matriz [fila_siguiente] [columna_lateral_subida]
      dato_matriz_bajada = self.matriz [fila_siguiente] [columna_lateral_bajada]

      mov = 1 + self.fila_inicial

      while mov < self.size + 1:

        if fila_actual_subida - 1 >= self.fila_inicial:
          fila_actual_subida -= 1
        else:
          columna_lateral_subida += 1 

        if fila_actual_bajada + 1 <= self.size:
          fila_actual_bajada += 1
        else:
          columna_lateral_bajada -= 1
        mov += 1

      self.matriz_copia [fila_actual_bajada] [columna_lateral_bajada] =  dato_matriz_bajada
      self.matriz_copia [fila_actual_subida] [columna_lateral_subida] =  dato_matriz_subida

      fila_siguiente += 1
      fila_actual_bajada = fila_siguiente
      fila_actual_subida = fila_siguiente
      columna_lateral_subida = self.fila_inicial
      columna_lateral_bajada = self.size 
    
    self.frontales_90 ()  
    self.cuadro += 1
    if self.cuadro == (len (self.matriz) //2):
      return
      
    self.size -= 1
    self.fila_inicial += 1
    self.laterales_90 ()
       
  def frontales_90 (self):

    if (self.fila_inicial +1) < self.size:

      for column in range (self.fila_inicial + 1, self.size):
        fila = self.fila_inicial
        fila_final = self.size

        dato_arriba = self.matriz [fila] [column]
        dato_abajo = self.matriz [fila_final] [column]

        column_arriba = column
        column_abajo = column

        mov = 1 + self.fila_inicial
        while mov < self.size + 1:

          if column_arriba + 1 <= self.size:
            column_arriba += 1
          else:
            fila += 1

          if column_abajo - 1 >= self.fila_inicial:
            column_abajo -= 1
          else:
           fila_final -= 1
          mov += 1

        self.matriz_copia [fila] [column_arriba] = dato_arriba
        self.matriz_copia [fila_final] [column_abajo] = dato_abajo
    return
    
  def laterales_45 (self):

    columna_lateral_subida = self.fila_inicial
    columna_lateral_bajada = self.size

    fila_siguiente = self.fila_inicial
    fila_actual_subida = fila_siguiente 
    fila_actual_bajada = fila_siguiente
 

    while fila_siguiente <= self.size:

      dato_matriz_subida = self.matriz [fila_siguiente] [columna_lateral_subida]
      dato_matriz_bajada = self.matriz [fila_siguiente] [columna_lateral_bajada]

      mov = 1 + self.fila_inicial

      while mov < ((self.size ) // 2)+1:

          if fila_actual_subida - 1 >= self.fila_inicial:
              fila_actual_subida -= 1
          else:
              columna_lateral_subida += 1 

          if fila_actual_bajada + 1 <= self.size:
              fila_actual_bajada += 1
          else:
              columna_lateral_bajada -= 1

          mov += 1

      self.matriz_copia [fila_actual_bajada] [columna_lateral_bajada] =  dato_matriz_bajada
      self.matriz_copia [fila_actual_subida] [columna_lateral_subida] =  dato_matriz_subida

      fila_siguiente += 1
      fila_actual_bajada = fila_siguiente
      fila_actual_subida = fila_siguiente
      columna_lateral_bajada = self.size
      columna_lateral_subida = self.fila_inicial
      
    self.frontales_45 ()
    self.cuadro += 1
    if self.cuadro == (len (self.matriz) //2):
      return self.matriz_copia
    
    self.size -= 1
    self.fila_inicial += 1
    return self.laterales_45 ()
       
  def frontales_45 (self):

    if (self.fila_inicial +1) < self.size:
      for column in range (self.fila_inicial + 1, self.size):

        fila = self.fila_inicial
        fila_final = self.size

        dato_arriba = self.matriz [fila] [column]
        dato_abajo = self.matriz [fila_final] [column]

        column_arriba = column
        column_abajo = column

        mov = 1 + self.fila_inicial
        while mov < ((self.size ) // 2) + 1:

          if column_arriba + 1 <= self.size:
            column_arriba += 1
          else:
            fila += 1

          if column_abajo - 1 >= self.fila_inicial:
            column_abajo -= 1
          else:
            fila_final -= 1

          mov += 1

        self.matriz_copia [fila] [column_arriba] = dato_arriba
        self.matriz_copia [fila_final] [column_abajo] = dato_abajo
    return 

matriz = [
  [   -62,      -17,    113,    -91,    116,    -115,   ],
  [   127,      63,     96,     -37,    88,     -71,    ],
  [   43,       -7,     -12,    -111,   73,     9,      ],
  [   56,       53,     -14,    -1,     86,     -91,    ],
  [   -46,      81,     -45,    -123,   -5,     123,    ],
  [   103,      59,     64,     -51,    -108,   19,     ]]


"""[
  [   43,       127,    -62,    -17,    113,    -91,    ],
  [   56,       -7,     63,     96,     -37,    116,    ],
  [   -46,      53,     -12,    -111,   88,     -115,   ],
  [   103,      81,     -14,    -1,     73,     -71,    ],
  [   59,       -45,    -123,   -5,     86,     9,      ],
  [   64,       -51,    -108,   19,     123,    -91,    ],
]"""
import numpy as np
# angulo = 45
# angulo = angulo //360
# if angulo // 90 > 0:
#    cuantos_90 = angulo // 90
#    angulo = angulo % 90
#    for i in range (cuantos_90):
#      matriz = cuadrilandia (matriz)
#      matriz.laterales_90 ()
#      matriz = matriz.matriz_copia
angulo = 45
if angulo // 45 > 0: 
  cuantos_45 = angulo // 45

  for i in range (cuantos_45):
    matriz = cuadrilandia (matriz).laterales_45 ()
    print (np.array (matriz))