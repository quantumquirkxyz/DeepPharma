# Modelo lógico de datos

**Versión:** 0.1
**Estado:** Propuesta arquitectónica en refinamiento
**Fuente:** glosario, casos de uso, vista de datos y trazabilidad

## Entidades principales

| Entidad | Propósito |
|---|---|
| `Usuario` | Identidad y acceso |
| `Rol` | Capacidades autorizadas |
| `CentroSalud` | Ámbito operativo |
| `Medicamento` | Catálogo de medicamentos |
| `InventarioActual` | Estado actual por medicamento y centro |
| `RegistroInventario` | Historial de actualizaciones |
| `ConjuntoDatos` | Dataset recibido y versionado |
| `Experimento` | Ejecución de entrenamiento/evaluación |
| `Modelo` | Artefacto predictivo versionado |
| `PrediccionRiesgo` | Resultado de inferencia |
| `AlertaDesabastecimiento` | Condición operativa accionable |
| `GestionAlerta` | Historial de acciones sobre alertas |
| `FuenteIntegracion` | Configuración y procedencia externa |

## Reglas de integridad

- `InventarioActual` identifica un medicamento y un centro.
- `RegistroInventario` no elimina historial.
- `PrediccionRiesgo` referencia el modelo y versión utilizados.
- `AlertaDesabastecimiento` referencia una predicción o condición operativa.
- `GestionAlerta` conserva actor, estado anterior, estado nuevo y fecha.
- `ConjuntoDatos`, `Experimento` y `Modelo` conservan versiones y procedencia.
- Un `Experimento` registra configuración, semilla, métricas, limitaciones y
  referencia al conjunto de datos.
- Un `Modelo` no se habilita para inferencia solo por haber sido entrenado;
  requiere evaluación y aprobación explícita.
- `FuenteIntegracion` no almacena secretos en texto plano.

## Pendientes

- Definir claves y tipos físicos.
- Definir normalización.
- Definir índices.
- Definir política de retención.
- Definir migraciones.
