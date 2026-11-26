# Revisión estructural de especificaciones de casos de uso

**Estado:** Revisión documental completada; dependencias externas y evidencia
de ejecución pendientes.

## Criterio

Cada especificación debe contener objetivo, actores, disparador,
precondiciones, postcondiciones, flujo básico, alternos, excepciones, reglas,
requisitos, escenarios, criterios de aceptación y pendientes.

## Resultado

| Casos | Estructura | Semántica | Estado |
|---|---|---|---|
| CU-01–CU-19 | Todas las especificaciones contienen las secciones RUP esenciales | Relaciones, fuentes, reglas y criterios contrastados documentalmente; dependencias externas abiertas | Revisión documental |
| CU-04, CU-05 | Además tienen realizaciones detalladas | Consistentes con DS/DCOL/DCD preliminares | Borrador revisado |
| CU-06 | Tiene alcance académico separado del MVP | Protocolo SUS y muestra pendientes | Borrador académico |

## Hallazgos de consistencia

1. `CU-01` menciona CSV/XLSX y el tracer bullet acepta JSON; debe resolverse
   mediante `CL-08`, no por supuesto.
2. `CU-01` propone el período 2019–2023 sin evidencia institucional; queda
   sujeto a `CL-09`.
3. `CU-05` conserva referencias a unidades y cobertura; el MVP fija stock
   entero no negativo, pero las reglas institucionales siguen abiertas.
4. `CU-04`, `CU-14` y `CU-15` requieren conservar la separación entre consulta,
   detalle y gestión; el catálogo mantiene esas relaciones como candidatas.
5. `CU-02`, `CU-10` y `CU-11` deben mantener la separación entre entrenar,
   evaluar y aprobar modelos.

## Conclusión

Las especificaciones tienen una estructura documental suficiente para la
revisión académica y sus dependencias están registradas. No deben marcarse
como evidencia ejecutada ni como aprobación institucional mientras existan
aclaraciones externas o pruebas pendientes.
