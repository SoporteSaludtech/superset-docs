# NIACTFDME

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`AcFCod`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIACTMCON`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIACDMANI`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`NIACDMMES`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`NIACDMCHI`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIACDMVLR`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIACDMAIM`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIACDMCAJ`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIACDMDEP`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIACDMDAI`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIACDMDAJ`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`NIACDMICN`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
