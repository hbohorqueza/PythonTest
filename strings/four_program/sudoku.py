def checkset(digs):
    return sorted(list(digs)) == [str(x) for x in range(1, 10)]

# Ejemplo de Sudoku válido como lista de strings
rows = [
    "295743861",
    "431865927",
    "876192543",
    "387459216",
    "612387495",
    "549216738",
    "763524189",
    "928671354",
    "154938672"
]

ok = True

# Verificar filas
for r in range(9):
    if not checkset(rows[r]):
        ok = False
        break

# Verificar columnas
if ok:
    for c in range(9):
        col = [rows[r][c] for r in range(9)]
        if not checkset(col):
            ok = False
            break

# Verificar subcuadrados 3x3
if ok:
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = []
            for r in range(3):
                for c in range(3):
                    square.append(rows[i + r][j + c])
            if not checkset(square):
                ok = False
                break

# Veredicto final
print("Si" if ok else "No")
