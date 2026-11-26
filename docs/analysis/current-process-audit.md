# Auditoría del proceso actual de inventario y reposición

**Versión:** 0.1
**Estado:** Modelo hipotético académico aprobado provisionalmente
**Fecha:** 2026-11-25

## 1. Objetivo

Determinar qué partes del proceso actual de gestión de medicamentos pueden modelarse como hechos respaldados y cuáles siguen siendo supuestos.

Este documento precede a la aprobación de `UC-BUSINESS-CURRENT-01.puml`.

## 2. Evidencia revisada

| Fuente | Evidencia útil | Limitación |
|---|---|---|
| Contexto inicial de DeepPharma | Describe uso de Excel, sistemas semi-digitales, SALMI, reposición y escenarios de falta | Documento del proyecto; no prueba el procedimiento institucional real |
| `Cap. 1 Refinamiento...pptx` | Define casos de uso, actores, flujos y requisitos | Material metodológico; no describe MINSA/CSS |
| `Capitulo 2. Análisis y Diseño...pptx` | Define modelado de análisis, BCE y realización | Material metodológico; no describe el proceso operativo |
| `TrabajoFinal ISA-2s26.docx` | Define entregables académicos | No constituye evidencia del proceso MINSA/CSS |
| `PlanIS-2sem2026.docx` | Define plan y evaluación de la asignatura | No constituye evidencia del proceso operativo |

## 3. Hechos actualmente respaldados

- El problema del proyecto es el riesgo de desabastecimiento de medicamentos.
- DeepPharma pretende trabajar con inventario, predicciones y alertas.
- El proyecto distingue datos históricos e inventario actual.
- SALMI aparece como sistema existente o integración objetivo en el material del proyecto.
- El modelo propuesto debe distinguir el sistema DeepPharma de sistemas externos.

## 4. Supuestos no aprobados

Los siguientes elementos aparecen en el diagrama preliminar, pero no están respaldados por una fuente institucional o entrevista registrada:

- El farmacéutico registra directamente todas las existencias.
- El administrador de farmacia tiene responsabilidades distintas al farmacéutico.
- Existe un almacén central involucrado en el flujo modelado.
- Existe un proveedor o proceso de compras con esa interacción exacta.
- El paciente participa directamente en el proceso de reposición.
- SALMI registra o consulta exactamente las operaciones dibujadas.
- La solicitud de reposición sigue el flujo representado.
- La aprobación de compras y la recepción física ocurren como se dibujaron.

Estos elementos deben permanecer como hipótesis y no como hechos del negocio.

## 5. Vacíos de información

Para aprobar el proceso actual se necesita confirmar:

1. Actores y cargos reales que registran inventario.
2. Sistema o documento utilizado en cada paso.
3. Frecuencia y responsable de cada registro.
4. Datos obligatorios y validaciones actuales.
5. Quién detecta el stock bajo.
6. Quién inicia, revisa y autoriza la reposición.
7. Participación del almacén central.
8. Participación de proveedores y compras.
9. Participación real de SALMI.
10. Tratamiento de inventario agotado.
11. Flujo de recepción y actualización de existencias.
12. Evidencia disponible para cada paso.

## 6. Criterio de aprobación

El modelo `UC-BUSINESS-CURRENT-01.puml` solo podrá convertirse en línea base cuando cada actor, actividad y relación tenga:

- fuente;
- responsable confirmado;
- entrada;
- salida;
- sistema o documento utilizado;
- condición de inicio;
- condición de finalización;
- validación de un stakeholder o fuente institucional.

## 7. Supuestos académicos provisionales

| ID | Supuesto | Impacto |
|---|---|---|
| ASM-01 | El farmacéutico registra o consulta existencias del centro | Define el punto de entrada operativo |
| ASM-02 | El administrador de farmacia supervisa inventario y reposición | Define responsabilidades administrativas |
| ASM-03 | Un almacén central participa en la reposición | Define la salida del proceso |
| ASM-04 | Un proveedor o proceso de compras interviene cuando se solicita reposición | Define una dependencia externa |
| ASM-05 | SALMI u otro sistema existente puede apoyar el registro de inventario | Mantiene la integración como hipótesis |
| ASM-06 | El paciente recibe el impacto del desabastecimiento, pero no gestiona la reposición | Evita modelarlo como actor operativo sin evidencia |

Estos supuestos solo sirven para construir y discutir el modelo académico. Cada uno debe validarse o reemplazarse antes de declarar que el modelo representa el proceso institucional real.

## 8. Condiciones de reemplazo

Cuando aparezca evidencia real, se deberá:

1. identificar el supuesto afectado;
2. registrar la fuente;
3. actualizar actores y actividades;
4. revisar casos de uso derivados;
5. actualizar requisitos y trazabilidad;
6. revisar diagramas y escenarios;
7. registrar el cambio;
8. ejecutar las pruebas afectadas.

## 9. Estado del diagrama actual

`UC-BUSINESS-CURRENT-01.puml` queda como:

> **Modelo hipotético académico provisional, pendiente de validación institucional.**

Puede utilizarse para avanzar en el ejercicio académico, pero no debe presentarse como afirmación del proceso real.
