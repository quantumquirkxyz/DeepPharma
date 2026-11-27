# Validación de procedencia de artefactos

Esta seam valida que un artefacto JSON fue construido a partir de las fuentes
declaradas y que esas fuentes no cambiaron después de producirlo. Es una
validación de integridad y trazabilidad; no certifica la calidad del contenido,
la validez clínica ni una integración institucional.

## Contrato mínimo

El artefacto debe incluir:

```json
{
  "sourceArtifacts": ["docs/requirements/example.md"],
  "sourceDigests": {
    "docs/requirements/example.md": "sha256:<64 lowercase hexadecimal characters>"
  }
}
```

Cada referencia debe ser una ruta relativa al repositorio. La ruta no puede
escapar de la raíz mediante `..`, debe existir como archivo regular y debe tener
una entrada correspondiente en `sourceDigests`. El validador calcula SHA-256
sobre los bytes actuales y compara el resultado con el digest declarado.

## Uso

Desde la raíz del repositorio:

```bash
python3 -m json.tool .agents/skills/platform/artifacts/requirements/mvp-inventory-risk-final.json
python3 .agents/skills/platform/artifacts/validate_provenance.py \
  .agents/skills/platform/artifacts/requirements/mvp-inventory-risk-final.json \
  --root . \
  --report .agents/skills/platform/artifacts/provenance/validation-report.json
```

El comando devuelve código `0` únicamente cuando todas las referencias pasan.
Los estados `invalid` y `failed` se conservan en la salida y en el reporte,
para que un fallo parcial sea auditable y no se confunda con una ejecución
exitosa.

## Trazabilidad y límites

- Requisito: Parent Spec #2 → Sub-Spec #7 → Ticket #25.
- Criterios: AC-01–AC-14, específicamente integridad de artefactos, estado de
  validación y evidencia reproducible.
- Evidencia esperada: `validation-report.json` y la salida de
  `python3 -m json.tool`.
- Fuera de alcance: refactorizaciones no relacionadas, datos institucionales,
  certificación de producción, afirmaciones clínicas y modificaciones de
  artefactos cuando la validación falla.
- Riesgo residual: SHA-256 prueba integridad accidental o deliberada del
  contenido, pero no demuestra quién produjo el artefacto ni que la fuente sea
  correcta. La firma/autenticación del productor queda fuera de este slice.
