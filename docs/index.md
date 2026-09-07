# Centro de Analítica e Inteligencia Clínica - Hosvital HIS

Repositorio central de documentación técnica, operativa y funcional de los cuadros de mando institucionales orientados al monitoreo del ciclo asistencial, la optimización financiera y la seguridad del paciente.

---

## Matriz General de Cuadros de Mando

| Área de Gestión | Cuadro de Mando | Indicadores Principales | Frecuencia | Enlace al Manual |
| :--- | :--- | :--- | :--- | :--- |
| **Arquitectura y Datos** | Arquitectura y Modelo de Datos | Esquema relacional general, pipeline Direct Query y flujos analíticos | N/A | [Ver Arquitectura](arquitectura/modelo-datos.md) |
| **Arquitectura y Datos** | Diccionario de Vistas BI | Catálogo técnico de vistas SQL materializadas (`VW_*`) | N/A | [Ver Vistas BI](diccionario-datos.md) |
| **Arquitectura y Datos** | Catálogo General HOSVITAL | Estructura completa de 1.784 tablas y vistas transaccionales | N/A | [Ver Catálogo](diccionario-general/index.md) |
| **Gestión Asistencial** | Consola Egresos y Urgencias | Estancia Media (ALOS), oportunidad de triage y destinos de alta | 15 Minutos | [Ver Ficha Técnica](dashboards/01-egresos-urgencias.md) |
| **Gestión Asistencial** | Consola Análisis de Ingresos | Volumen por vía de ingreso, asegurador y especialidad médica | 15 Minutos | [Ver Ficha Técnica](dashboards/10-consola_analisis_ingresos.md) |
| **Gestión Asistencial** | Calidad, Seguridad e IAAS | Tasa de infecciones por 100 camas-día y protocolos de aislamiento | 6 Horas | [Ver Ficha Técnica](dashboards/04-vigilancia-iaas.md) |
| **Gestión Asistencial** | Vigilancia Epidemiológica (SIVIGILA)| Notificación obligatoria de eventos, transmisibilidad ETV/ETS | 6 Horas | [Ver Ficha Técnica](dashboards/05 - Sivigila.md) |
| **Gestión Asistencial** | Riesgo y Alto Costo (CAC) | Adherencia a guías, tamizaje oncológico y marcadores renales | Semanal | [Ver Ficha Técnica](dashboards/06-alto-costo-cac.md) |
| **Gestión Asistencial** | Consola y Cohortes CAC | Indicadores de severidad y seguimiento de cohortes protegidas | Semanal | [Ver Ficha Técnica](dashboards/07-consola-y-cohortes-cac.md) |
| **Gestión Asistencial** | Cohortes - Enfermedades Crónicas | Riesgo cardiovascular, HTA, diabetes y control ambulatorio | Mensual | [Ver Ficha Técnica](dashboards/08-consola_gestion_cohortes_cronicas.md) |
| **Gestión Asistencial** | Estadísticas de Trauma | Índices de severidad (ISS/RTS) y tiempos quirúrgicos iniciales | 12 Horas | [Ver Ficha Técnica](dashboards/09-consola_estadisticas_trauma.md) |
| **Gestión Quirúrgica** | Programación y Ocupación QX | Rendimiento de quirófanos, cancelaciones y oportunidad de agenda | Tiempo Real | [Ver Ficha Técnica](dashboards/03-ordenes-quirurgicas.md) |
| **Gestión Administrativa** | Censo Hospitalario y Ocupación | Disponibilidad de camas en tiempo real, bloqueos y desinfección | Tiempo Real | [Ver Ficha Técnica](dashboards/11-consola-censo-hospitalario.md) |
| **Gestión Logística** | Control FEFO y Trazabilidad de Lotes | Semáforo de vencimiento (Res. 1403), capital en riesgo de caducidad, días para vencer y saldo valorizado por bodega/CUM | Turno / 8 Horas | [Ver Ficha Técnica](logistica/control_fefo_lotes.md) |
| **Gestión Financiera y Cartera** | Consola de Glosas y Devoluciones | Efectividad de recobro, saldo objetado, pérdidas y homologación | 24 Horas | [Ver Manual](guia-usuario.md) |
| **Gestión Financiera y Cartera** | Prefacturación y Producción | Días de rezago de prefactura, WIP y cargos en tránsito | Turno / 8 Horas | [Ver Ficha Técnica](dashboards/02-prefacturacion.md) |
| **Gestión Financiera y Cartera** | Facturación y WIP Post-Alta | Tiempos de egreso a factura, Ley 1438 y corte de estancias | 12 Horas | [Ver Ficha Técnica](dashboards/12-consola-facturacion-wip.md) |
| **Gestión Financiera y Cartera** | Edades de Cartera y Recaudo | Saldo neto exigible, recaudo acumulado, valor glosado, efectividad (%) y estratificación etaria (0 a >360 días) | 8 Horas | [Ver Ficha Técnica](dashboards/14-consola-edades-cartera-recaudo.md) |

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