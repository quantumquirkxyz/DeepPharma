# Modelo físico de datos

**Estado:** Propuesta técnica; pendiente de aprobación de arquitectura.

## Reglas físicas propuestas

- Todas las entidades tienen clave primaria estable.
- Las relaciones usan claves foráneas y restricciones explícitas.
- `inventario_actual` tiene unicidad por medicamento y centro.
- `stock_actual` es entero no negativo en el MVP.
- Historiales y gestiones son append-only.
- Consultas de inventario, alertas y predicciones requieren índices por
  centro, estado, entidad y fecha.
- Los datasets grandes no deben depender indefinidamente de un JSON único;
  la decisión de partición u object storage depende de mediciones y retención.

## Índices candidatos

| Tabla | Índice | Motivo |
|---|---|---|
| `inventario_actual` | `(centro_salud_id, medicamento_id)` | consulta operativa |
| `registro_inventario` | `(inventario_id, registrado_en)` | historial |
| `predicciones_riesgo` | `(inventario_id, generado_en)` | última predicción |
| `alertas_desabastecimiento` | `(estado, nivel, creada_en)` | bandeja de alertas |
| `gestion_alerta` | `(alerta_id, gestionada_en)` | auditoría |
| `conjuntos_datos` | `(fuente, version, recibido_en)` | procedencia |
| `experimentos` | `(conjunto_datos_id, creado_en)` | reproducibilidad |
| `modelos` | `(estado, creado_en)` | ciclo de vida |

## Pendientes de aprobación

- tipos físicos finales;
- índices medidos;
- retención y archivado;
- clasificación de datos;
- estrategia para datasets grandes;
- migración y rollback por entorno.
