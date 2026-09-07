# DET_FACT_REEMBOLSO

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
|  | **`factReembolsoId`** | `bigint` | SI | Campo transaccional de Hosvital HIS |
|  | **`cuenta`** | `varchar(20)` | NO | Campo transaccional de Hosvital HIS |
|  | **`numeroIdProveedor`** | `varchar(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`tipoProveedor`** | `varchar(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`numeroObligacion`** | `varchar(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`centroCosto`** | `varchar(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`fechaAutorizacion`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`numeroAutorizacion`** | `varchar(50)` | SI | Campo transaccional de Hosvital HIS |
|  | **`tipoComprobante`** | `varchar(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`observacion`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`valorBase`** | `decimal(18,2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`impuesto`** | `varchar(8)` | NO | Campo transaccional de Hosvital HIS |
|  | **`valorImpuesto`** | `decimal(18,2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`valorTotal`** | `decimal(18,2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`consecutivo`** | `int` | NO | Campo transaccional de Hosvital HIS |
