# Gestión Quirúrgica: Ocupación y Programación de Salas

- **Módulo de Origen:** Bloque Quirúrgico (`procir`, `procir1`, `HCCOM1`, `MAEESP`, `maepro`, `maemed1`)
- **Propósito:** Trazabilidad integral de las solicitudes de cirugía, confirmaciones de tabla y efectividad en el uso de salas.
- **Frecuencia de Actualización:** 5 minutos

---

## 1. Alcance Conceptual y Fórmulas Matemáticas

### Tasa de Cancelación Quirúrgica
Proporción de cirugías reservadas o confirmadas que fueron suspendidas antes del acto quirúrgico:

$$\text{Tasa Cancelación (\%)} = \left( \frac{\text{Órdenes Canceladas}}{\text{Total Órdenes Programadas}} \right) \times 100$$

### Tasa de Cumplimiento Quirúrgico
Porcentaje de procedimientos efectivamente ejecutados frente al plan operatorio:

$$\text{Cumplimiento (\%)} = \left( \frac{\text{Cirugías Realizadas}}{\text{Total Órdenes Programadas}} \right) \times 100$$

### Criterios de Interpretación Quirúrgica
- **Cancelación <= 3%:** Estándar óptimo de oportunidad prequirúrgica y valoración preanestésica.
- **Cancelación > 5%:** Disparador de intervención en confirmación de pacientes o disponibilidad de instrumental.

---

## 2. Especificación Técnica T-SQL

```sql
SELECT DISTINCT 
    PC.ProFSep AS FECHA_SOLICITUD,
    PC.procircod AS NUMERO_ORDEN,
    PC.profecF AS FECHA_PROGRAMADA_CIRUGIA,
    CONCAT(CONVERT(VARCHAR, PC.profecF, 103), ' ', PC.ProHorI, ' - ', PC.ProHorF) AS HORARIO_CIRUGIA,
    PC.PfcHrCnf AS FECHA_CONFIRMACION,
    PC.PFcHrCnc AS FECHA_CANCELACION,
    CASE 
        WHEN PC.PFcHrCnc IS NULL OR PC.PFcHrCnc <= '17530101' THEN 'No Cancelada' 
        ELSE 'Cancelada' 
    END AS ESTADO_CANCELACION,
    CB.mpcedu AS NUMERO_DOCUMENTO,
    CB.mptdoc AS TIPO_DOCUMENTO,
    CB.mpnomc AS NOMBRE_PACIENTE,
    CB.mptele AS TELEFONO_PACIENTE,
    ISNULL(PC1.Crgcod, 'N/A') AS CUPS_PROCEDIMIENTO,
    ISNULL(MP.prnomb, 'PROCEDIMIENTO SIN DEFINIR') AS DESCRIPCION_PROCEDIMIENTO,
    ME.MENOME AS ESPECIALIDAD_QX,
    M1.mmnomm AS MEDICO_ORDENANTE,
    CASE 
        WHEN CAST(PC.ProFliSol AS VARCHAR) = '0' THEN 'Sin definir' 
        WHEN CAST(HC.HISCLPR AS VARCHAR) = '1' THEN 'Orden Ambulatoria' 
        WHEN CAST(HC.HISCLPR AS VARCHAR) = '2' THEN 'Orden Hospitalización' 
        WHEN CAST(HC.HISCLPR AS VARCHAR) = '3' THEN 'Orden Urgencias' 
        ELSE 'Otro' 
    END AS ORIGEN_ATENCION,
    CASE 
        WHEN CAST(PC.proesta AS VARCHAR) = '1' THEN 'Reservada'
        WHEN CAST(PC.proesta AS VARCHAR) = '2' THEN 'Confirmada'
        WHEN CAST(PC.proesta AS VARCHAR) = '3' THEN 'Cancelada'
        WHEN CAST(PC.proesta AS VARCHAR) = '4' THEN 'Realizada'
        ELSE 'Pendiente' 
    END AS ESTADO_ORDEN
FROM dbo.procir PC
LEFT JOIN dbo.procir1 PC1 
    ON PC.proempcod = PC1.proempcod AND PC.proMcdpto = PC1.proMcdpto AND PC.procircod = PC1.procircod
LEFT JOIN dbo.MAEESP ME ON RTRIM(PC.ProEspSep) = RTRIM(ME.mecode)
LEFT JOIN dbo.capbas CB ON PC.mpcedu = CB.mpcedu AND PC.mptdoc = CB.mptdoc
LEFT JOIN dbo.maepro MP ON PC1.Crgcod = MP.prcodi
LEFT JOIN dbo.maemed1 M1 ON PC.propersep = M1.mmcodm
LEFT JOIN dbo.HCCOM1 HC 
    ON PC.mpcedu = HC.HISCKEY AND PC.mptdoc = HC.HISTIPDOC AND PC.ProFliSol = HC.hiscsec;
```

---

## 3. Diccionario de Componentes Visuales

| Componente | Tipo de Visualización | Métrica / Dimensión | Objetivo Operativo |
| :--- | :--- | :--- | :--- |
| **Total Solicitudes QX** | Big Number | `COUNT(DISTINCT NUMERO_ORDEN)` | Demanda global de programación quirúrgica. |
| **Cirugías Realizadas** | Big Number | `COUNT(DISTINCT NUMERO_ORDEN)` ejecutadas | Productividad neta de salas de cirugía. |
| **Estado de la Programación** | Gráfico Circular (Donut) | `ESTADO_ORDEN` | Proporción Reservadas vs Confirmadas vs Canceladas. |
| **Demanda por Especialidad** | Gráfico de Barras | `ESPECIALIDAD_QX` | Carga de procedimientos por servicio quirúrgico. |
| **Consola de Programación** | Tabla Interactiva | Paciente, CUPS, Cirujano, Teléfono | Herramienta de gestión para confirmación de tabla. |