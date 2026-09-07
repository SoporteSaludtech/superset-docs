# HCCOM

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`HISCKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`HISTipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HISCFOTO`** | `char(35)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISTSANG`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISCNUM`** | `decimal(10,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISCNUMDE`** | `decimal(10,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISCANTPE1`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISCANTPE2`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HCAlergia`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISCGINECO`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HischAB`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HisPPr`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`HISALEPAC`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
