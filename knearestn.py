import random 


# Pendiente de graficar: https://docs.bokeh.org/en/latest/docs/user_guide/plotting.html

# Generar puntos de grupos con un rango específico para que tengan una clasificación fija y punto a evaluar
def llenar_grupo(num_puntos):    
    grupo1 = []
    grupo2 = []
    for _ in range(num_puntos):
        punto = (random.randint(15, 30), random.randint(0, 15))
        grupo1.append(punto)

    for _ in range(num_puntos):
        punto = (random.randint(0, 15), random.randint(15, 30))
        grupo2.append(punto)

    return grupo1, grupo2

def dato_aleatorio():
    punto_nuevo = (random.randint(0, 30), random.randint(0, 30))
    return punto_nuevo

# Generar lista de distancias
def distancias_g(num_puntos, grupo1, grupo2, punto_nuevo):
    distancias_grupo1 = []
    distancias_grupo2 = []
    
    for i in range(num_puntos):
        distancia = ((punto_nuevo[0] - grupo1[i][0])**2 + (punto_nuevo[1] - grupo1[i][1])**2)**0.5
        distancias_grupo1.append(round(distancia,2))
    
    for i in range(num_puntos):
        distancia = ((punto_nuevo[0] - grupo2[i][0])**2 + (punto_nuevo[1] - grupo2[i][1])**2)**0.5
        distancias_grupo2.append(round(distancia, 2))
    
    return distancias_grupo1, distancias_grupo2

# Se distribuirán los mínimos hacia dos grupos
def distribuir_minimos(k):
    dist_min_g1 = []
    dist_min_g2 = []
    for _ in range(k):
        min_g1 = min(distancias_grupo1)
        min_g2 = min(distancias_grupo2)
        if min_g1 < min_g2:
            dist_min_g1.append(min_g1)
            distancias_grupo1.remove(min_g1)
        elif min_g2 < min_g1:
            dist_min_g2.append(min_g2)
            distancias_grupo2.remove(min_g2)
        else: 
            dist_min_g1.append(min_g1)
            distancias_grupo1.remove(min_g1)
            dist_min_g2.append(min_g2)
            distancias_grupo2.remove(min_g2)
    return dist_min_g1, dist_min_g2 

def asignar_punto(dist_min_g1, dist_min_g2, punto_nuevo, grupo1, grupo2):
    if len(dist_min_g1) > len(dist_min_g2):
        grupo1.append(punto_nuevo)
    elif len(dist_min_g1) < len(dist_min_g2):
        grupo2.append(punto_nuevo)
    else:
        if sum(dist_min_g1) / len(dist_min_g1) < sum(dist_min_g2) / len(dist_min_g2):
            grupo1.append(punto_nuevo)
        elif sum(dist_min_g1) / len(dist_min_g1) > sum(dist_min_g2) / len(dist_min_g2):             
            grupo2.append(punto_nuevo)
        else: print('Ingrese un K mayor para poder clasificar el punto en un grupo')
    return grupo1, grupo2


if __name__ == "__main__":
    k = int(input("Escoge un valor K mayor a 2: "))
    num_puntos = int(input("Escoge un número de puntos para cada grupo: "))
    assert k <= num_puntos*2, 'K no puede exceder la cantidad total de puntos de los dos grupos' 
    grupo1, grupo2 = llenar_grupo(num_puntos)
    punto_nuevo = dato_aleatorio()
    distancias_grupo1, distancias_grupo2 = distancias_g(num_puntos, grupo1, grupo2, punto_nuevo)
    dist_min_g1, dist_min_g2 = distribuir_minimos(k)
    grupo1, grupo2 = asignar_punto(dist_min_g1, dist_min_g2, punto_nuevo, grupo1, grupo2)
    print(f'Mínimos grupo 1: {dist_min_g1}')
    print(f'Mínimos grupo 2: {dist_min_g2}')
    print(f'Grupo 1: {grupo1}')
    print(f'Grupo 2: {grupo2}')
    print(f'Punto nuevo: {punto_nuevo}')