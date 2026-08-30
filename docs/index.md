# Centro de Analítica e Inteligencia Clínica - Hosvital HIS

Repositorio central de documentación técnica, operativa y funcional de los cuadros de mando institucionales orientados al monitoreo del ciclo asistencial, la optimización financiera y la seguridad del paciente.

---

## Matriz General de Cuadros de Mando

| Área de Gestión | Cuadro de Mando | Indicadores Principales | Frecuencia de Actualización | Enlace al Manual |
| :--- | :--- | :--- | :--- | :--- |
| **Gestión Asistencial** | **Egresos y Urgencias** | Estancia Media (ALOS), Tasa de Ocupación, Rotación de Camas | 15 Minutos | [Ver Ficha Técnica](dashboards/01-egresos-urgencias.md) |
| **Gestión Asistencial** | **Calidad, Seguridad e IAAS** | Tasa de Infecciones x 100 Camas-Día, Aislamiento por Pabellón | 15 Minutos | [Ver Ficha Técnica](dashboards/04-vigilancia-iaas.md) |
| **Gestión Financiera** | **Prefacturación y Producción** | Valor WIP en Tránsito, Aging de Prefactura, Consumos por EPS | 10 Minutos | [Ver Ficha Técnica](dashboards/02-prefacturacion.md) |
| **Gestión Quirúrgica** | **Programación y Ocupación QX** | Tasa de Cancelación, Oportunidad Quirúrgica, Demanda por Especialidad | 5 Minutos | [Ver Ficha Técnica](dashboards/03-ordenes-quirurgicas.md) |

---

## Flujo del Modelo de Información

```text
┌─────────────────────────────────────────────────────────────────────────┐
│                     HOSVITAL HIS - CAPA TRANSACCIONAL                   │
│  Tablas Núcleo: Ingresos, Capbas, TMPFAC, procir, HCDIAGN, MAEDIA       │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    CAPA DE TRANSFORMACIÓN Y REGLAS T-SQL                │
│  • Tratamiento de fechas centinela (1753-01-01)                         │
│  • Filtro de anulaciones operativas (tfestaanu = 'N')                   │
│  • Consolidación multirubro y cálculo de tiempos asistenciales          │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                     CAPA DE EXPLOTACIÓN Y DECISIÓN                      │
│  Cuadros de mando con filtros interactivos, KPIs y consolas operativas  │
└─────────────────────────────────────────────────────────────────────────┘
Estándares Técnicos y de Gobierno del Dato
Tratamiento de Nulos y Fechas Centinela: Todas las consultas analíticas aíslan valores no inicializados del motor relacional (<= 1753-01-01) para evitar distorsiones en los cálculos de estancia y oportunidad.

Integridad de Transacciones Válidas: Se aplican filtros estrictos de no anulación en los módulos financieros (TMPFAC1.tfestaanu1 = 'N' y TMPFAC2.TFestaanu2 = 'N') y de trazabilidad en cancelaciones de sala (PFcHrCnc).

Seguridad y Confidencialidad: El acceso a los manuales y tableros está segmentado según el rol operativo (Dirección Médica, Coordinación Quirúrgica, Auditoría de Cuentas y Comité de Infecciones).