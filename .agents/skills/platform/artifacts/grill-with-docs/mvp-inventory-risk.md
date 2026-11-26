# Grill-with-docs — MVP de inventario y riesgo

## Resultado

El alcance confirmado cubre inventario, validación/importación de datos,
predicción ML reproducible, fallback baseline, alertas auditables, RBAC y
adaptador SALMI simulado.
El ML reproducible con datos sintéticos o públicos autorizados forma parte del
MVP. Los datos institucionales no autorizados y la integración SALMI real quedan
fuera del MVP.

## Decisiones

- Las cargas inválidas no modifican el inventario.
- Los conjuntos son inmutables y conservan procedencia, versión y estado.
- Si el modelo ML falla o está retirado, se usa `baseline-rules-1` como
  `FALLBACK_DETERMINISTA` y se registra la degradación.
- Los fixtures sintéticos se conservan durante desarrollo/evaluación y pueden
  eliminarse mediante una operación documentada.
- La planificación SDD queda en `docs/spec/`.
- El diseño de tracker está consolidado en
  `docs/engineering/tracker-design.md`: Project privado, cinco Milestones,
  jerarquía nativa de sub-issues y contrato uniforme de labels.

## Riesgos residuales

- Falta contrato SALMI autorizado.
- Falta dataset institucional autorizado para una evolución posterior.
- Deben medirse límites de tamaño y rendimiento.
- Falta definir retención institucional.
- Falta ejecutar la prueba de degradación y recuperación del fallback ML.

## Próximo consumidor

El siguiente consumidor correcto es `automatic-refinement`, que debe producir
un `RefinementArtifact` en estado `refined-awaiting-review`. Después de la
revisión explícita del refinamiento, el flujo continuará con
`make-project`, `to-spec`, Sub-Specs y `to-tickets`.

- `docs/spec/constitution.md`
- `docs/spec/mvp-inventory-risk.md`
- `docs/spec/plan-mvp-inventory-risk.md`
- `docs/spec/tasks-mvp-inventory-risk.md`
