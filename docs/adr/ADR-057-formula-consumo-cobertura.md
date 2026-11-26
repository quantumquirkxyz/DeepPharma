# ADR-057 — Fórmula de consumo y días de cobertura

**Estado:** Aceptada para el MVP
**Fecha:** 2026-11-26
**Decisor:** Propietario del proyecto

## Decisión

El consumo diario promedio será el total de unidades consumidas dividido por
los días válidos de una ventana móvil de 30 días.

```text
consumo_diario_promedio = unidades_consumidas / días_válidos
días_de_cobertura = stock_disponible / consumo_diario_promedio
```

Si no existe consumo válido o el denominador es cero, cobertura y riesgo serán
`INDETERMINATE`; nunca se interpretarán como riesgo cero.

## Consecuencias

- La ventana y las unidades quedan versionadas y auditables.
- Los datos insuficientes producen incertidumbre explícita.
- Los umbrales de riesgo se mantienen separados de la fórmula.
