# Revisión de consistencia API–datos–seguridad

**Estado:** Revisión completada; gaps registrados.

## Invariantes

| Invariante | API | Datos | Seguridad | Estado |
|---|---|---|---|---|
| Inventario único por medicamento-centro | POST actualiza | restricción única | escritura protegida | Parcial: falta ámbito |
| Historial inmutable | endpoint de history | registro append-only | actor autenticado | Parcial |
| Dataset no validado no afecta inventario | validación separada | estado del conjunto | escritura protegida | Falta endpoint de aplicación |
| Alerta tiene origen | alertas referencian predicción | FK a predicción/inventario | lectura protegida | Parcial |
| Acción de alerta auditable | PATCH | `GestionAlerta` | `alerts:manage` | Implementado para baseline |
| Fuente externa aislada | contrato propuesto | fuente/versionado pendiente | contrato autorizado | SALMI simulado pendiente |

La implementación actual permite destinos de estado válidos, pero todavía
debe aplicar la máquina de transiciones de `ADR-018`; esta diferencia queda
registrada como gap de implementación y no como cumplimiento completo.

Los endpoints de catálogo actuales aún requieren protección explícita para
cumplir `ADR-020`; la documentación define el comportamiento objetivo y no
declara el código actual como conforme.

## Contratos que deben cerrarse

- esquema estricto de fila de importación;
- versión del esquema;
- respuestas de error;
- paginación y límites;
- ámbito de centro;
- idempotencia;
- retención y consulta de auditoría.
