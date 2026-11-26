# Documentación de DeepPharma

## Mapa documental

| Área | Propósito | Estado |
|---|---|---|
| `academic/` | Rúbrica, fuentes académicas y seguimientos | Base inicial |
| `sources/` | Jerarquía y registro de fuentes | Inicial |
| `requirements/` | Actores, requisitos, casos, escenarios y trazabilidad | En refinamiento |
| `analysis/` | Auditorías, BCE/VOPC y responsabilidades | En refinamiento |
| `design/` | Diagramas UML y realizaciones | En refinamiento |
| `architecture/` | Documento RUP, vistas y riesgos | Propuesta |
| `adr/` | Decisiones arquitectónicas canónicas | En consolidación |
| `quality/` | Plan y catálogo de pruebas | Propuesta |
| `implementation/` | Contratos y límites técnicos | Propuesta |
| `spec/` | Constitución, spec, plan y tareas SDD | Borrador local |
| `engineering/` | Gates de refinamiento y auditorías | Activo |
| `security/` | Seguridad, privacidad y amenazas | Propuesta |
| `operations/` | Despliegue y operación | Propuesta |

## Reglas documentales

1. La rúbrica y las instrucciones oficiales tienen precedencia sobre las
   propuestas técnicas.
2. Un documento debe declarar versión, estado, fuente y alcance.
3. `Propuesta` o `Borrador` no significa aprobado.
4. Toda decisión técnica estable debe vivir en un ADR.
5. Toda afirmación de cumplimiento debe tener evidencia ejecutada.
6. Los cambios de requisitos deben actualizar trazabilidad, casos, pruebas y
   arquitectura afectados.

## Gates

- **Refinamiento:** no quedan conflictos críticos ni decisiones silenciosas.
- **Línea base:** el usuario aprueba requisitos, arquitectura y pruebas.
- **Tracker:** se publica una Spec Issue y luego tickets derivados.
- **Implementación:** cada ticket tiene criterios y evidencia.
- **Cierre:** código, documentación, pruebas y evidencia coinciden.

El estado actual y las brechas se mantienen en
`engineering/refinement-baseline.md` y en los informes de `.reports/`.
