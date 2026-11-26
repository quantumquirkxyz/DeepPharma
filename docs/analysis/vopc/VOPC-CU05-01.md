# VOPC-CU05-01 — Registrar actualización válida de inventario

**Escenario:** `ESC-CU05-01`
**Caso de uso:** `CU-05`
**Estado:** Modelo de análisis preliminar

## Participantes

| Participante | Estereotipo | Responsabilidad |
|---|---|---|
| `Farmacéutico` | Actor | Iniciar la actualización y proporcionar los datos |
| `PantallaActualizacionInventario` | Boundary | Capturar datos y mostrar validaciones |
| `ControlGestionInventario` | Control | Coordinar validación, registro y actualización |
| `Medicamento` | Entity | Proporcionar identidad y reglas del medicamento |
| `CentroSalud` | Entity | Proporcionar identidad y ámbito del centro |
| `InventarioActual` | Entity | Mantener la cantidad actual y estado del inventario |
| `RegistroInventario` | Entity | Representar la actualización histórica |

## Responsabilidades y restricciones

- El actor interactúa con la frontera, no directamente con entidades.
- La frontera captura y presenta; no contiene reglas de negocio.
- El control coordina el caso de uso.
- Las entidades representan información y reglas del dominio.
- Persistencia técnica y adaptadores se introducirán en el diseño, no en este VOPC.
