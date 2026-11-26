# ADR-002 — Validación antes de aplicar datos

**Estado:** Aceptada
**Fecha:** 2026-11-25
**Decisión:** Equipo DeepPharma

## Contexto

El inventario operativo no puede ser alterado por cargas con errores de
esquema, tipos, referencias, cantidades o duplicados.

## Decisión

Toda carga se registra como `ConjuntoDatos` inmutable con fuente, versión,
estado, cantidad de registros y errores. Solo los conjuntos `VALIDO` podrán
ser aplicados por el servicio de importación. La validación no muta
`InventarioActual`.

## Consecuencias

- Los errores son consultables y reproducibles.
- La aplicación será una transacción separada de la validación.
- Se necesita versionar el esquema de entrada.
- Una carga aceptada no implica que los datos sean institucionalmente
  verdaderos; solo que cumplen el contrato técnico.
