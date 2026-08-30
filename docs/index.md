# Portal de Documentación BI - Hosvital HIS & Superset

Bienvenido al repositorio central de documentación técnica, operativa y funcional de los tableros analíticos institucionales desarrollados sobre **Microsoft SQL Server (HVT_REDHUMANA)** y desplegados en **Apache Superset**.

---

## Estructura del Ecosistema

``text
[ Hosvital HIS (SQL Server) ]
             │
             │ (Consultas SQL Optimizadas / Vistas)
             ▼
[ Datasets Físicos / Virtuales en Superset ]
             │
             │ (Métricas Agregadas / Filtros Globales)
             ▼
[ Tableros de Control Asistenciales, Financieros y Quirúrgicos ]
Módulos Documentados
Egresos Hospitalarios y Urgencias: Rotación de giro de cama, oportunidad de triage y promedio de estancia (ALOS).

Prefacturación y Producción Asistencial: Trazabilidad de cargos asistenciales en tablas temporales (TMPFAC) y envejecimiento de cuentas.

Órdenes Quirúrgicas y Programación: Trazabilidad del ciclo de vida quirúrgico, tasas de cancelación y uso de quirófanos.

Vigilancia Epidemiológica e IAAS: Presión infecciosa intrahospitalaria, índice por 100 camas-día y mapas de calor etarios.