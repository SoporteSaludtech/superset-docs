# Gestión Asistencial: Egresos Hospitalarios y Urgencias

- **Módulo de Origen:** Hospitalización y Urgencias (`Ingresos`, `Capbas`, `Maepab`, `Maemed1`, `MAEESP`, `Maeemp`)
- **Propósito:** Monitorizar el flujo de altas médicas, rotación de camas, tiempo de estancia y carga por especialidad médica.
- **Frecuencia de Actualización:** 15 minutos

---

## 1. Alcance Conceptual y Fórmulas Matemáticas

### Estancia Media Hospitalaria (ALOS - Average Length of Stay)
Calcula el número promedio de días que los pacientes dados de alta permanecieron internados:

$$\text{ALOS (Días)} = \frac{\sum_{i=1}^{n} (\text{FechaEgreso}_i - \text{FechaIngreso}_i)}{\text{Total Egresos}}$$

### Tasa de Ocupación Hospitalaria
Porcentaje de utilización de la capacidad instalada en un corte determinado:

$$\text{Ocupación (\%)} = \left( \frac{\text{Camas Ocupadas}}{\text{Camas Habilitadas}} \right) \times 100$$

### Criterios de Interpretación Clínica y Operativa
- **Ocupación 75% - 85%:** Rango óptimo que permite absorber fluctuaciones de demanda sin saturar urgencias.
- **Ocupación > 90%:** Alerta crítica de congestión hospitalaria y riesgo de retención de pacientes en urgencias (*boarding*).
- **Estancia Prolongada (> 1.5 DE del promedio):** Disparador de auditoría para identificar retrasos en interconsultas o estudios diagnósticos.

---

## 2. Especificación Técnica T-SQL

```sql
SELECT 
    i.IngCsc AS CONSECUTIVO_INGRESO,
    i.MPCedu AS NUMERO_IDENTIFICACION,
    i.MPTDoc AS TIPO_IDENTIFICACION,
    c.MPNomC AS NOMBRE_PACIENTE,
    i.IngFecAdm AS FECHA_INGRESO,
    i.IngFecEgr AS FECHA_EGRESO,
    CASE 
        WHEN i.ClaPro = 2 THEN 'Hospitalización'
        WHEN i.ClaPro = 3 THEN 'Urgencias'
        ELSE 'Otro'
    END AS TIPO_ATENCION,
    pab.MPNomP AS SERVICIO_EGRESO,
    i.IngCam AS CAMA_EGRESO,
    esp.MENOME AS ESPECIALIDAD_MEDICO_TRATANTE,
    med.mmnomm AS MEDICO_TRATANTE,
    emp.MENOMB AS CONTRATO_EMPRESA,
    CASE 
        WHEN DATEDIFF(DAY, i.IngFecAdm, i.IngFecEgr) >= 0 
        THEN DATEDIFF(DAY, i.IngFecAdm, i.IngFecEgr) + 1 
        ELSE 1 
    END AS DIAS_ESTANCIA
FROM dbo.Ingresos i
INNER JOIN dbo.Capbas c ON i.MPCedu = c.MPCedu AND i.MPTDoc = c.MPTDoc
LEFT JOIN dbo.Maepab pab ON i.MPCodP = pab.MPCodP
LEFT JOIN dbo.Maemed1 med ON i.IngMedTra = med.mmcodm
LEFT JOIN dbo.MAEESP esp ON med.mmeesp = esp.mecode
LEFT JOIN dbo.Maeemp emp ON i.IngNit = emp.MENNIT
WHERE i.ClaPro IN (2, 3)
  AND i.IngFecEgr IS NOT NULL 
  AND i.IngFecEgr > '1753-01-01';
```

---

## 3. Diccionario de Componentes Visuales

| Componente | Tipo de Visualización | Métrica / Dimensión | Objetivo Operativo |
| :--- | :--- | :--- | :--- |
| **KPI Total Egresos** | Big Number | `COUNT(CONSECUTIVO_INGRESO)` | Conteo total de altas hospitalarias en el corte. |
| **KPI Promedio Estancia** | Big Number | `AVG(DIAS_ESTANCIA)` | Control del giro de cama asistencial (ALOS). |
| **Top Especialidades** | Gráfico de Barras | `ESPECIALIDAD_MEDICO_TRATANTE` | Carga de altas por servicio médico tratante. |
| **Egresos por Pabellón** | Gráfico Circular (Donut) | `SERVICIO_EGRESO` | Concentración de altas por servicio hospitalario. |
| **Consola Nominal de Altas** | Tabla Interactiva | Paciente, Cama, Fechas, Asegurador | Auditoría clínica caso a caso y revisión de estancia. |