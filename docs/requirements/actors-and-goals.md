# Catálogo de actores y objetivos

**Estado:** Borrador validado por grill-with-docs
**Versión:** 0.1
**Fuente:** Baseline académico de DeepPharma y decisiones confirmadas del equipo
**Última actualización:** 2026-11-25

## 1. Propósito

Este catálogo identifica los actores externos que interactúan con DeepPharma, sus objetivos y sus límites de responsabilidad. Es la fuente previa al modelo general de casos de uso.

DeepPharma incluye la ingesta y validación de inventario, el entrenamiento y uso operativo de modelos predictivos, la generación de riesgos y alertas, la consulta del dashboard y la actualización del inventario. No incluye la operación interna de SALMI, la decisión administrativa de compra, la entrega física de medicamentos ni la atención clínica al paciente.

## 2. Actores humanos

| ID | Actor | Objetivo principal | Responsabilidades |
| --- | --- | --- | --- |
| ACT-01 | Administrador del sistema | Mantener la configuración y operación técnica de DeepPharma | Usuarios, configuración, integraciones y soporte operativo |
| ACT-02 | Farmacéutico | Anticipar y responder al riesgo de desabastecimiento | Actualizar inventario, consultar alertas, revisar riesgos y actuar según procedimientos |
| ACT-03 | Ingeniero de Machine Learning | Entrenar, evaluar y registrar modelos predictivos | Preparar datos, ejecutar entrenamiento, evaluar modelos y aprobar versiones |
| ACT-04 | Evaluador de usabilidad | Evaluar la usabilidad del producto | Coordinar y analizar la evaluación SUS como actividad externa |
| ACT-05 | Administrador de farmacia | Administrar la operación de inventario y alertas de farmacia | Supervisar inventario, alertas y reportes de su ámbito |

`ACT-01` y `ACT-05` son actores independientes. No se establece generalización hasta disponer de evidencia de que uno hereda las capacidades del otro.

El actor principal de valor es `ACT-02 Farmacéutico`.

## 3. Sistemas externos

| ID | Actor | Interacción | Estado |
| --- | --- | --- | --- |
| EXT-01 | SALMI | Fuente o destino potencial de sincronización de inventario | Integración objetivo; contrato técnico pendiente |
| EXT-02 | Portal de Datos Abiertos de Panamá | Proporciona datos históricos para `CU-01` | Fuente objetivo; API o formato estable pendiente de verificación |
| EXT-03 | Servicio de correo/notificaciones | Entrega notificaciones de riesgo crítico | Alcance funcional inicial |

La falta de contrato técnico de SALMI es un riesgo y una restricción. El primer MVP no asumirá acceso directo a SALMI; podrá utilizar adaptadores y datos sintéticos o públicos autorizados.

Los datos del Portal de Datos Abiertos deberán registrar procedencia, versión, fecha de descarga y controles de calidad. Se distinguirán datos públicos, sintéticos e institucionales.

## 4. Casos de uso de alto nivel

| ID | Caso de uso | Actor iniciador | Objetivo |
| --- | --- | --- | --- |
| CU-01 | Registrar datos históricos de inventario | ACT-01 | Cargar, validar y preparar datos históricos |
| CU-02 | Entrenar y evaluar modelos de ML | ACT-03 | Comparar y registrar un modelo aprobado |
| CU-03 | Generar predicciones de riesgo | DeepPharma / actor autorizado bajo demanda | Producir predicciones diarias con horizonte definido |
| CU-04 | Visualizar alertas priorizadas | ACT-02 / ACT-05 | Consultar y gestionar alertas accionables |
| CU-05 | Gestionar inventario en tiempo real | ACT-02 / ACT-05 | Registrar, validar y consultar inventario |

`CU-06 Evaluar usabilidad con SUS` se conserva como caso de uso académico de evaluación externa para cumplir el mínimo de seis especificaciones. No forma parte del modelo funcional principal ni implica que DeepPharma implemente un módulo SUS.

Esta separación es una decisión académica explícita: `CU-06` tendrá especificación, escenarios y trazabilidad propios, pero se clasificará como actividad de validación del producto.

## 5. Refinamientos confirmados

- `CU-05` se refinará en registro, validación, consulta, sincronización y detección de umbral según objetivos reales. La detección automática no se convertirá artificialmente en actor o caso de uso independiente.
- `CU-02` separa entrenamiento y evaluación de modelos de `CU-03`, que representa inferencia operativa.
- `CU-04` se refinará en consulta, filtros, detalle, reconocimiento y exportación cuando cada elemento represente un objetivo reutilizable y trazable.
- La notificación de riesgo crítico forma parte del alcance funcional inicial y se relaciona con `EXT-03`.
- Los temporizadores y automatizaciones internas no son actores externos.

## 6. Pendientes y evidencia requerida

- Confirmar permisos, contrato y formato de integración de SALMI.
- Verificar disponibilidad, estabilidad y licencia de la fuente histórica del Portal de Datos Abiertos.
- Confirmar la matriz de roles y permisos con stakeholders.
- Validar si `ACT-01` y `ACT-05` tienen capacidades superpuestas.
- Derivar el diagrama general de casos de uso a partir de este catálogo.
