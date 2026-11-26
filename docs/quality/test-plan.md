# Plan de pruebas

**Versión:** 0.1
**Estado:** Estrategia propuesta; catálogo diseñado y ejecución pendiente
**Fuentes:** `SRC-01`, `SRC-15`, requisitos y catálogo de escenarios

## 1. Objetivo

Verificar que DeepPharma cumple requisitos funcionales, reglas de negocio y atributos de calidad mediante pruebas trazables y ejecutadas con evidencia.

## 2. Niveles

- **Unitaria:** funciones, clases y reglas aisladas.
- **Integración:** interacción entre persistencia, servicios, adaptadores y componentes.
- **Sistema:** flujos completos de casos de uso.
- **Aceptación:** cumplimiento de escenarios y necesidades de actores.

La selección del nivel se rige por `docs/adr/ADR-010-estrategia-de-pruebas.md`.

## 3. Técnicas

- Partición de equivalencia.
- Análisis de valores límite.
- Tablas de decisión.
- Transición de estados.
- Caja negra.
- Caja blanca.
- Cobertura de ramas.
- Pruebas de regresión.
- Pruebas exploratorias.

## 4. Tipos adicionales

- Integridad de datos.
- Rendimiento.
- Seguridad y autorización.
- Accesibilidad.
- Usabilidad.
- Compatibilidad.
- Recuperación ante fallos.
- Calidad de datos.
- Evaluación de modelos ML.
- Reproducibilidad de experimentos.

## 5. Prioridad

1. Escenarios principales de `CU-01` a `CU-05`.
2. Excepciones de datos, autorización, predicción y alertas.
3. Escenarios de integración y modelos.
4. `CU-06` y evaluación SUS.
5. Casos candidatos de ampliación.

## 6. Evidencia mínima

Cada ejecución debe conservar:

- identificador;
- fecha y entorno;
- versión del código;
- datos de entrada;
- pasos;
- resultado esperado;
- resultado obtenido;
- estado;
- evidencia;
- defecto asociado, si existe.

No se marcará una prueba como aprobada sin ejecución verificable.
