# Gestión Financiera y Cartera

Módulo analítico orientado al control del ciclo de ingresos hospitalarios, auditoría médica de cuentas, trazabilidad del riesgo financiero y optimización del flujo de caja institucional frente a las entidades responsables de pago (EPS / EAPB).

---

## Tableros de Control Disponibles

| Cuadro de Mando | Enfoque Operativo / Analítico | Frecuencia de Corte | Enlace Directo |
| :--- | :--- | :---: | :--- |
| **Prefacturación y Producción** | Monitoreo de consumos en tránsito, cargos sin liquidar y cuentas de pacientes hospitalizados en curso. | Turno / 8 Horas | [Abrir Cuadro de Mando](../dashboards/02-prefacturacion.md) |
| **Facturación y WIP Post-Alta** | Control del trabajo en proceso (Work In Process), rezago de radicación tras alta médica y cumplimiento de términos de ley. | 12 Horas | [Abrir Cuadro de Mando](../dashboards/12-consola-facturacion-wip.md) |
| **Consola de Glosas y Devoluciones** | Gestión de objeciones normativas, efectividad de recobro, pérdidas asumidas y mesas de conciliación. | 24 Horas | [Abrir Manual de Usuario](../guia-usuario.md) |

---

## Indicadores Clave del Ciclo de Ingresos

* **Días de Facturación en Tránsito (WIP):** Tiempo promedio transcurrido entre el egreso médico del paciente y la generación formal de la factura electrónica.
* **Índice de Glosa Inicial:** Proporción económica objetada por los pagadores sobre el total de la facturación radicada en el periodo:
  Out-Null\% \text{ Glosa Inicial} = \left(\frac{\text{Valor Glosado}}{\text{Valor Radicado}}\right) \times 100Out-Null
* **Efectividad de Recuperación:** Capacidad de respuesta técnica y jurídica para levantar montos objetados:
  Out-Null\% \text{ Efectividad} = \left(\frac{\text{Valor Levantado}}{\text{Valor Glosado}}\right) \times 100Out-Null
