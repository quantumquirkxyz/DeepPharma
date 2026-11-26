# Backup y recuperación

**Estado:** Diseño aceptado; parámetros del entorno pendientes.

## Requisitos

- backup de base de datos y artefactos ML;
- cifrado y control de acceso;
- retención documentada;
- restauración probada;
- registro de fecha, versión, operador y resultado;
- separación entre datos sintéticos y datos institucionales.

## Evidencia mínima

1. crear backup;
2. restaurar en entorno aislado;
3. ejecutar migraciones compatibles;
4. verificar health checks y datos esperados;
5. registrar resultado y limitaciones.

Los valores RPO/RTO se determinarán por entorno y no se inventan en la fase
académica.
