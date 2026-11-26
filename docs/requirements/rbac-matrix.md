# Matriz RBAC inicial

**Estado:** Propuesta pendiente de validación con stakeholders
**Versión:** 0.1
**Fuente:** Catálogo de actores y decisiones confirmadas en grill-with-docs

## 1. Propósito

Definir provisionalmente qué capacidades puede ejecutar cada actor humano. Esta matriz orienta requisitos, casos de uso y seguridad; no sustituye la validación de permisos institucionales.

## 2. Matriz de capacidades

| Capacidad | ACT-01 Administrador del sistema | ACT-02 Farmacéutico | ACT-03 Ingeniero ML | ACT-04 Evaluador SUS | ACT-05 Administrador de farmacia |
| --- | ---: | ---: | ---: | ---: | ---: |
| Cargar datos históricos | Sí | No | Sí | No | No |
| Entrenar modelos | No | No | Sí | No | No |
| Evaluar y registrar modelos | No | No | Sí | No | No |
| Consultar predicciones | Sí | Sí | Sí | No | Sí |
| Actualizar inventario | Configurable | Sí | No | No | Sí |
| Consultar inventario | Sí | Sí | Sí | No | Sí |
| Gestionar alertas | Sí | Sí | No | No | Sí |
| Ejecutar predicción bajo demanda | Sí | Configurable | Sí | No | Configurable |
| Configurar integraciones | Sí | No | No | No | No |
| Administrar usuarios | Sí | No | No | No | No |
| Evaluar usabilidad | No | Participa | No | Sí | Participa |

## 3. Reglas provisionales

- `ACT-01` administra configuración, usuarios e integraciones, pero no es responsable del entrenamiento científico de modelos.
- `ACT-03` administra el ciclo de entrenamiento y evaluación de modelos, pero no modifica inventario operativo.
- `ACT-02` es el actor principal de valor y puede actualizar inventario, consultar riesgos y gestionar alertas.
- `ACT-05` administra inventario y alertas dentro de su ámbito de farmacia.
- `ACT-04` coordina la evaluación SUS; la aplicación de la encuesta sigue siendo una actividad externa salvo que se defina un módulo específico.
- Las capacidades marcadas como `Configurable` requieren una decisión de autorización antes de convertirse en requisitos normativos.

## 4. Pendientes de validación

- Confirmar permisos reales por rol con stakeholders.
- Determinar si la ejecución manual de predicciones se permite al farmacéutico.
- Definir alcance de farmacia para `ACT-02` y `ACT-05`.
- Definir segregación de funciones para datos, modelos e inventario.
- Derivar requisitos de autorización y casos de prueba de seguridad.

## 5. Principio aceptado de seguridad

Todos los endpoints de datos requieren autenticación y autorización. Solo
health/readiness y token quedan fuera de la autorización de datos. Los roles y
ámbitos se aplican en backend y se deniega por defecto.

La consulta de auditoría también está protegida por rol y ámbito. Los usuarios
operativos solo consultan operaciones autorizadas; la auditoría completa queda
reservada a roles administrativos o de auditoría.
