# Diccionario de Datos - Vistas Analíticas BI

Catálogo de vistas de capa semántica alojadas en SQL Server (\HVT_HOSVITAL\) consumidas por **Apache Superset**.

---

## 1. Módulo Financiero y Cartera


### VW_GLOSAS_Y_DEVOLUCIONES

Soporta la **Consola de Glosas y Devoluciones**. Unifica cabeceras, detalles de objeción y trazabilidad de radicación.

| Campo | Tipo SQL | Superset Type | Descripción |
| :--- | :--- | :--- | :--- |
| \CODIGO_SEDE\ | \VARCHAR(10)\ | STRING | Código de la sede prestadora. |
| \NOMBRE_SEDE\ | \VARCHAR(100)\ | STRING | Nombre descriptivo de la sede. |
| \NUMERO_FACTURA\ | \VARCHAR(20)\ | STRING | Factura de venta emitida por Hosvital. |
| \TIPO_OBJECION\ | \VARCHAR(30)\ | STRING | Clasificación: Glosa Parcial o Devolución Total. |
| \CODIGO_ASEGURADORA\ | \VARCHAR(20)\ | STRING | NIT o identificador de la EAPB / EPS. |
| \NOMBRE_ASEGURADORA\ | \VARCHAR(150)\ | STRING | Nombre comercial de la aseguradora. |
| \CODIGO_MOTIVO_GLOSA\ | \VARCHAR(10)\ | STRING | Código normativo del motivo de objeción. |
| \DESCRIPCION_MOTIVO_GLOSA\ | \VARCHAR(255)\ | STRING | Detalle según resolución ministerial. |
| \CODIGO_CONCEPTO_ITEM\ | \VARCHAR(20)\ | STRING | CUPS de procedimiento o CUM de medicamento. |
| \DESCRIPCION_ITEM\ | \VARCHAR(255)\ | STRING | Denominación del producto/servicio en disputa. |
| \ESTADO_GLOSA\ | \VARCHAR(50)\ | STRING | Estado agrupado: Notificada, En Trámite, Conciliada, Cerrada. |
| \FECHA_NOTIFICACION_GLOSA\ | \DATETIME\ | TEMPORAL | Fecha de recepción formal del requerimiento. |
| \VALOR_FACTURADO\ | \DECIMAL(18,2)\ | NUMERIC | Valor total de la factura asociada. |
| \VALOR_GLOSADO\ | \DECIMAL(18,2)\ | NUMERIC | Monto inicial objetado por la aseguradora. |
| \VALOR_LEVANTADO_IPS\ | \DECIMAL(18,2)\ | NUMERIC | Recursos recuperados y ratificados a la IPS. |
| \VALOR_ACEPTADO_IPS\ | \DECIMAL(18,2)\ | NUMERIC | Pérdida aceptada por error operacional. |
| \SALDO_PENDIENTE\ | \DECIMAL(18,2)\ | NUMERIC | Monto en litigio o mesa de conciliación. |

---

### VW_PREFACTURACION_PRODUCCION

Alimenta la **Consola Prefacturación y Producción**. Agrupa consumos en tránsito y cargos no facturados.

| Campo | Tipo SQL | Superset Type | Descripción |
| :--- | :--- | :--- | :--- |
| \ID_CONSUMO\ | \BIGINT\ | STRING / ID | Identificador único del cargo hospitalario. |
| \NUMERO_HISTORIA\ | \VARCHAR(20)\ | STRING | Identificación del paciente. |
| \NOMBRE_ASEGURADORA\ | \VARCHAR(150)\ | STRING | Aseguradora responsable del contrato. |
| \CENTRO_COSTO\ | \VARCHAR(50)\ | STRING | Unidad de servicio generadora del gasto. |
| \FECHA_CONSUMO\ | \DATETIME\ | TEMPORAL | Momento del registro clínico del servicio. |
| \ESTADO_CARGO\ | \VARCHAR(30)\ | STRING | Estado en tabla \TMPFAC\ (Pendiente, Auditado, Facturado). |
| \DIAS_TRANSITO\ | \INT\ | NUMERIC | Días desde la prestación hasta la prefacturación. |
| \VALOR_TOTAL_CARGO\ | \DECIMAL(18,2)\ | NUMERIC | Monto económico en tránsito pendiente por cerrar. |

---

## 2. Módulo Administrativo

### dbo.VW_CENSO_HOSPITALARIO

Base de la **Consola de Gestión y Censo Hospitalario**. Refresca el estado de camas en tiempo real.

