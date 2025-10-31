from typing import NamedTuple
from datetime import datetime
import csv

Piloto=NamedTuple("Piloto", [("nombre", str),("escuderia", str)])

CarreraFP=NamedTuple("CarreraFP",[
        ("fecha_hora",datetime), 
        ("circuito",str),                    
        ("pais",str), 
        ("seco",bool), # True si el asfalto estuvo seco, False si estuvo mojado
        ("tiempo",float), 
        ("podio", list[Piloto])])

def lee_carreras(filename: str) -> list[CarreraFP]:
    Carreras=[]
    with open(filename, encoding="utf-8") as f:
        lector = csv.reader(f)
        next (lector)

        for fila in lector:
            (fecha_hora_str, circuito, pais, asfalto, tiempo_str, nom1, esc1, nom2, esc2, nom3, esc3) = fila

            fecha_hora = datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M")
            seco = (asfalto.strip().lower() == "seco")
            tiempo = float(tiempo_str)
            podio = [
                Piloto(nom1, esc1),
                Piloto(nom2, esc2),
                Piloto(nom3, esc3)
            ]

            carrera = CarreraFP(fecha_hora, circuito, pais, seco, tiempo, podio)
            Carreras.append(carrera)

            print(f"{fecha_hora_str} - {circuito} ({pais}) → Ganador: {nom1} ({esc1})")
    return Carreras

