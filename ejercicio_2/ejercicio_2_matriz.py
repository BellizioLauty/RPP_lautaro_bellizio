#funcion para calcular la media geometrica de filas o columnas de una matriz cuadrada
def es_cuadrada(matriz):
    '''Valida si la matriz es cuadrada.'''
    n = len(matriz)
    for fila in matriz:
        if len(fila) != n:
            return False
    return True


def suma_diagonales_base(matriz):
    '''Calcula la suma de la diagonal principal y secundaria de una matriz cuadrada.'''
    n = len(matriz)
    suma_principal = 0
    suma_secundaria = 0
    for i in range(n):
        suma_principal += matriz[i][i]
        suma_secundaria += matriz[i][n - i - 1]
    return suma_principal, suma_secundaria

def media_geometrica(matriz, tipo='fila'):
    '''Calcula la media geométrica de filas o columnas de una matriz cuadrada.'''
    if not es_cuadrada(matriz):
        return 'La matriz no es cuadrada.'
    
    n = len(matriz)
    resultados = []
    
    # Calcular la media geométrica para cada fila o columna
    if tipo == 'fila':
        for i in range(n):
            producto = 1
            for j in range(n):
                producto *= matriz[i][j]
            media_geo = producto ** (1/n)
            resultados.append(media_geo)
    elif tipo == 'columna':
        for j in range(n):
            producto = 1
            for i in range(n):
                producto *= matriz[i][j]
            media_geo = producto ** (1/n)
            resultados.append(media_geo)
    else:
        return 'El tipo debe ser "fila" o "columna".'
    
    return resultados

def suma_diagonales(matriz):
    '''Calcula la suma de las diagonales principal y secundaria.'''
    if not es_cuadrada(matriz):
        return 'La matriz no es cuadrada.'
    
    suma_principal, suma_secundaria = suma_diagonales_base(matriz)
    return suma_principal + suma_secundaria


def transpuesta(matriz):
    '''Devuelve la transpuesta de una matriz cuadrada.'''
    if not es_cuadrada(matriz):
        return 'La matriz no es cuadrada.'
    
    n = len(matriz)
    matriz_transpuesta = []
    for j in range(n):
        nueva_fila = []
        for i in range(n):
            nueva_fila.append(matriz[i][j])
        matriz_transpuesta.append(nueva_fila)
    
    return matriz_transpuesta

def suma_diagonales_opcional(matriz, diagonal='ambas'):
    '''Calcula la suma de las diagonales según el parámetro especificado.'''
    if not es_cuadrada(matriz):
        return 'La matriz no es cuadrada.'
    
    suma_principal, suma_secundaria = suma_diagonales_base(matriz)
    
    if diagonal == 'principal':
        return suma_principal
    elif diagonal == 'secundaria':
        return suma_secundaria
    elif diagonal == 'ambas':
        return suma_principal + suma_secundaria
    else:
        return 'El parámetro diagonal debe ser "principal", "secundaria" o "ambas".'

def main():
    # Ejemplo de matriz
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    # 1. Media geométrica
    print('Media geométrica de filas:', media_geometrica(matriz, 'fila'))
    print('Media geométrica de columnas:', media_geometrica(matriz, 'columna'))
    
    # 2. Suma de diagonales
    print('Suma de ambas diagonales:', suma_diagonales(matriz))
    
    # 3. Transpuesta de la matriz
    print('Matriz transpuesta:')
    transpuesta_matriz = transpuesta(matriz)
    for fila in transpuesta_matriz:
        print(fila)
    
    # 4. Suma de diagonales con opción
    print('Suma de la diagonal principal:', suma_diagonales_opcional(matriz, 'principal'))
    print('Suma de la diagonal secundaria:', suma_diagonales_opcional(matriz, 'secundaria'))
    print('Suma de ambas diagonales:', suma_diagonales_opcional(matriz, 'ambas'))

#ejecutar main
main()