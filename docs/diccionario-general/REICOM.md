# REICOM

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`REICKEY`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`REITipDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
|  | **`REITSANG`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICNUM`** | `decimal(11,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICANTPE1`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICANTPE2`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIAlergia`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REICGINECO`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIchAB`** | `varchar(MAX)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIHisPPr`** | `smallint` | SI | Campo transaccional de Hosvital HIS |
|  | **`REINUMDE`** | `decimal(10,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`REIREIPas`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
