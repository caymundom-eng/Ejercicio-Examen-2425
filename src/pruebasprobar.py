from pathlib import Path

ruta = Path("log_iter.txt")
ruta.write_text("\n".join(f"evento {n}" for n in range(1, 4)), encoding="utf-8")

with ruta.open(encoding="utf-8") as f:
    procesado = [f"{idx}: {linea.strip()}" for idx, linea in enumerate(f, start=1)]

print(procesado)