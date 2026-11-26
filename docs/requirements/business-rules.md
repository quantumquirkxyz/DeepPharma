# Reglas de negocio

**Versión:** 0.1
**Estado:** Propuesta de línea base
**Fuente:** contexto de DeepPharma, casos de uso y glosario

| ID | Regla | Estado |
|---|---|---|
| RN-01 | Solo se incorporan fuentes autorizadas. | Aceptada para MVP; ADR-021 |
| RN-02 | Cada conjunto conserva procedencia, versión y fecha. | Aceptada para MVP; ADR-002/008 |
| RN-03 | Un conjunto no validado no puede utilizarse para entrenamiento. | Aceptada para MVP; ADR-002 |
| RN-04 | Las correcciones de datos crean una nueva versión. | Aceptada para MVP; ADR-008 |
| RN-05 | Un modelo entrenado no es automáticamente un modelo aprobado. | Aceptada para MVP; ADR-009 |
| RN-06 | La evaluación debe respetar el orden temporal de los datos. | Aceptada para MVP; ADR-017 |
| RN-07 | Una predicción y una alerta operativa son conceptos distintos. | Aceptada para MVP; ADR-003 |
| RN-08 | La ausencia de datos no equivale a riesgo cero. | Propuesta |
| RN-09 | Los umbrales de 10 y 20 días son hipótesis hasta ser validados. | Hipótesis |
| RN-10 | Una actualización de inventario conserva historial y procedencia. | Aceptada para MVP; ADR-002 |
| RN-11 | Las cantidades negativas no son válidas. | Aceptada para MVP; ADR-002 |
| RN-12 | Las transiciones de alertas deben seguir una máquina de estados aprobada. | Aceptada para MVP; ADR-018 |
| RN-13 | Reconocer una alerta no equivale a resolverla. | Aceptada para MVP; ADR-018 |
| RN-14 | Una notificación enviada no equivale a una alerta atendida. | Aceptada para MVP; ADR-019 |
| RN-15 | SALMI se integra mediante un adaptador y contrato autorizado. | Aceptada para MVP; ADR-004 |
| RN-16 | Los datos simulados deben identificarse como simulados. | Aceptada para MVP; ADR-021 |
| RN-17 | Los permisos se aplican por rol y ámbito. | Aceptada como principio; ADR-006 |
| RN-18 | Un usuario no puede elevar sus propios privilegios. | Aceptada como principio; ADR-020 |
| RN-19 | Las versiones retiradas de modelos conservan su historial. | Aceptada para MVP; ADR-009 |
| RN-20 | Los resultados históricos no se modifican silenciosamente al cambiar un modelo. | Aceptada para MVP; ADR-009 |
| RN-21 | Los datos públicos, sintéticos e institucionales se distinguen. | Aceptada para MVP; ADR-021 |
| RN-22 | Una explicación de ML no demuestra causalidad. | Aceptada para MVP; ADR-003 |

Las reglas marcadas como propuesta requieren revisión de stakeholders antes de convertirse en línea base.
