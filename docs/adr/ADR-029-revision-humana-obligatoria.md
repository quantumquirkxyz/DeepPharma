# ADR-029 — Revisión humana obligatoria

**Estado:** Aceptada para MVP
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

DeepPharma solo generará información de inventario, resultados de riesgo y
alertas para revisión humana autorizada. No ejecutará automáticamente acciones
clínicas, reposiciones institucionales ni cambios operativos irreversibles a
partir de un resultado ML o del fallback.

Una acción posterior debe conservar actor, autorización, contexto del resultado
y auditoría de la decisión.

## Consecuencias

- El sistema es apoyo operativo, no decisor autónomo.
- Las alertas deben mostrar contexto y limitaciones.
- Las pruebas deben verificar que una predicción no muta por sí sola el
  inventario ni produce una reposición.
