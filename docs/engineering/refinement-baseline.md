# Línea base de refinamiento de Ingeniería de Software

**Estado:** Aprobada para planificación del MVP; no certifica producción
**Regla:** este documento no autoriza implementación ni publicación en GitHub.

## Bloqueadores de decisión

Estos puntos siguen abiertos y no se resolverán por suposición:

- Resuelto por `ADR-057`: ventana móvil de 30 días, consumo diario promedio y
  cobertura indeterminada cuando no existe denominador válido.
- Resuelto por `ADR-059`: estados mínimos de Dataset, Riesgo, Inventario y
  Alertas.
- Resuelto por `ADR-058`: objetivos iniciales de benchmark, no productivos.
- Resuelto por decisión explícita: Project privado y repositorio público.

Los gaps de evidencia permanecen como trabajo trazable. No autorizan afirmar
cumplimiento productivo, institucional o clínico.

## Objetivo

Cerrar el contexto, decisiones, requisitos, arquitectura, modelos, calidad,
riesgos y documentación necesarios para que una futura spec sea publicable y
sus tickets sean implementables sin suposiciones.

## Orden de cierre

### R-01 Contexto y dominio

- [x] Propósito y alcance provisional del MVP.
- [x] Actores y vocabulario inicial.
- [x] Separación entre baseline, predicción ML y alerta operativa.
- [x] Stock entero no negativo para el MVP.
- [x] Confirmar unidades enteras para el MVP.
- [x] Confirmar fórmula de consumo y días de cobertura (`ADR-057`).

### R-02 Requisitos

- [x] Requisitos funcionales iniciales.
- [x] Requisitos no funcionales iniciales.
- [x] Casos de uso y escenarios preliminares.
- [x] Criterios iniciales del MVP.
- [x] Auditar estructura, duplicados preliminares y estados de requisitos.
- [x] Documentar revisión de requisitos y clasificar académico/MVP/futuro.
- [x] Registrar conflictos, requisitos sin evidencia y responsables en
  aclaraciones.
- [x] Consolidar matriz requisito–caso–escenario–prueba–código–evidencia
  documental.

### R-03 Decisiones y arquitectura

- [x] ADR de monolito modular en capas como propuesta.
- [x] ADR de validación antes de aplicar datos.
- [x] ADR de baseline determinista.
- [x] ADR de adaptador SALMI.
- [x] ADRs propuestos para jobs, autorización por ámbito, migraciones y
  retención.
- [x] Autorizar la arquitectura candidata como decisión técnica del MVP;
  aprobación de línea base completa pendiente.
- [x] Consolidar ADRs duplicados bajo `docs/adr/`.
- [x] Documentar límites de módulos, puertos y adaptadores; implementación
  pendiente.

### R-04 Modelos

- [x] BCE/VOPC y realizaciones seleccionadas.
- [x] Modelo lógico de datos preliminar.
- [x] Modelo API preliminar.
- [x] Revisión API–datos–seguridad.
- [x] Revisión de línea base arquitectónica.
- [ ] Revisar consistencia entre modelo conceptual, lógico y físico en código.
- [x] Completar modelo de dominio y estados (`ADR-059`).
- [x] Definir contratos documentales de importación y errores; implementación
  pendiente.
- [x] Registrar modelo físico propuesto e índices candidatos.

### R-05 Calidad y operación

- [x] Escenarios de calidad y riesgos iniciales.
- [x] Pruebas automatizadas del tracer bullet.
- [x] Registro explícito de evidencia ejecutada y no ejecutada.
- [x] Runbook operativo y modelo de seguridad propuestos.
- [x] Registro de evidencia y gaps de calidad.
- [x] Cerrar seguridad, privacidad, auditoría y retención como propuestas técnicas.
- [x] Definir estrategia de integración, contrato y despliegue.
- [x] Definir evidencia requerida para cada requisito.
- [x] Cumplir los umbrales iniciales de benchmark en el entorno de evaluación
  HTTP corregido (`.reports/execution/20261126/benchmark-approved-http-final.txt`);
  la medición anterior fue superseded por un arnés inválido.

### R-06 SDD y tracker

- [x] Constitución SDD local.
- [x] Spec, plan y tareas locales.
- [x] Índice de gobernanza y formato de work items.
- [x] Revisar artefactos con análisis de consistencia.
- [x] Aprobar la spec para planificación del MVP.
- [ ] Crear Milestone y GitHub Project.
- [ ] Publicar Spec Issue.
- [ ] Derivar tickets con dependencias.

## Gate de salida

La fase de refinamiento termina solo cuando:

1. no existen conflictos críticos entre documentos;
2. toda ambigüedad tiene decisión o marcador `[NEEDS CLARIFICATION]`;
3. cada tarea futura tiene un requisito y evidencia;
4. los ADRs tienen estado y decisor;
5. la arquitectura y los modelos están alineados;
6. el usuario aprueba la línea base;
7. recién entonces se publican tracker artifacts.

## No hacer todavía

- No crear Issues, Milestones, Projects ni PRs.
- No crear ramas de implementación.
- No presentar el código actual como producto terminado.
- No afirmar métricas ML, integración SALMI ni evidencia institucional.
