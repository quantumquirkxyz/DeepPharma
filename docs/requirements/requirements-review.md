# Revisión de requisitos

**Estado:** Baseline MVP aprobada para planificación; no constituye
certificación institucional ni productiva.

## Cobertura documental

| Artefacto | Cobertura | Estado |
|---|---|---|
| Necesidades y características | 10 necesidades / características | Presente |
| Requisitos funcionales | RF-01–RF-18 | Baseline MVP aprobada; ejecución parcial |
| Requisitos no funcionales | RNF-01–RNF-22 | Aprobados como objetivos; medición parcial |
| Reglas de negocio | RN-01–RN-22 | Baseline MVP aprobada; evidencia pendiente |
| Actores y objetivos | ACT/EXT catalogados | En refinamiento |
| Casos de uso | CU-01–CU-19 | Especificaciones estructuradas |
| Escenarios | 87 escenarios | Diseñados, no ejecutados |
| Pruebas | CP-CU01–CP-CU19 | Diseñadas, evidencia parcial |

## Reglas de calidad aplicadas

- Cada requisito usa un identificador estable.
- Cada requisito debe tener caso, escenario y prueba.
- Las metas de rendimiento no se consideran cumplidas sin medición.
- Las capacidades institucionales no se convierten en hechos sin fuente.
- Los requisitos candidatos no se confunden con requisitos aprobados.

## Hallazgos

1. La matriz inicial relaciona necesidades con requisitos y escenarios, pero la
   columna de código/evidencia debe completarse por slice.
2. RNF-02, RNF-03, RNF-04, RNF-05, RNF-13, RNF-16 y RNF-17 requieren entorno,
   volumen y medición antes de fijar objetivos.
3. RF-02, RF-10, RF-11 y RF-12 pertenecen al futuro ciclo ML y no deben
   presentarse como implementados por el baseline determinista.
4. RF-09 y RF-18 dependen del contrato y configuración de fuentes; SALMI
   continúa simulado y queda como seam explícito.
5. La trazabilidad detallada de AC-01–AC-14 está en
   `docs/requirements/acceptance-traceability-mvp.md`; los criterios no
   ejecutados siguen siendo trabajo de verificación y bloquean cualquier
   afirmación de cumplimiento.

## Aprobación

El propietario del proyecto autoriza esta baseline para derivar arquitectura,
specs y tickets del MVP. Los criterios `Partial` y `Not executed` son trabajo
futuro trazable; no se presentan como comportamiento ya implementado.

## Decisión de refinamiento

Los requisitos se clasifican en:

- `académico`: exigido por la rúbrica;
- `MVP`: necesario para el tracer bullet funcional;
- `futuro`: depende de datos, contratos o decisiones no disponibles;
- `candidato`: requiere aprobación antes de entrar al alcance.
