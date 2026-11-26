# VOPC-CU04-01 — Consultar alertas críticas

**Escenario:** `ESC-CU04-01`
**Caso de uso:** `CU-04`
**Estado:** Modelo de análisis preliminar

## Participantes

| Participante | Estereotipo | Responsabilidad |
|---|---|---|
| `Farmacéutico` | Actor | Solicitar y revisar alertas de su ámbito |
| `PantallaAlertasPriorizadas` | Boundary | Recibir filtros y presentar resultados |
| `ControlConsultaAlertas` | Control | Coordinar permisos, consulta y priorización |
| `AlertaDesabastecimiento` | Entity | Representar estado y prioridad de una alerta |
| `PrediccionRiesgo` | Entity | Representar el resultado predictivo asociado |
| `InventarioActual` | Entity | Proporcionar estado de inventario y cobertura |
| `Medicamento` | Entity | Identificar el medicamento |
| `CentroSalud` | Entity | Identificar el centro y ámbito |

## Responsabilidades y restricciones

- El actor interactúa con la frontera.
- La frontera no decide prioridad ni ejecuta reglas de negocio.
- El control verifica permisos y coordina la consulta.
- La alerta conserva referencia a predicción e inventario.
- La clasificación operativa no se confunde con la salida original del modelo.
