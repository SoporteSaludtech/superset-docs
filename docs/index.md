# Centro de Analítica e Inteligencia Clínica - Hosvital HIS

Repositorio central de documentación técnica, operativa y funcional de los cuadros de mando institucionales orientados al monitoreo del ciclo asistencial, la optimización financiera y la seguridad del paciente.

---

## Matriz General de Cuadros de Mando

| Área de Gestión | Cuadro de Mando | Indicadores Principales | Frecuencia | Enlace al Manual |
| :--- | :--- | :--- | :--- | :--- |
| **Gestión Asistencial** | **Egresos y Urgencias** | Estancia Media (ALOS), Tasa de Ocupación, Rotación de Camas | 15 Minutos | [Ver Ficha Técnica](dashboards/01-egresos-urgencias.md) |
| **Gestión Asistencial** | **Calidad, Seguridad e IAAS** | Tasa de Infecciones x 100 Camas-Día, Aislamiento por Pabellón | 15 Minutos | [Ver Ficha Técnica](dashboards/04-vigilancia-iaas.md) |
| **Gestión Financiera** | **Prefacturación y Producción** | Valor WIP en Tránsito, Aging de Prefactura, Consumos por EPS | 10 Minutos | [Ver Ficha Técnica](dashboards/02-prefacturacion.md) |
| **Gestión Quirúrgica** | **Programación y Ocupación QX** | Tasa de Cancelación, Oportunidad Quirúrgica, Demanda por Especialidad | 5 Minutos | [Ver Ficha Técnica](dashboards/03-ordenes-quirurgicas.md) |

---

## Flujo del Modelo de Información

=== "1. Capa Transaccional (Origen)"
    **Hosvital HIS - Motor Relacional SQL Server**
    
    * **Entidades Principales:** `Ingresos`, `Capbas`, `TMPFAC`, `procir`, `HCDIAGN`, `MAEDIA`.
    * **Naturaleza del Dato:** Registro transaccional en tiempo real derivado de la operación clínica, admisión de pacientes, programación quirúrgica y facturación médica.

=== "2. Capa de Transformación y Reglas"
    **Ingeniería de Datos y Consultas T-SQL**
    
    * **Tratamiento de Fechas:** Aislamiento de valores centinela por omisión (`<= 1753-01-01`).
    * **Filtros de Integridad:** Depuración de anulación de cargos (`tfestaanu = 'N'`) y trazabilidad de cancelaciones (`PFcHrCnc`).
    * **Métricas Asistenciales:** Cálculo dinámico de estancias acumuladas, rangos etarios quinquenales y consolidación multirubro.

=== "3. Capa de Explotación y Decisión"
    **Consolas Analíticas e Indicadores Institucionales**
    
    * **Tarjetas KPI y Big Numbers:** Resumen consolidado para la toma de decisiones directivas.
    * **Visualización Segmentada:** Distribución por asegurador (EPS), pabellón y especialidad médica.
    * **Consolas Nominales:** Tablas de auditoría caso a caso para comités de calidad y jefaturas asistenciales.

---

## Estándares de Calidad y Gobierno del Dato

!!! info "Tratamiento de Valores Nulos y Fechas Centinela"
    Todas las consultas aíslan fechas no registradas (`<= 1753-01-01`) para evitar distorsiones en los promedios de estancia (ALOS), oportunidad en triage y programación quirúrgica.

!!! success "Integridad de Transacciones Asistenciales y Financieras"
    Se aplican criterios estrictos de no anulación en los consumos clínicos (`TMPFAC1.tfestaanu1 = 'N'` y `TMPFAC2.TFestaanu2 = 'N'`), garantizando que solo la producción real sea considerada en los balances de prefacturación.

!!! warning "Seguridad, Perfiles y Confidencialidad"
    La información clínica sensible se encuentra protegida bajo políticas de gobierno del dato, permitiendo el acceso a las vistas de auditoría únicamente a los roles correspondientes (Dirección Médica, Coordinación de Quirófanos, Auditoría de Cuentas y Comité de Infecciones).