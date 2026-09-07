# HOMPROC

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`PRCODI`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`TrfCod`** | `char(5)` | NO | Campo transaccional de Hosvital HIS |
|  | **`HomProCod`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HomProDsc`** | `varchar(750)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HomProCnt`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`HomProVlr`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`HomProLH`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOMPROOBS`** | `varchar(250)` | SI | Campo transaccional de Hosvital HIS |
|  | **`HOMPROPR`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
