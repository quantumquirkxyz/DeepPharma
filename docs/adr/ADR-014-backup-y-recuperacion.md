# ADR-014 — Backup y recuperación verificable

**Estado:** Aceptada como diseño; objetivos numéricos pendientes
**Fecha:** 2026-11-25
**Decisor:** Propietario del proyecto

## Decisión

El sistema debe diseñar backup, restauración verificada y recuperación ante
fallos. Cada entorno definirá RPO/RTO, retención, cifrado, acceso y pruebas de
restauración. Un backup no se considera válido hasta comprobar que puede
restaurarse.

## Consecuencias

- La operación debe conservar evidencia de backups y restauraciones.
- Las pruebas de recuperación no deben modificar datos productivos sin
  autorización.
- El MVP local tendrá un procedimiento documentado, sin presentarlo como
  capacidad productiva.
