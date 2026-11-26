# Escenarios de calidad arquitectónica

**Versión:** 0.1
**Estado:** Escenarios propuestos; objetivos pendientes de aprobación y medición
**Fuente:** requisitos no funcionales, `SRC-11`, `SRC-12`, `SRC-14`

| ID | Atributo | Fuente del estímulo | Estímulo | Entorno | Respuesta | Medida |
|---|---|---|---|---|---|---|
| QA-01 | Rendimiento | Administrador | Carga un conjunto estándar | Entorno local documentado | El sistema registra y valida el conjunto | Tiempo medido contra RNF-01 |
| QA-02 | Rendimiento | Scheduler | Inicia inferencia diaria | Datos válidos y modelo habilitado | Se procesan las entidades y se registran resultados | Tiempo medido contra RNF-03 |
| QA-03 | Disponibilidad | Fuente externa | SALMI no responde | Sincronización activa | Se conserva último estado válido y se registra fallo | Cero pérdida silenciosa |
| QA-04 | Seguridad | Usuario | Solicita datos fuera de su ámbito | Sistema operativo | Se rechaza acceso sin revelar datos | 100% de casos no autorizados rechazados |
| QA-05 | Auditabilidad | Administrador | Cambia un rol o integración | Configuración activa | Se registra actor, fecha y cambio | 100% de cambios auditables |
| QA-06 | Reproducibilidad | Ingeniero ML | Repite experimento | Mismo dataset y configuración | Produce resultado comparable | Configuración y versión completas |
| QA-07 | Modificabilidad | Equipo | Sustituye adaptador SALMI | Código de dominio estable | El dominio no requiere cambios | Pruebas de contrato aprobadas |
| QA-08 | Integridad | Farmacéutico | Registra cantidad inválida | Formulario activo | Se rechaza sin alterar inventario | 100% de entradas inválidas controladas |
| QA-09 | Trazabilidad | Auditor | Consulta una alerta | Datos históricos disponibles | Se identifica modelo, predicción y fuente | Cadena completa verificable |
| QA-10 | Usabilidad | Farmacéutico | Consulta alertas críticas | Prototipo o MVP | Encuentra y comprende la información | Evidencia SUS y tareas definidas |
| QA-11 | Observabilidad | Operador | Ocurre un error de integración | Entorno operativo | Se correlaciona y diagnostica el fallo | `traceId`, log y runbook |
| QA-12 | Seguridad | Auditor | Se intenta acceso fuera del ámbito | Sistema operativo | Se rechaza y audita la operación | Evento correlacionado y sin filtración |

## Reglas

- Cada escenario debe derivar de uno o más `RNF-*`.
- La medida debe poder ejecutarse o documentarse.
- Los objetivos aún no medidos no se presentan como cumplidos.
- Los escenarios de calidad guían arquitectura y pruebas.
