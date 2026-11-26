# DeepPharma

Sistema académico y experimental para gestionar inventario de medicamentos y
explorar la detección temprana de riesgo de desabastecimiento.

> **Estado:** línea base técnica del MVP autorizada. La validación académica e
> institucional y la integración real todavía están pendientes.

## Alcance provisional del MVP

- inventario por medicamento y centro de salud;
- validación e importación controlada de datos;
- baseline determinista de riesgo;
- alertas con ciclo de vida auditable;
- autenticación y RBAC;
- adaptador SALMI simulado.

El MVP incluye entrenamiento ML reproducible con datos sintéticos o públicos
autorizados. Fuera del MVP quedan los datos institucionales no autorizados y la
integración SALMI sin contrato técnico autorizado.

## Estado de Ingeniería de Software

El proyecto sigue RUP y UML 2.5.1 para los artefactos académicos y SDD para
refinar y gobernar la implementación:

```text
fuentes → contexto → requisitos → casos/escenarios → análisis/diseño
        → arquitectura → pruebas → spec/plan/tasks → Issues → implementación
```

No se deben crear tickets de implementación hasta cerrar y aprobar la línea
base documental.

## Navegación

- [`CONTEXT.md`](CONTEXT.md): contexto, alcance y reglas del repositorio.
- [`docs/README.md`](docs/README.md): índice de documentación.
- [`docs/engineering/refinement-baseline.md`](docs/engineering/refinement-baseline.md):
  checklist de cierre documental.
- [`docs/academic/rubric.md`](docs/academic/rubric.md): mínimos académicos.
- [`docs/requirements/`](docs/requirements/): requisitos, actores, casos y
  trazabilidad.
- [`docs/analysis/`](docs/analysis/): análisis, BCE/VOPC y auditorías.
- [`docs/design/`](docs/design/): diagramas UML editables y exportados.
- [`docs/architecture/`](docs/architecture/): arquitectura y vistas RUP.
- [`docs/adr/`](docs/adr/): decisiones arquitectónicas canónicas.
- [`docs/quality/`](docs/quality/): estrategia y catálogo de pruebas.
- [`docs/spec/`](docs/spec/): constitución, spec, plan y tareas SDD locales.
- [`apps/`](apps/): tracer bullet ejecutable.

## Tracer bullet local

### API

```bash
cd apps/api
export SECRET_KEY='use-a-local-secret-of-at-least-32-bytes'
uv sync
uv run alembic upgrade head
DEMO_PASSWORD='local-only-password' uv run python -m scripts.seed
uv run fastapi dev app/main.py
```

### Web

En otra terminal:

```bash
cd apps/web
bun install
bun run dev
```

La aplicación web espera la API en `http://localhost:8000`. Se puede cambiar
con `NEXT_PUBLIC_API_URL`.

## Validación local

```bash
cd apps/api && uv run pytest
cd apps/web && bun run lint && bun run build
```

Los resultados deben reportarse como evidencia de una ejecución concreta; no
se deben convertir en afirmaciones académicas o institucionales sin respaldo.

## Seguridad y datos

- No incluir `.env`, contraseñas, tokens ni datos institucionales.
- Usar únicamente datos sintéticos, públicos con licencia compatible o datos
  autorizados.
- La clave `SECRET_KEY` se configura fuera del repositorio.
- SALMI permanece simulado hasta disponer de un contrato autorizado.
