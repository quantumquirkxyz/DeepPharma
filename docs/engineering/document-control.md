# Control documental

**Estado:** Activo
**Responsable técnico:** equipo DeepPharma
**Autoridad de fuentes:** `docs/sources/source-register.md`

## Estados permitidos

- `Borrador`: contenido en elaboración.
- `Propuesta`: decisión o artefacto sujeto a revisión.
- `Aceptada`: decisión autorizada para el MVP.
- `Ejecutada`: evidencia producida por una ejecución reproducible.
- `Archivada`: documento histórico reemplazado.

## Reglas

1. Todo documento declara versión, estado, fuente y alcance.
2. Una propuesta no se presenta como cumplimiento.
3. Una prueba diseñada no se presenta como prueba ejecutada.
4. Una decisión institucional requiere fuente o responsable externo.
5. Un ADR reemplazado debe apuntar al ADR sucesor.
6. Cambios de requisitos actualizan casos, trazabilidad, arquitectura y
   pruebas afectadas.
7. Los documentos académicos oficiales conservan su autoridad sobre las
   extensiones profesionales.

## Mapa de autoridad

| Artefacto | Autoridad |
|---|---|
| Rúbrica y mínimos | documentos académicos oficiales |
| Requisitos y casos | `docs/requirements/` después de aprobación |
| Decisiones técnicas | `docs/adr/` |
| Contexto vigente | `CONTEXT.md` |
| Pruebas y evidencia | `docs/quality/` |
| SDD | `docs/spec/` |
| Estado de refinamiento | `docs/engineering/` |

## Revisión

La revisión de línea base debe comprobar que no existan documentos
contradictorios, referencias muertas, estados falsamente aprobados ni
resultados sin evidencia.
