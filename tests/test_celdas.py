from src.bingo import carton
from src.bingo import validar_quince_numeros

def test_contar_celdas_ocupadas():
    carton = (
        (1,0,1,0,0,1,0,0,1),
        (1,0,0,1,0,0,1,0,1),
        (1,0,0,0,1,0,0,1,1),
     )
    # Esperamos encontrar 15 celdas ocupadas.
    assert validar_quince_numeros(carton) == True
