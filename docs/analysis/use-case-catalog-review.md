# Revisión de consistencia del catálogo de casos de uso

**Versión:** 0.1
**Estado:** Revisión estructural completada; validación semántica pendiente
**Fecha:** 2026-11-25

## 1. Criterio de revisión

Un caso de uso se mantiene independiente cuando representa un objetivo de valor para un actor, con resultado, flujo, permisos y trazabilidad propios. Si solo representa una parte obligatoria o reutilizable de otro objetivo, se modela como `include` o como comportamiento interno.

## 2. Resultados

| Caso | Decisión preliminar | Justificación |
|---|---|---|
| CU-01 Registrar datos históricos | Independiente | Objetivo administrativo de incorporar un conjunto |
| CU-02 Entrenar y evaluar modelos | Independiente | Objetivo del ingeniero de ML y ciclo de experimento |
| CU-03 Generar predicciones | Independiente | Operación predictiva con disparador programado o manual |
| CU-04 Visualizar y gestionar alertas | Independiente | Objetivo principal del farmacéutico |
| CU-05 Gestionar inventario | Independiente | Objetivo operativo de registrar inventario |
| CU-06 Evaluar usabilidad SUS | Independiente académico | Requisito de entrega; actividad externa |
| CU-07 Validar datos | Independiente candidato / relacionado con CU-01 | Resultado propio de calidad y bloqueo de entrenamiento |
| CU-08 Preprocesar datos | Independiente candidato | Transformación reproducible antes de entrenamiento |
| CU-09 Sincronizar inventario | Independiente candidato | Integración externa con contrato y errores propios |
| CU-10 Evaluar modelos | Refinamiento candidato de CU-02 | Puede ser `include` de CU-02 si siempre es obligatorio |
| CU-11 Registrar modelo aprobado | Independiente candidato | Decisión y ciclo de vida con permisos propios |
| CU-12 Consultar explicación | Independiente candidato | Objetivo explícito de transparencia para usuarios |
| CU-13 Consultar inventario | Independiente candidato | Consulta de valor; puede separarse de actualización |
| CU-14 Consultar detalle de alerta | Refinamiento de CU-04 | Probablemente `include` u objetivo reutilizable |
| CU-15 Gestionar alerta | Independiente candidato | Mutación, auditoría y transición de estado propias |
| CU-16 Notificar riesgo crítico | `include` candidato de CU-03 | Se activa condicionalmente al producirse una condición crítica |
| CU-17 Generar reportes | Independiente candidato | Objetivo de consulta y exportación para administración |
| CU-18 Administrar usuarios y roles | Independiente candidato | Objetivo administrativo y de seguridad |
| CU-19 Configurar integraciones | Independiente candidato | Objetivo administrativo distinto de ejecutar sincronización |

## 3. Relaciones preliminares

Estas relaciones no se congelan hasta revisar las especificaciones:

- `CU-01` puede incluir `CU-07` cuando el registro siempre exige validación.
- `CU-07` puede habilitar `CU-08` después de aprobación.
- `CU-02` puede incluir `CU-10` si evaluar es obligatorio en cada entrenamiento.
- `CU-03` puede incluir condicionalmente `CU-16` cuando el nivel sea crítico.
- `CU-04` puede incluir `CU-14` al seleccionar una alerta.
- `CU-04` puede relacionarse con `CU-15` como extensión opcional de gestión.
- `CU-05` puede relacionarse con `CU-13` como consulta separada, si ambos tienen objetivos distintos.
- `CU-09` depende de `CU-19` para disponer de una fuente configurada.
- `CU-12` puede extender `CU-14` cuando el usuario solicite explicabilidad.

## 4. Comportamientos que no deben ser casos de uso

- Actualizar visualmente el dashboard.
- Calcular internamente una métrica sin objetivo de actor.
- Crear una instancia interna de un modelo.
- Aplicar una transformación automática sin actor o resultado independiente.
- Ejecutar un temporizador interno.
- Guardar una fila en base de datos.
- Enviar un retorno de método.

## 5. Riesgos de modelado

- Exceso de casos de uso derivados de pasos internos.
- Confundir la especificación académica de `CU-06` con una funcionalidad del MVP.
- Duplicar consulta de alertas entre `CU-04` y `CU-14`.
- Duplicar consulta de inventario entre `CU-05` y `CU-13`.
- Tratar `CU-10` como independiente sin justificar el objetivo de aprobación.
- Usar `include` o `extend` solo para completar el diagrama.

## 6. Siguiente validación

Antes de crear el diagrama general definitivo se debe:

1. Revisar las especificaciones una frente a otra.
2. Confirmar relaciones y dependencias.
3. Consolidar requisitos `RF`, `RNF` y `RN`.
4. Crear la matriz de trazabilidad.
5. Dibujar el modelo propuesto con relaciones justificadas.

La revisión estructural consolidada se encuentra en
`docs/requirements/use-case-review.md`. Las preguntas que requieren
conocimiento externo están registradas en
`docs/requirements/clarifications.md`.
