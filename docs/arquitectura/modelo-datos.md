# Arquitectura y Modelo de Datos General - Intelligy Health

## 1. Visión Global de la Plataforma
El ecosistema de Business Intelligence de **Intelligy Health** desacopla el procesamiento analítico del motor transaccional de **Hosvital HIS** mediante una capa semántica de vistas SQL materializadas e indexadas.

```mermaid
graph TD
    subgraph Capa Transaccional [HVT_HOSVITAL - SQL Server]
        MAEATE[MAEATE: Facturación y Pacientes]
        ADGLOSAS[ADGLOSAS / 1: Glosas]
        INGRESOS[HISTORIAPAC / INGRESOS: Asistencial]
        CAMAS[CAMAS / CENSO: Gestión Camas]
        QX[ORDQUIR / QUIROF: Cirugías]
    end

    subgraph Capa Analítica [Vistas Homologadas]
        V_GLO[VW_GLOSAS_Y_DEVOLUCIONES]
        V_ING[VW_ANALISIS_INGRESOS]
        V_CEN[VW_CENSO_HOSPITALARIO]
        V_WIP[VW_FACTURACION_WIP]
        V_QX[VW_ORDENES_QUIRURGICAS]
        V_EGR[VW_EGRESOS_URGENCIAS]
    end

    subgraph Capa de Visualización [Apache Superset]
        D_FIN[Consolas Financieras]
        D_ADM[Consolas Administrativas]
        D_ASI[Consolas Asistenciales]
        D_QX[Consolas Quirúrgicas]
    end

    Capa Transaccional --> Capa Analítica
    Capa Analítica --> Capa de Visualización
```

---

## 2. Dominios de Datos y Vistas Maestras

| Dominio | Vistas Analíticas Centrales | Tablas Base Hosvital | Granularidad |
| :--- | :--- | :--- | :--- |
| **Gestión Financiera** | \VW_GLOSAS_Y_DEVOLUCIONES\, \VW_PREFACTURACION\ | \ADGLOSAS\, \ADGLOSAS1\, \TMPFAC\, \MAEATE\ | Ítem glosado / Orden de cargo |
| **Gestión Administrativa**| \VW_CENSO_HOSPITALARIO\, \VW_FACTURACION_WIP\ | \CAMAS\, \PABELLONES\, \MAEATE\, \FACNOT\ | Cama física / Cuenta post-alta |
| **Gestión Asistencial** | \VW_EGRESOS_URGENCIAS\, \VW_ANALISIS_INGRESOS\ | \HISTORIAPAC\, \TRIAGE\, \INGRESOS\, \MAEPAC\ | Episodio de atención / Paciente |
| **Riesgo y Epidemiología** | \VW_VIGILANCIA_IAAS\, \VW_COHORTES_CAC\ | \LABORATORIO\, \DIAGNOSTICOS\, \FORMULACION\ | Evento de notificación / Ficha |
| **Gestión Quirúrgica** | \VW_ORDENES_QUIRURGICAS\ | \ORDQUIR\, \QUIROFANOS\, \CIRUGIAS\ | Procedimiento en quirófano |

---

## 3. Entidades Maestras Transversales (Core HIS)

* **\MAEATE\ (Atenciones y Facturación):** Eje de unión central que conecta episodios clínicos, consumos facturados y cobros a aseguradoras.
* **\MAEPAC\ (Maestro de Pacientes):** Registro demográfico único (tipo de documento, identificación, fecha de nacimiento, género).
* **\MAEEMP\ / \CONTRATOS\ (Aseguradoras y Planes):** Identificación institucional de EAPB, EPS, convenios y modalidades contractuales (Capitación, Evento, PGP).
* **\MAEPRO\ (Procedimientos y Suministros):** Catálogo unificado de códigos CUPS, medicamentos CUM y materiales hospitalarios.

---

## 4. Estándares Técnicos del Pipeline BI

* **Motor de Base de Datos:** Microsoft SQL Server (\HVT_HOSVITAL\).
* **Modo de Conexión:** Direct Query / Live Virtual Datasets sobre Apache Superset.
* **Tolerancia a Nulos:** Homologación mediante \ISNULL()\ y \COALESCE()\ en campos de agrupación categórica.
* **Zonas Horarias:** Fechas estandarizadas en formato ISO-8601 (\YYYY-MM-DD hh:mm:ss\) para compatibilidad con Superset Time-Grain.
