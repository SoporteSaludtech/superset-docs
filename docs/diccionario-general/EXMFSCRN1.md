# EXMFSCRN1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ExMPCedu`** | `char(15)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ExMPTDoc`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ExIngCsc`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ExCtvRN`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ExIngEgr`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ExItmRN`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ExFscPtl`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ExObsRN`** | `varchar(1000)` | SI | Campo transaccional de Hosvital HIS |
