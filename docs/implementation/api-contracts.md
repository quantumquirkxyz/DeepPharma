# Contratos API iniciales

**Versión:** 0.1
**Estado:** Línea base técnica aceptada; detalles de límites y OpenAPI pendientes de implementación
**Fuente:** casos de uso y arquitectura

## Principios

- Los contratos representan recursos y operaciones del dominio.
- Toda operación requiere autorización según rol y ámbito.
- Las respuestas no exponen secretos ni datos fuera del permiso.
- Los errores tienen estructura consistente.
- Los contratos se versionan antes de romper consumidores.

## Recursos candidatos

| Recurso | Casos relacionados |
|---|---|
| `/inventory` | CU-05, CU-13 |
| `/historical-datasets` | CU-01, CU-07, CU-08 |
| `/experiments` | CU-02, CU-10 |
| `/models` | CU-11 |
| `/predictions` | CU-03, CU-12 |
| `/alerts` | CU-04, CU-14, CU-15 |
| `/reports` | CU-17 |
| `/users` y `/roles` | CU-18 |
| `/integrations` | CU-09, CU-19 |

## Contrato común de error

```json
{
  "code": "VALIDATION_ERROR",
  "message": "Descripción accionable",
  "details": [],
  "traceId": "identificador-de-correlación"
}
```

## Reglas

- `4xx` representa errores del consumidor o autorización.
- `5xx` representa fallos del servicio o dependencia.
- Las operaciones mutantes deben definir idempotencia cuando corresponda.
- Las respuestas de predicción deben incluir modelo, versión, fecha y horizonte.
- Las respuestas de inventario deben incluir fuente, fecha y estado de actualización.
- Las respuestas de alertas deben incluir predicción o condición de origen.

## Decisiones pendientes de cierre

- OpenAPI como contrato publicado y versionado.
- Paginación, filtros y límites máximos de colección.
- Códigos de dominio y catálogo de errores.
- Idempotencia de operaciones mutantes.
- Ámbito de centro de salud en cada consulta.
- Política de compatibilidad y deprecación.

## Pendientes

- Implementar la especificación OpenAPI versionada.
- Implementar paginación y filtros.
- Implementar códigos de dominio.
- Implementar claves de idempotencia.

## Correspondencia de datos

| Recurso | Entidades | Seguridad mínima | Estado |
|---|---|---|---|
| `/inventory` | `InventarioActual`, `RegistroInventario` | `inventory:read/write` + ámbito | Parcial |
| `/datasets` | `ConjuntoDatos` | `inventory:write` | Validación inicial |
| `/predictions` | `PrediccionRiesgo` | `inventory:read` | Baseline |
| `/alerts` | `AlertaDesabastecimiento`, `GestionAlerta` | read/manage + ámbito | Baseline parcial |
| `/integrations` | fuentes externas | administración | No implementado |

El estado `Parcial` significa que existe un tracer bullet, no que el contrato
esté aprobado para producción.
