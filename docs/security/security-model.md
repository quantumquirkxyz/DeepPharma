# Modelo de seguridad y privacidad

**Estado:** Propuesta; pendiente de validación institucional.

## Identidad y autorización

- OAuth2 Bearer/JWT para el tracer bullet.
- RBAC en backend, no solo en la interfaz.
- Separar rol de ámbito de centro de salud.
- Aplicar mínimo privilegio y denegar por defecto.
- Auditar cambios de roles, asignaciones y acciones sensibles.

## Datos

- No almacenar secretos en código, logs ni fixtures.
- Clasificar datos como sintéticos, públicos o institucionales autorizados.
- No usar datos institucionales hasta contar con autorización y retención
  aprobada.
- No presentar ausencia de datos como riesgo cero.

## Amenazas a revisar

- acceso cruzado entre centros;
- elevación de privilegios;
- tokens expirados o reutilizados;
- exposición de datasets;
- inyección en archivos importados;
- filtración en errores y logs;
- abuso de endpoints de evaluación.

## Evidencia requerida

- pruebas de autorización positiva y negativa;
- revisión de secretos;
- pruebas de alcance por centro;
- política de retención aprobada;
- registro de incidentes y respuesta.
