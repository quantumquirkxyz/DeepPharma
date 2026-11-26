# ADR-032 — Original restringido y proyección operativa mínima

**Estado:** Aceptada para MVP
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

Cuando sea necesario conservar un dataset fuente completo para
reproducibilidad, se almacenará en un repositorio restringido, versionado y
con controles de acceso separados. La aplicación operativa utilizará una
proyección mínima con los campos necesarios para inventario, riesgo,
auditoría y evaluación.

Los usuarios operativos no tendrán acceso automático al original completo.
Toda extracción o consulta excepcional requiere autorización, finalidad,
registro y cumplimiento de la política de datos aplicable.

## Consecuencias

- Se preserva la reproducibilidad sin exponer datos innecesarios.
- El hash y la referencia del original deben quedar ligados al experimento.
- La retención y eliminación del original siguen sujetas a la política
  institucional.
