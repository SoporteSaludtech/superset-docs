# MEDICAMENTO_CONTROL

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`id`** | `bigint` | NO | Campo transaccional de Hosvital HIS |
|  | **`empcod`** | `varchar(2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`anio`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`mes`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`msreso`** | `varchar(15)` | NO | Campo transaccional de Hosvital HIS |
|  | **`consecutivo`** | `bigint` | SI | Campo transaccional de Hosvital HIS |
|  | **`registroSanitario`** | `varchar(20)` | SI | Campo transaccional de Hosvital HIS |
|  | **`nombreGenerico`** | `varchar(500)` | SI | Campo transaccional de Hosvital HIS |
|  | **`nombreComercial`** | `varchar(260)` | SI | Campo transaccional de Hosvital HIS |
|  | **`observacionIngreso`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`observacionEgreso`** | `varchar(255)` | SI | Campo transaccional de Hosvital HIS |
|  | **`saldoInicial`** | `decimal(18,2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`ingresos`** | `decimal(18,2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`egresos`** | `decimal(18,2)` | NO | Campo transaccional de Hosvital HIS |
|  | **`saldoFinal`** | `decimal(18,2)` | NO | Campo transaccional de Hosvital HIS |
