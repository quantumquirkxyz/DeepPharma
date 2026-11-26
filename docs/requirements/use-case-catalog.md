# Catálogo de casos de uso

**Versión:** 0.1
**Estado:** Catálogo provisional en refinamiento; no aprobado
**Fuente:** `SRC-01`, `SRC-04`, `SRC-05` y decisiones de grill-with-docs

## Casos de uso académicos base

| ID | Nombre | Clasificación | Estado |
|---|---|---|---|
| CU-01 | Registrar datos históricos de inventario | Funcional principal | Especificación en refinamiento |
| CU-02 | Entrenar y evaluar modelos de aprendizaje automático | Funcional principal | Especificación en refinamiento |
| CU-03 | Generar predicciones de riesgo de desabastecimiento | Funcional principal | Especificación en refinamiento |
| CU-04 | Visualizar y gestionar alertas priorizadas | Funcional principal | Especificación en refinamiento |
| CU-05 | Gestionar inventario en tiempo real | Funcional principal | Especificación en refinamiento |
| CU-06 | Evaluar usabilidad del sistema mediante escala SUS | Académico / validación externa | Especificación académica en refinamiento |

## Casos de uso adicionales candidatos

Los casos siguientes amplían el modelo sin renumerar ni modificar los seis casos académicos base:

| ID | Nombre | Actor principal | Estado |
|---|---|---|---|
| CU-07 | Validar datos de inventario | Administrador del sistema / Ingeniero ML | Candidato |
| CU-08 | Preprocesar datos históricos | Ingeniero ML | Candidato |
| CU-09 | Sincronizar inventario con fuente externa | Administrador del sistema | Candidato |
| CU-10 | Evaluar modelos predictivos | Ingeniero ML | Candidato |
| CU-11 | Registrar modelo aprobado | Ingeniero ML | Candidato |
| CU-12 | Consultar explicación de una predicción | Farmacéutico / Ingeniero ML | Candidato |
| CU-13 | Consultar inventario actual | Farmacéutico / Administrador de farmacia | Candidato |
| CU-14 | Consultar detalle de alerta | Farmacéutico / Administrador de farmacia | Candidato |
| CU-15 | Reconocer o gestionar una alerta | Farmacéutico / Administrador de farmacia | Candidato |
| CU-16 | Notificar riesgo crítico | Servicio de correo/notificaciones | Candidato |
| CU-17 | Generar reportes de inventario y riesgo | Administrador de farmacia | Candidato |
| CU-18 | Administrar usuarios y roles | Administrador del sistema | Candidato |
| CU-19 | Configurar fuentes e integraciones | Administrador del sistema | Candidato |

## Reglas de nomenclatura

- Los identificadores son estables y no se reutilizan.
- Los nombres expresan objetivos mediante verbo en infinitivo.
- Los refinamientos internos no cambian el identificador del caso de uso de alto nivel.
- Los escenarios usarán `ESC-CUxx-nn`.
- Los diagramas usarán el prefijo correspondiente al tipo de modelo.
- Los casos de uso se especificarán con la plantilla RUP registrada como `SRC-07`.

## Clasificación de CU-06

`CU-06` se conserva para cumplir el mínimo académico de seis especificaciones. Se documentará con flujo, escenarios y trazabilidad, pero no se incluirá como funcionalidad operativa principal de DeepPharma salvo que se apruebe un requisito explícito para implementar un módulo SUS.

## Dependencias preliminares

- `CU-01` proporciona datos para `CU-02`.
- `CU-02` produce modelos aprobados para `CU-03`.
- `CU-03` produce predicciones que alimentan `CU-04`.
- `CU-05` proporciona datos operativos para `CU-03` y puede recibir acciones derivadas de `CU-04`.
- `CU-06` evalúa el producto y sus interfaces, no el proceso operativo de inventario.
- Los casos `CU-07` a `CU-19` solo se consolidarán después de verificar que tienen objetivo propio y no son pasos internos de los casos base.
