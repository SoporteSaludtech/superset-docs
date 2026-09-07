# Modelo de Datos - Gestión de Glosas y Devoluciones

## 1. Visión General de la Arquitectura
El módulo analítico de Business Intelligence se desacopla del procesamiento transaccional de **Hosvital HIS** mediante la vista centralizada:

dbo.VW_GLOSAS_Y_DEVOLUCIONES

Esta vista desnormaliza y homologa las relaciones entre las cabeceras de objeción, los ítems de factura objetados, los motivos normativos de glosa y la trazabilidad de radicación frente a las EPS y aseguradoras.

---

## 2. Tablas Transaccionales Integradas

| Tabla Hosvital | Descripción Funcional | Claves de Enlace | Rol en la Vista |
| :--- | :--- | :--- | :--- |
| **\ADGLOSAS\** | Cabecera general de la glosa | \GloNum\, \MPNFac\ | Fecha de notificación, pagador responsable y estado maestro (\GloEdo\). |
| **\ADGLOSAS1\** | Detalle por ítem de consumo glosado | \GloNum\, \GloItem\, \PRNCON\ | Valores monetarios: objetado, aceptado, levantado y saldo en disputa. |
| **\MAEATE\** | Maestro de atenciones y facturación | \MPNFac\, \MATipDoc\, \MPTDoc\ | Paciente, plan de beneficios, contrato y fecha de emisión/radicación. |
| **\GLOSAS\** | Catálogo normativo de motivos | \GlsCod\ | Clasificación estándar del Ministerio de Salud / normatividad EPS. |
| **\MAEPRO\** | Maestro de productos y procedimientos | \PRNCON\ | Homologación del código CUPS o CUM y denominación técnica. |
| **\ADMGLO11\ / \ADMGLO01\** | Tablas de radicación y devoluciones | \GloNum\, \RadNum\ | Fechas límite, oficios de radicación externa y devoluciones de facturas. |

---

## 3. Homologación de Estados Gerenciales

Hosvital registra internamente múltiples códigos en el campo \ADGLOSAS.GloEdo\. La vista estandariza estos valores para su consumo en dashboards analíticos:

* **Códigos 1, 2:** \Notificada (Sin Responder)\
* **Códigos 3, 4, 11:** \Respondida / En Trámite\
* **Códigos 5, 6, 8, 9:** \En Conciliación\
* **Códigos 12, 13:** \Cerrada / Conciliada\
* **Otros:** \En Revisión Auditoría\

---

## 4. Métricas e Indicadores de Negocio

* **Valor Glosado:** Total objetado por las EPS (\ADGLOSAS1.GloVlr\).
* **Valor Levantado:** Monto recuperado tras la respuesta institucional (\ADGLOSAS1.GloVlrLev\).
* **Valor Aceptado:** Pérdida asumida por la institución (\ADGLOSAS1.GloVlrAce\).
* **Saldo Pendiente:**
  Out-Null\text{SALDO\_PENDIENTE} = \text{VALOR\_GLOSADO} - (\text{VALOR\_LEVANTADO} + \text{VALOR\_ACEPTADO})Out-Null
* **Porcentaje de Efectividad:**
  Out-Null\% \text{ Efectividad} = \left(\frac{\text{VALOR\_LEVANTADO}}{\text{VALOR\_GLOSADO}}\right) \times 100Out-Null
