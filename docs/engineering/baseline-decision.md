# Decisión de línea base de Ingeniería de Software

**Fecha:** 2026-11-25
**Estado:** Borrador para grill-with-docs; no aprobado
**Autoridad:** propietario del proyecto y documentación académica registrada

## Decisión

Este documento propone una línea base técnica para discusión. No afirma que
existan datos institucionales, resultados ML, integración SALMI real ni
evidencia SUS.

## Decisiones técnicas cerradas

- RUP y UML 2.5.1 para el paquete académico.
- SDD para spec, plan, tareas y verificación.
- Monolito modular en capas para el MVP.
- FastAPI/SQLAlchemy/Alembic para API y persistencia.
- Next.js/TypeScript para frontend.
- Alembic como autoridad única de esquema.
- Stock entero no negativo en unidades para el MVP.
- Validación antes de aplicar datos.
- Datasets inmutables por versión.
- Pipeline ML reproducible con datos sintéticos/públicos autorizados.
- Variable objetivo ML basada en riesgo futuro simulado, no en el umbral del
  fallback.
- Fallback ML explícito, determinista y auditable ante indisponibilidad del
  modelo.
- Linaje completo de cada resultado de riesgo y no recalculación silenciosa de
  históricos.
- Monitoreo ML de calidad, distribución y deriva con fixtures sintéticos de
  cambio controlado.
- Reproducibilidad completa de experimentos ML mediante código, dependencias,
  semilla, configuración, datos y entorno.
- Explicabilidad operativa con limitaciones explícitas, sin afirmar causalidad
  ni justificación clínica.
- Revisión humana obligatoria para cualquier acción posterior a un resultado de
  riesgo o alerta.
- Auditoría append-only de eventos de dominio y decisiones humanas con
  integridad verificable.
- Acceso a auditoría restringido por rol y ámbito.
- Dataset fuente completo restringido y proyección operativa mínima.
- Protección de originales con cifrado, mínimo privilegio, auditoría y
  rotación de credenciales.
- Respuesta documentada ante incidentes de datos, con contención y
  preservación de evidencia.
- Kill switch y rollback auditables para modelo, notificaciones e integraciones.
- Taxonomías separadas de prioridad y riesgo para work items.
- Cadena Parent Spec/Sub-Spec/Ticket unificada bajo `area:requirements`.
- Relaciones Parent Spec → Sub-Spec → Ticket representadas mediante
  sub-issues nativos obligatorios.
- Milestones usados como entregas, no como fases ni sustitutos de jerarquía.
- Labels como metadata común entre Issues, PRs y Project, con sincronización
  documentada del Status.
- Sincronización Status/labels mediante automatización verificable, no
  asumida por GraphQL.
- `status:needs-info` separado de `area:requirements`, con `status:blocked`
  transversal.
- Readiness jerárquico desde Parent Spec hasta Ticket ejecutable.
- Especificación por niveles: Parent Spec aprobado, luego Sub-Spec aprobado,
  luego Tickets mediante `to-tickets`.
- Orden remoto: Project, Milestones, Parent Specs, Sub-Specs y finalmente
  Tickets.
- Project objetivo `DeepPharma — MVP` sobre `quantumquirkxyz/DeepPharma`;
  privado inicialmente y con creación remota pendiente.
- Partición inicial en cinco Milestones: baseline/gobierno, datos/inventario,
  riesgo ML/fallback, alertas/auditoría/notificaciones y
  seguridad/operación/verificación.
- Contrato uniforme de labels para Parent Specs, Sub-Specs, Tickets y PRs.
- Dependencias nativas `blocked_by` explícitas y separadas de la jerarquía.
- Trazabilidad controlada Ticket → rama `issue/<number>-<slug>` → PR.
- Tracker y PRs en inglés; documentación académica y técnica existente puede
  conservar el español.
- Labels como fuente canónica de tipos, con Issue Types nativos solo si son
  compatibles sin duplicación semántica.

El diseño consolidado del tracker se encuentra en
`docs/engineering/tracker-design.md`.
- Baseline determinista versionado `baseline-rules-1` como fallback y
  referencia.
- Ciclo ML con estados `ENTRENADO`, `EVALUADO`, `APROBADO` y `RETIRADO`.
- Alertas separadas de predicciones.
- RBAC separado de ámbito de centro.
- SALMI detrás de puerto y adaptador.
- Jobs como seam para procesamiento pesado futuro.
- Evidencia ejecutada separada de casos diseñados.
- Pruebas unitarias, integración, sistema y aceptación con trazabilidad.
- Despliegue local reproducible mediante Docker/Compose.
- Observabilidad productiva diseñada y recuperación con backup/restauración
  verificable.
- Notificaciones mediante adaptador simulado e idempotente.
- Retención provisional de fixtures sintéticos durante desarrollo/evaluación,
  con eliminación documentada; retención institucional pendiente.
- Rendimiento definido como benchmark reproducible; SLO numéricos pendientes
  de entorno representativo y medición.
- SUS definido como evaluación académica separada, sujeta a protocolo y
  evidencia de ejecución.

## Decisiones externas pendientes

- permisos institucionales por centro;
- fuente y licencia de datos históricos;
- definición institucional de desabastecimiento;
- fórmula de consumo y días de cobertura;
- protocolo, muestra y resultado SUS;
- contrato SALMI;
- retención de datos institucionales;
- objetivos de rendimiento medidos.

Estas decisiones permanecen en `docs/requirements/clarifications.md`.

## Criterio de cierre

El refinamiento documental se cerrará mediante
`docs/engineering/baseline-closure-checklist.md`. El cierre requiere
consistencia documental y no permite convertir pruebas no ejecutadas ni
decisiones externas pendientes en evidencia o aprobación.
