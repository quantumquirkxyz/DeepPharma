# ADR-001 — Monolito modular en capas (compatibility view)

> La versión canónica se encuentra en
> [`../adr/ADR-001-monolito-modular-en-capas.md`](../adr/ADR-001-monolito-modular-en-capas.md).
> Este archivo se conserva temporalmente para no romper referencias existentes.

**Estado:** Propuesta
**Fecha:** 2026-11-25
**Decisor:** Equipo DeepPharma

## Contexto

DeepPharma necesita integrar inventario, datos históricos, predicción, alertas, dashboard y evaluación académica. El equipo debe demostrar trazabilidad, pruebas y una arquitectura reproducible con recursos limitados.

## Decisión

Utilizar un **monolito modular en capas** para el primer MVP:

- presentación;
- aplicación;
- dominio;
- infraestructura;
- módulo de datos y ML mediante contratos internos;
- adaptadores para SALMI y fuentes externas.

La base de datos será PostgreSQL cuando se confirme el stack de implementación. El entrenamiento y la inferencia se separarán mediante interfaces y artefactos versionados.

## Alternativas descartadas inicialmente

- **Microservicios:** complejidad operacional y de despliegue innecesaria para el primer MVP.
- **Serverless:** introduce decisiones de plataforma y observabilidad fuera del alcance académico inicial.
- **Lógica en la base de datos:** aumenta acoplamiento y dificulta pruebas.

## Consecuencias

### Positivas

- Menor complejidad de despliegue.
- Trazabilidad directa entre casos de uso y módulos.
- Pruebas de integración más sencillas.
- Posibilidad de separar módulos posteriormente.

### Negativas

- El proceso ML puede competir por recursos con la API.
- Se requiere disciplina modular para evitar un monolito acoplado.
- La escalabilidad independiente queda limitada inicialmente.

## Riesgos y revisión

Revisar esta decisión si el volumen, latencia, aislamiento de entrenamiento o integración con SALMI exige separar componentes.
