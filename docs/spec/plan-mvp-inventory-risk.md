# Plan SDD — MVP de inventario y riesgo

**Estado:** Plan aprobado para derivación de tickets; implementación requiere
tickets `status:ready`

## Arquitectura

Se mantiene el monolito modular en capas:

- API/presentación;
- aplicación;
- dominio;
- persistencia;
- adaptadores de integración;
- pipeline ML reproducible síncrono y seam de jobs futuro;

## Slices

1. **Importación y validación:** entidades de dataset, carga, validaciones y
   reporte de errores.
2. **Aplicación transaccional:** aplicar únicamente conjuntos válidos,
   registrar procedencia y auditoría.
3. **ML y riesgo reproducible:** preparar dataset, entrenar/evaluar modelo,
   registrar experimento y conservar el fallback baseline versionado.
4. **Gestión de alertas:** ya implementada parcialmente; completar filtros,
   transiciones y evidencia.
5. **SALMI simulado:** puerto, adaptador fixture y sincronización segura.
6. **Verificación:** integración, trazabilidad, documentación y quality gates.

## Seams

- `DatasetValidator`: contrato de validación independiente de FastAPI.
- `InventoryImportService`: transacción de validación y aplicación.
- `RiskEvaluator`: evaluación ML o fallback determinista versionado.
- `ExperimentRunner`: entrenamiento/evaluación reproducible y síncrono en el
  MVP, con seam para jobs posteriores.
- `TemporalEvaluator`: particiones temporales, controles de fuga y métricas
  comparables contra el fallback.
- `ExternalInventorySource`: puerto para SALMI y adaptadores.

## Estrategia de datos

Los conjuntos importados son inmutables. La aplicación a inventario se ejecuta
solo desde un conjunto válido y deja un actor y una fuente. Los errores son
consultables y no se mezclan con el inventario operativo.

## Riesgos

- El contrato de entrada puede cambiar: versionar esquema.
- Datos insuficientes: usar fixtures sintéticos y declarar limitaciones.
- Cargas grandes: empezar con límites explícitos y medir antes de optimizar.
