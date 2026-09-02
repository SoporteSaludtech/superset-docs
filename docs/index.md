# Centro de Analítica e Inteligencia Clínica - Hosvital HIS

Repositorio central de documentación técnica, operativa y funcional de los cuadros de mando institucionales orientados al monitoreo del ciclo asistencial, la optimización financiera y la seguridad del paciente.

---

## Matriz General de Cuadros de Mando

| Área de Gestión | Cuadro de Mando | Indicadores Principales | Frecuencia | Enlace al Manual |
| :--- | :--- | :--- | :--- | :--- |
| **Gestión Asistencial** | **Consola Egresos y Urgencias** | Estancia Media (ALOS), Tasa de Ocupación, Rotación de Camas | 15 Minutos | [Ver Ficha Técnica](dashboards/01-egresos-urgencias.md) |
| **Gestión Asistencial** | **Consola Análisis de Ingresos** | Total Ingresos, Distribución Ambulatorio vs Hospitalización, Top Especialidades Tratantes, Concentración por EPS | 15 Minutos | [Ver Ficha Técnica](dashboards/consola_analisis_ingresos.md) |
| **Gestión Asistencial** | **Consola Calidad, Seguridad e IAAS** | Tasa de Infecciones x 100 Camas-Día, Aislamiento por Pabellón | 6 Horas | [Ver Ficha Técnica](dashboards/04-vigilancia-iaas.md) |
| **Gestión Asistencial** | **Consola Vigilancia en Salud Pública (SIVIGILA)** | Índice de Detección SIVIGILA, Casos Totales, Transmisibilidad ETV vs ETS | 6 Horas | [Ver Ficha Técnica](dashboards/05%20-%20Sivigila.md) |
| **Gestión Asistencial** | **Cosola Riesgo y Altocosto** | Tasa de Detección CAC, Adherencia a Guías Clínicas, Distribución de Estadíos | 6 Horas | [Ver Ficha Técnica](dashboards/06-alto-costo-cac.md) |
| **Gestión Asistencial** | **Consola y Cohortes CAC** | Auditoría Nominal de Cohortes, Tasa de Cumplimiento Terapéutico, Días de Tratamiento Activo | 6 Horas| [Ver Ficha Técnica](dashboards/07-consola-y-cohortes-cac.md) |
| **Gestión Asistencial** | **Consola de Gestión y Cohortes - Enfermedades Crónicas** | Control HTA (PAS < 140 / PAD < 90), Control Metabólico DM2 (HbA1c ≤ 7.0%), Tasa de Reingreso EPOC | 6 Horas | [Ver Ficha Técnica](dashboards/08-consola_gestion_cohortes_cronicas.md) |
| **Gestión Asistencial** | **Consola Estadísticas de Trauma** | Volumen por Nivel de Triage, Tiempo Puerta-Médico, Tasa de Intervención Quirúrgica de Trauma | 6 Horas | [Ver Ficha Técnica](dashboards/09-consola_estadisticas_trauma.md) |
| **Gestión Financiera** | **Consola Prefacturación y Producción** | Valor WIP en Tránsito, Aging de Prefactura, Consumos por EPS | 15 Minutos | [Ver Ficha Técnica](dashboards/02-prefacturacion.md) |
| **Gestión Quirúrgica** | **Consola Programación y Ocupación QX** | Tasa de Cancelación, Oportunidad Quirúrgica, Demanda por Especialidad | 15 Minutos | [Ver Ficha Técnica](dashboards/03-ordenes-quirurgicas.md) |


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
    
    * **Tarjetas KPI y Resúmenes:** Resumen consolidado para la toma de decisiones directivas.
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