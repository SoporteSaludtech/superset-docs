# CTRPRES1

**Tipo de Objeto:** Tabla Transaccional  
**Base de Datos:** `HVT_HOSVITAL`  
**Esquema:** `dbo`

---

## Estructura de Campos

| PK | Nombre de Columna | Tipo de Dato | Admite Nulos | Descripción / Rol Funcional |
| :-: | :--- | :--- | :-: | :--- |
| 🔑 | **`EMPCOD`** | `char(2)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`BODEGA`** | `char(4)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`DOCCOD`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CtrPreNoD`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CtrPreCns`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CTRPRESED`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CrPrDcDev`** | `char(3)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CrPrNoDev`** | `decimal(15,0)` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CrPrCsDev`** | `smallint` | NO | Campo transaccional de Hosvital HIS |
| 🔑 | **`CRPRSEDEV`** | `char(9)` | NO | Campo transaccional de Hosvital HIS |
|  | **`CrPrCnDev`** | `money` | SI | Campo transaccional de Hosvital HIS |
|  | **`CRPRFEDEV`** | `datetime` | SI | Campo transaccional de Hosvital HIS |
|  | **`CRPRVUDEV`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CRPRVTDEV`** | `decimal(17,4)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CRPRCDDEV`** | `char(3)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CRPRCODEV`** | `decimal(15,0)` | SI | Campo transaccional de Hosvital HIS |
|  | **`CRPRSCDEV`** | `char(9)` | SI | Campo transaccional de Hosvital HIS |