| Campo | Tipo SQL | Superset Type | Descripción |
| :--- | :--- | :--- | :--- |
| \CODIGO_CAMA\ | \VARCHAR(20)\ | STRING | Identificador físico de la cama. |
| \NOMBRE_PABELLON\ | \VARCHAR(100)\ | STRING | Bloque, piso o pabellón de hospitalización. |
| \TIPO_SERVICIO\ | \VARCHAR(50)\ | STRING | UCI, Intermedios, Hospitalización General, Aislamiento. |
| \ESTADO_CAMA\ | \VARCHAR(30)\ | STRING | Ocupada, Disponible, En Desinfección, En Mantenimiento. |
| \NUMERO_HISTORIA\ | \VARCHAR(20)\ | STRING | Documento del paciente ocupante (nulo si vacía). |
| \FECHA_INGRESO_CAMA\ | \DATETIME\ | TEMPORAL | Fecha y hora en que se asignó la cama al paciente actual. |
| \DIAS_ESTANCIA_ACTUAL\| \INT\ | NUMERIC | Días continuos de ocupación por el paciente actual. |
| \ALERTA_ESTANCIA\ | \VARCHAR(20)\ | STRING | Indicador: Normal (≤3d), Prolongada (4-7d), Crítica (>7d). |

---

### VW_FACTURACION_WIP

Base de la **Consola Facturación y WIP Post-Alta**. Monitorea el rezago de emisión de facturas.

| Campo | Tipo SQL | Superset Type | Descripción |
| :--- | :--- | :--- | :--- |
| \NUMERO_INGRESO\ | \VARCHAR(20)\ | STRING | Consecutivo de atención hospitalaria. |
| \FECHA_EGRESO_CLINICO\| \DATETIME\ | TEMPORAL | Momento de alta médica firmada en Hosvital. |
| \DIAS_REZAGO_FACTURA\ | \INT\ | NUMERIC | Días hábiles sin emitir factura posterior al egreso. |
| \CUMPLIMIENTO_LEY1438\| \VARCHAR(20)\ | STRING | Semáforo normativo de facturación (En Término / Vencido). |
| \VALOR_ESTIMADO_CUENTA\| \DECIMAL(18,2)\| NUMERIC | Monto acumulado de servicios pendientes de corte legal. |

---

## 3. Módulo Asistencial y Quirúrgico

### VW_EGRESOS_URGENCIAS

Base de la **Consola Egresos y Urgencias**. Métricas de rotación y oportunidad.

| Campo | Tipo SQL | Superset Type | Descripción |
| :--- | :--- | :--- | :--- |
| \CONSECUTIVO_ATENCION\ | \VARCHAR(20)\ | STRING | Identificador del episodio asistencial. |
| \NIVEL_TRIAGE\ | \VARCHAR(10)\ | STRING | Clasificación de severidad (Triage I a V). |
| \FECHA_INGRESO\ | \DATETIME\ | TEMPORAL | Entrada a la sala de urgencias. |
| \FECHA_ALTA\ | \DATETIME\ | TEMPORAL | Salida formal por egreso o remisión. |
| \DESTINO_EGRESO\ | \VARCHAR(50)\ | STRING | Domicilio, Traslado UCI, Remisión Externa, Fallecimiento. |
| \HORAS_PERMANENCIA\ | \DECIMAL(10,2)\ | NUMERIC | Tiempo total transcurrido en el servicio de urgencias. |

---

### VW_ORDENES_QUIRURGICAS

Base de la **Consola Programación y Ocupación QX**. Gestión de salas y quirófanos.

| Campo | Tipo SQL | Superset Type | Descripción |
| :--- | :--- | :--- | :--- |
| \NUMERO_ORDEN_QX\ | \VARCHAR(20)\ | STRING | Consecutivo de la orden de cirugía. |
| \SALA_QUIROFANO\ | \VARCHAR(50)\ | STRING | Nombre o número de quirófano asignado. |
| \ESPECIALIDAD_QX\ | \VARCHAR(100)\ | STRING | Cirugía General, Ortopedia, Neurocirugía, etc. |
| \ESTADO_CIRUGIA\ | \VARCHAR(30)\ | STRING | Programada, Realizada, Cancelada, Reprogramada. |
| \FECHA_PROGRAMADA\ | \DATETIME\ | TEMPORAL | Fecha pactada en agenda. |
| \DURACION_MINUTOS\ | \INT\ | NUMERIC | Tiempo efectivo de uso de la sala quirúrgica. |
