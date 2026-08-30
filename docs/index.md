# Centro de Analítica e Inteligencia Clínica - Hosvital HIS

Repositorio técnico y metodológico para el monitoreo del desempeño asistencial, la eficiencia en el ciclo de ingresos y la seguridad del paciente. Este portal centraliza las definiciones de métricas, reglas de negocio, modelos relacionales y criterios de auditoría aplicables sobre el sistema de información hospitalario.

---

## Arquitectura del Flujo de Información

```text
┌─────────────────────────────────────────────────────────────┐
│                    Hosvital HIS (RDBMS)                     │
│    Modelos Transaccionales: Capbas, Ingresos, TMPFAC, etc.  │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                 Capa de Extracción y Reglas                 │
│         Consultas T-SQL Optimizadas y Filtros de Negocio    │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                Visualización y Cuadros de Mando             │
│       Paneles de Gestión Asistencial, Quirúrgica y Financiera│
└─────────────────────────────────────────────────────────────┘
Catálogo de Módulos y Cuadros de Mando
Egresos Hospitalarios y Urgencias: Control de giro de cama, oportunidad de atención en urgencias y cálculo de estancia media (ALOS).

Prefacturación y Producción Asistencial: Trazabilidad de cargos asistenciales por contrato, balance de procedimientos frente a insumos y antigüedad de prefacturas.

Ocupación y Programación Quirúrgica: Trazabilidad de órdenes quirúrgicas, adherencia a salas, índice de cancelaciones y distribución por especialidad.

Calidad, Seguridad del Paciente e IAAS: Vigilancia de infecciones asociadas a la atención en salud, tasa por 100 camas-día y segmentación etaria.
