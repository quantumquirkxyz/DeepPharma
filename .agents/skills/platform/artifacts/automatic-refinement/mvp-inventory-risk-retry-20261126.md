# Automatic Refinement — Retry 2026-11-26

**Estado:** `blocked`
**Aprobación:** `not-approved`

## Veredicto

La crítica independiente devolvió `FAIL`. No es válido emitir
`refined-awaiting-review`.

## Bloqueadores principales

1. Las afirmaciones de pruebas previas no tienen registros archivados
   asociados a comandos, timestamps y resultados.
2. La línea base conserva checks pendientes.
3. La automatización Issue/PR/Project y la capacidad remota de sub-issues no
   están verificadas.
4. El runtime completo con loop ledger y handoffs de critic/verifier no está
   evidenciado.

## Correcciones aplicadas

- ADR-037 marcada como supersedida por ADR-054.
- Regla determinista de `idea` post-grill documentada.
- Contratos locales de Skills documentados.
- `status:needs-info` separado de `area:requirements`.
- Evidencia previa reclasificada como parcialmente archivada.

## Próximo consumidor

Una nueva ejecución de `automatic-refinement` después de resolver los
bloqueadores. No se autoriza `make-project`, `to-spec`, `to-tickets` ni
`implement` desde este artefacto.
