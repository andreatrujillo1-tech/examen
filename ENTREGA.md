# Entrega individual — Parte práctica

- Nombre y código: Andrea Trujillo Antezana  94046
- URL del repositorio privado: 
- Rama entregada: Andrea 
- Commit final: se presenta en el formulario/mensaje de entrega después del último commit.

## Resultado inicial

- Comando ejecutado:
- Resumen real de pytest antes de cambiar el código: falta comprobar  con test

## Cambios y requisitos
puse un if para ver si hay conflicto y retorno un "CONFLICTO", porque faltaba cumplir con RF-04
## Trazabilidad de sus pruebas

| Nombre de la prueba | Requisito | Resultado esperado |
|---|---|---|
|test_cambio_valido | comprobar el OK, el nuevo horario y la conservacion de otra reserva|cambio sea valido |
|test_conflicto_horario| comprobar la cadena CONFLICTO | |
|test_conservacion_ante_conflicto |comprobar que la lista completa queda igual a una copia independiente previa | Exista un conflicto |
|test_limite_adyacente| comprobar que comenzar al terminar otra reserva se acepta y deja el horario esperado | Dejar el horario esperado|

## Resultado final y límites

- Comando ejecutado: pytest
- Resumen real de pytest (passed/failed y otros resultados si aparecen): Pasaron 7 test en 0.04s
- ¿Qué comportamiento sigue sin comprobar? Escriba una limitación concreta:


No presente una prueba fallida como aprobada. Conserve y explique cualquier pendiente.
