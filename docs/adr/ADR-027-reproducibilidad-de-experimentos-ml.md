# ADR-027 — Reproducibilidad completa de experimentos ML

**Estado:** Aceptada para MVP
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

Cada experimento ML conservará:

- versión del código;
- dependencias fijadas;
- semilla;
- configuración;
- esquema y hash del dataset;
- particiones;
- entorno documentado o contenedorizado;
- métricas y artefactos generados.

Un resultado no se considera reproducible solo por conservar la semilla.

## Consecuencias

- Los experimentos pueden repetirse y compararse.
- Los cambios de dependencia requieren registrar una nueva versión.
- El almacenamiento de artefactos debe distinguir modelos, datasets y reportes.
