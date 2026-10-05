"""Escriba aquí sus pruebas. No borre ni modifique tests/test_base.py.

Cada función de prueba comienza con test_ y usa assert.
Agregue al menos los cuatro casos descritos en el README.
Los imports ya están preparados; deepcopy crea una copia independiente
de la lista y de los diccionarios para comprobar que no se modificaron.
"""
from copy import deepcopy

from reservas import modificar_reserva


# compruebe ok, el nuevo horario y la conservacion de otra reserva
def test_cambio_valido():
    reservas = [{"id": "R1", "sala": "A", "inicio": 540, "fin": 600, "estado": "confirmada"},
        {"id": "R2", "sala": "A", "inicio": 720, "fin": 780, "estado": "confirmada"},
    ]
    resultado = modificar_reserva(reservas, "R1", 600, 660)

    assert resultado == "OK"
    assert reservas[0]["inicio"] == 600
    assert reservas[0]["fin"] == 660
    assert reservas[1] == {"id": "R2", "sala": "A", "inicio": 720, "fin": 780, "estado": "confirmada"}

#comprobar la cadena conflicto
def test_conflicto_horario():
    """Prueba 2: Comprueba la devolución exacta de 'CONFLICTO'."""
    reservas = [{"id": "R1", "sala": "A", "inicio": 540, "fin": 600, "estado": "confirmada"},
        {"id": "R2", "sala": "A", "inicio": 600, "fin": 660, "estado": "confirmada"},
    ]
    resultado = modificar_reserva(reservas, "R1", 630, 690)
    assert resultado == "CONFLICTO"

#compruebe que la lista completa queda igual a una copia independiente previa
def test_conservacion_ante_conflicto():
    reservas = [{"id": "R1", "sala": "A", "inicio": 540, "fin": 600, "estado": "confirmada"},
                {"id": "R2", "sala": "A", "inicio": 600, "fin": 660, "estado": "confirmada"},
    ]
    antes = deepcopy(reservas)
    modificar_reserva(reservas, "R1", 630, 690)
    assert reservas == antes

#compruebe que comenzar al terminar otra reserva se acepta y deja el horario esperado
def test_limite_adyacente():
    reservas = [{"id": "R1", "sala": "A", "inicio": 540, "fin": 600, "estado": "confirmada"},
                {"id": "R2", "sala": "A", "inicio": 600, "fin": 660, "estado": "confirmada"}
    ]

    resultado = modificar_reserva(reservas, "R1", 660, 720)
    assert resultado == "OK"
    assert reservas[0]["inicio"] == 660
    assert reservas[0]["fin"] == 720


