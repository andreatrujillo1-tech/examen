"""Escriba aquí sus pruebas. No borre ni modifique tests/test_base.py.

Cada función de prueba comienza con test_ y usa assert.
Agregue al menos los cuatro casos descritos en el README.
Los imports ya están preparados; deepcopy crea una copia independiente
de la lista y de los diccionarios para comprobar que no se modificaron.
"""
from copy import deepcopy

from reservas import modificar_reserva


# Ejemplo de estructura, sin solución del caso:
# def test_nombre_del_comportamiento():
#     datos = [...]
#     antes = deepcopy(datos)
#     resultado = modificar_reserva(datos, ...)
#     assert resultado == "..."
#     assert datos == antes  # Cuando la operación debe conservar TODO.
