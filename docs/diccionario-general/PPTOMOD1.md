# PPTOMOD1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`ModDocNro`** | `int` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ModTpoMod`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ModVig`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ModPreCod`** | `char(20)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ModRcuId`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`ModUniNeg`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
|  | **`ModDC`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ModVlr`** | `decimal(17,2)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ModObs`** | `varchar(60)` | SI | Campo transaccional de Hosvital HIS |
|  | **`ModSta`** | `char(1)` | SI | Campo transaccional de Hosvital HIS |
