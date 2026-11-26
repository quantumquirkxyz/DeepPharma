# ADR-031 — Acceso restringido a auditoría

**Estado:** Aceptada para MVP
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

La auditoría se protege mediante rol y ámbito:

- un farmacéutico consulta únicamente el historial de operaciones autorizadas;
- administradores o auditores consultan la auditoría completa de su ámbito;
- ningún usuario puede modificar ni eliminar eventos;
- las consultas de auditoría también generan trazabilidad.

El acceso administrativo concreto por centro queda sujeto a las asignaciones
institucionales pendientes.

## Consecuencias

- La auditoría no se convierte en una fuente de exposición lateral de datos.
- Las pruebas deben cubrir lectura fuera de ámbito y rol insuficiente.
- El sistema debe distinguir auditoría operativa de logs técnicos.
