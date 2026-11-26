# ADR-001 — Monolito modular en capas

**Estado:** Aceptada
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Contexto

DeepPharma integra inventario, datos, predicción, alertas, dashboard y
evaluación académica. El primer MVP necesita trazabilidad y despliegue
reproducible con complejidad operacional limitada.

## Decisión propuesta

Usar un monolito modular en capas:

- presentación;
- aplicación;
- dominio;
- infraestructura;
- datos/ML mediante contratos internos;
- adaptadores para fuentes externas.

## Alternativas

- Microservicios: complejidad operacional prematura para el MVP.
- Serverless: introduce decisiones de plataforma fuera del alcance actual.
- Lógica principal en la base de datos: aumenta acoplamiento y dificulta
  pruebas.

## Consecuencias

La propuesta reduce complejidad inicial y facilita trazabilidad, pero requiere
disciplina modular, límites de API, workers para cargas futuras y una política
de escalamiento explícita.

## Condición de aceptación

La propuesta se convertirá en línea base únicamente después de cerrar:

- vistas RUP;
- contratos API;
- datos, índices y retención;
- autorización por ámbito;
- workers/jobs;
- despliegue y migraciones;
- escenarios de calidad medibles.
