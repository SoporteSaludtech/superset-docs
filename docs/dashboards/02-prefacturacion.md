# Gestión Financiera: Prefacturación y Producción Asistencial

- **Módulo de Origen:** Facturación / Cuentas Médicas (`TMPFAC`, `TMPFAC1`, `TMPFAC2`, `MAEEMP`, `CAPBAS`)
- **Propósito:** Supervisar en tiempo real la producción asistencial ejecutada no facturada para optimizar el flujo de caja.
- **Frecuencia de Actualización:** 10 minutos

---

## 1. Alcance Conceptual y Fórmulas Matemáticas

### Valor Total Prefacturado (WIP - Work in Progress Financiero)
Cuantifica la producción asistencial acumulada en preliquidación pendiente de factura fiscal:

$$\text{Total Prefacturado (\$)} = \sum (\text{Cantidad} \times \text{Valor Unitario})$$

### Días de Rezago en Cierre de Cuenta (Aging)
Tiempo transcurrido desde el egreso del paciente hasta la liquidación de la orden:

$$\text{Aging (Días)} = \text{Fecha Actual} - \text{Fecha de Egreso}$$

### Criterios de Interpretación Financiera
- **Aging <= 3 días:** Operación oportuna de auditoría médica concurrente.
- **Aging 4 - 7 días:** Alerta operativa por cargos pendientes (evoluciones médicas o farmacia sin cerrar).
- **Aging > 7 días:** Riesgo severo de glosa por radicación extemporánea y retraso en recaudo.

---

## 2. Especificación Técnica T-SQL

```sql
SELECT 
    Nombre_Empresa AS CONTRATO_EMPRESA,
    fecha_ingreso AS FECHA_INGRESO,
    hora_ingreso AS HORA_INGRESO,
    identificacion AS NUMERO_IDENTIFICACION,
    tipo_id AS TIPO_IDENTIFICACION,
    Nombre_Paciente AS NOMBRE_PACIENTE,
    [#Ingreso] AS CONSECUTIVO_INGRESO,
    Tipo_Rubro AS TIPO_RUBRO,
    SUM(Valor) AS TOTAL_VALOR
FROM (
    SELECT 
        M.MenomB AS Nombre_Empresa,
        T.TFFCHI AS fecha_ingreso, 
        T.tfhori AS hora_ingreso, 
        T.tfcedu AS identificacion, 
        T.tftdoc AS tipo_id, 
        LTRIM(RTRIM(ISNULL(C.mpnom1, ''))) + ' ' + 
        LTRIM(RTRIM(ISNULL(C.mpnom2, ''))) + ' ' + 
        LTRIM(RTRIM(ISNULL(C.mpape1, ''))) + ' ' + 
        LTRIM(RTRIM(ISNULL(C.mpape2, ''))) AS Nombre_Paciente,
        T.Tmctving AS [#Ingreso],
        'Procedimientos' AS Tipo_Rubro,
        ISNULL(T1.tfvatp, 0) AS Valor
    FROM dbo.TMPFAC T
    INNER JOIN dbo.TMPFAC1 T1 
        ON T.tfcedu = T1.tfcedu AND T.Tftdoc = T1.Tftdoc AND T.Tmctving = T1.Tmctving
    INNER JOIN dbo.MAEEMP M ON T1.tfnitp = M.mennit
    INNER JOIN dbo.CAPBAS C ON T.tfcedu = C.mpcedu AND T.tftdoc = C.mptdoc
    WHERE T1.tfestaanu1 = 'N'

    UNION ALL

    SELECT 
        M.MenomB AS Nombre_Empresa,
        T.TFFCHI AS fecha_ingreso, 
        T.tfhori AS hora_ingreso, 
        T.tfcedu AS identificacion, 
        T.tftdoc AS tipo_id, 
        LTRIM(RTRIM(ISNULL(C.mpnom1, ''))) + ' ' + 
        LTRIM(RTRIM(ISNULL(C.mpnom2, ''))) + ' ' + 
        LTRIM(RTRIM(ISNULL(C.mpape1, ''))) + ' ' + 
        LTRIM(RTRIM(ISNULL(C.mpape2, ''))) AS Nombre_Paciente,
        T.Tmctving AS [#Ingreso],
        'Suministros y Medicamentos' AS Tipo_Rubro,
        ISNULL(T2.tfvats, 0) AS Valor
    FROM dbo.TMPFAC T
    INNER JOIN dbo.TMPFAC2 T2 
        ON T.tfcedu = T2.tfcedu AND T.Tftdoc = T2.Tftdoc AND T.Tmctving = T2.Tmctving
    INNER JOIN dbo.MAEEMP M ON T2.tfnitS = M.mennit
    INNER JOIN dbo.CAPBAS C ON T.tfcedu = C.mpcedu AND T.tftdoc = C.mptdoc
    WHERE T2.TFestaanu2 = 'N' AND T2.TFSTpotrn = 'F'
) AS Consolidado
GROUP BY 
    Nombre_Empresa, fecha_ingreso, hora_ingreso, 
    identificacion, tipo_id, Nombre_Paciente, [#Ingreso], Tipo_Rubro;
```

---

## 3. Diccionario de Componentes Visuales

| Componente | Tipo de Visualización | Métrica / Dimensión | Objetivo Operativo |
| :--- | :--- | :--- | :--- |
| **Total Prefacturado** | Big Number | `SUM(TOTAL_VALOR)` | Monto total acumulado en cuentas abiertas. |
| **Cuentas en Proceso** | Big Number | `COUNT(DISTINCT CONSECUTIVO_INGRESO)` | Carga total de admisiones pendientes de cierre. |
| **Proporción de Rubros** | Gráfico Circular (Donut) | `TIPO_RUBRO` | Relación de gasto Procedimientos vs Medicamentos. |
| **Top Aseguradores (EPS)** | Gráfico de Barras | `CONTRATO_EMPRESA` | Identificación de concentración de cartera WIP. |
| **Consola de Auditoría** | Tabla Interactiva | Paciente, Ingreso, Rubros, Montos | Trazabilidad de admisiones listas para facturar. |