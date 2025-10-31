from motoFP import lee_carreras

def test_lee_carreras():
    print("Test lee_carreras\n")

    # 1️⃣ Llamamos a la función con la ruta del CSV
    ruta = "data/mundial_motofp.csv"
    carreras = lee_carreras(ruta)

    # 2️⃣ Mostramos el número total de carreras
    print(f"Número de carreras leídas: {len(carreras)}\n")

    # 3️⃣ Mostramos las dos primeras y las dos últimas
    print("Las dos primeras son:")
    for carrera in carreras[:2]:
        print("\t", carrera)

    print("\nLas dos últimas son:")
    for carrera in carreras[-2:]:
        print("\t", carrera)

# 4️⃣ Bloque principal (para ejecutar el test directamente)
if __name__ == "__main__":
    test_lee_carreras()
