#Videoteca digital
#identificar que material audiovisual es popular y reciente

peliculas = ["Michael", "Mortal Kombat II", "Inception","Project Hail Mary",
"Almost Famous", "Sound of Metal", "The Drama", "Knives Out", "Hot Fuzz", "Shrek 2" ]
año_de_lanzamiento = [2026, 2026, 2010, 2026, 2000, 2019, 2026, 2019, 2007, 2004]
calificacion = [7.5, 8.0, 8.8, 7.9, 7.9, 8.1, 6.5, 8.0, 7.8, 7.2]
genero = ["Drama", "Acción", "Ciencia Ficción", "Ciencia Ficción", "Drama", "Drama", "Drama", "Misterio", "Comedia", "Animación"]
print("Películas disponibles en la videoteca digital:")
for indice in range(len(peliculas)):
    print(f"{peliculas[indice]} - Año: {año_de_lanzamiento[indice]}, Calificación: {calificacion[indice]}, Género: {genero[indice]}")   

# Solicitar criterios al usuario (calificación mínima y año mínimo)
try:
    umbral_calificacion = float(input("Introduce la calificación mínima (ej. 8.0): "))
except ValueError:
    print("Entrada inválida para calificación. Usando valor por defecto 8.0.")
    umbral_calificacion = 8.0
try:
    año_lanzamiento = int(input("Introduce el año mínimo de lanzamiento (ej. 2020): "))
except ValueError:
    print("Entrada inválida para año. Usando valor por defecto 2026.")
    año_lanzamiento = 2026
#contar titulos con una igual o mayor calificacion o igual a cierto umbral dado y cuyo año de lanzamiento sea posterior o igual a cierto año dado
def contar_peliculas(peliculas, umbral_calificacion, año_limite):
    contador = 0
    for indice in range(len(peliculas)):
        if calificacion[indice] >= umbral_calificacion and año_de_lanzamiento[indice] >= año_limite:
            contador += 1
    return contador

# Mostrar el conteo total de películas que cumplen con los criterios
total_peliculas = contar_peliculas(peliculas, umbral_calificacion, año_lanzamiento)
print(f"Total de películas con calificación >= {umbral_calificacion} y año de lanzamiento >= {año_lanzamiento}: {total_peliculas}")
