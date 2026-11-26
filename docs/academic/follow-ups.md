# Plan de seguimientos académicos

**Versión:** 0.1
**Estado:** Plan inicial basado en las fuentes académicas registradas

## Seguimiento 1 — Casos de uso y escenarios

### Objetivo

Refinar los requisitos funcionales y describir el comportamiento esperado del sistema.

### Entregables

- Informe del problema.
- Posicionamiento del producto.
- Actores y objetivos.
- Modelo de casos de uso.
- Mínimo seis especificaciones de casos de uso.
- Flujos básicos.
- Flujos alternos.
- Flujos de excepción.
- Precondiciones y postcondiciones cuando sean necesarias.
- Escenarios principales, alternos y críticos.
- Escenarios de calidad.
- Prototipos.
- Matriz de trazabilidad.

### Gate de salida

- Los actores están fuera del límite del sistema.
- Los casos de uso representan objetivos de valor.
- Los flujos están numerados y son verificables.
- No existen contradicciones entre requisitos, casos de uso y escenarios.

## Seguimiento 2 — Diagramas de interacción

### Objetivo

Realizar escenarios seleccionados mediante análisis y diseño orientado a objetos.

### Entregables

- Caso de uso seleccionado.
- Mínimo dos escenarios.
- Clases `Boundary`, `Control` y `Entity`.
- VOPC o vista de clases participantes.
- Mínimo dos diagramas de secuencia.
- Mínimo dos diagramas de colaboración/comunicación.
- Mínimo dos diagramas de clases de diseño.
- Responsabilidades y operaciones.
- Correspondencia entre secuencia y colaboración.

### Gate de salida

- Cada mensaje tiene receptor y responsabilidad.
- Las interacciones corresponden al escenario.
- Secuencia y colaboración representan el mismo comportamiento.
- Las clases de diseño soportan las operaciones modeladas.
- Los diagramas cumplen UML 2.5.1 y la convención gráfica del proyecto.

## Seguimiento 3 — Casos de prueba

### Objetivo

Verificar requisitos mediante casos de prueba diseñados antes y durante la implementación.

### Entregables

- Estrategia de pruebas.
- Casos de prueba funcionales.
- Casos de prueba de calidad.
- Técnicas de caja negra y caja blanca según corresponda.
- Pruebas unitarias, integración, validación y regresión según alcance.
- Evidencias y resultados.
- Defectos asociados.
- Matriz de trazabilidad de pruebas.

### Gate de salida

- Cada prueba referencia un requisito o escenario.
- Cada resultado reportado fue ejecutado.
- Los defectos están registrados.
- Las limitaciones están documentadas.
- La trazabilidad está actualizada.

## Dependencias

```text
Fuentes → Requisitos → Seguimiento 1 → Seguimiento 2 → Seguimiento 3
```

El proceso es iterativo: un defecto o cambio posterior puede reabrir un seguimiento y exigir actualizar sus artefactos dependientes.
