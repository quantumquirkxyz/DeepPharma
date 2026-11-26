# Documento de arquitectura de software

**Versión:** 0.1
**Estado:** Línea base técnica del MVP; decisiones externas pendientes
**Metodología:** RUP
**ADR principal:** `ADR-001-monolito-modular-en-capas.md`

## 1. Propósito

Describir la arquitectura candidata de DeepPharma y sus relaciones con requisitos, casos de uso, calidad y despliegue.

## 2. Metas arquitectónicas

- Trazabilidad entre casos de uso y módulos.
- Alta cohesión y bajo acoplamiento.
- Validación y reproducibilidad de datos y modelos.
- Integración externa desacoplada.
- Seguridad por roles y ámbitos.
- Capacidad de pruebas automatizadas.
- Despliegue reproducible.

## 3. Restricciones

- Cumplimiento de la rúbrica académica.
- SALMI no tiene todavía un contrato técnico confirmado.
- El MVP debe poder ejecutarse con datos públicos, sintéticos o autorizados.
- No se publicarán secretos ni datos restringidos.

## 4. Estilo arquitectónico

Monolito modular en capas, con puertos y adaptadores donde se requiera aislamiento de fuentes externas y modelos.

## 5. Módulos candidatos

- Identidad y autorización.
- Inventario.
- Ingesta y calidad de datos.
- Entrenamiento y evaluación ML.
- Inferencia y predicciones.
- Alertas y notificaciones.
- Reportes.
- Integraciones.

## 6. Vistas RUP

- **Casos de uso:** realizaciones `ESC-CU05-01` y `ESC-CU04-01`.
- **Lógica:** dominio, aplicación e interfaces.
- **Procesos:** API, tareas programadas, entrenamiento e inferencia.
- **Implementación:** módulos del monolito y contratos.
- **Despliegue:** cliente, aplicación, base de datos y almacenamiento de modelos.
- **Datos:** inventario, predicciones, alertas, usuarios, experimentos y modelos.

## 7. Estado

La arquitectura sigue siendo una propuesta. La revisión de consistencia se
encuentra en `architecture-baseline-review.md` y
`api-data-security-consistency.md`. Su aprobación se decidirá mediante
`grill-with-docs`.
